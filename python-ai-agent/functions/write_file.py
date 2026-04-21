import os
from functions.path_validator import validate_file_to_write
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes text content to a specified file, creating any necessary parent directories.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path where the file should be created or overwritten, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write into the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)


def write_file(working_directory, file_path, content):
    try:
        target_path = validate_file_to_write(working_directory, file_path)

        # Create any missing parent directories
        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        with open(target_path, 'w') as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"