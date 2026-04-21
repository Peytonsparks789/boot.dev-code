import os
from functions.path_validator import validate_directory
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def iterate_dir(current_dir, target_dir):
    for item in current_dir:
        current_path = os.path.join(target_dir, item)

        if os.path.isdir(current_path):
            yield f"  - {item}: file_size={os.path.getsize(current_path)} bytes, is_dir=True"
            yield from iterate_dir(os.listdir(current_path), current_path)
        yield f"  - {item}: file_size={os.path.getsize(current_path)} bytes, is_dir={False}"

def get_files_info(working_directory, directory="."):
    try:
        target_dir = validate_directory(working_directory, directory)

        return "\n".join(iterate_dir(os.listdir(target_dir), target_dir))
    except Exception as e:
        return f"    Error: {e}"