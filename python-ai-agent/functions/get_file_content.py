from config import MAX_CHARS
from functions.path_validator import validate_file
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the text content of a specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)


def get_file_content(working_directory, file_path):
    try:
        target_path = validate_file(working_directory, file_path)
        with open(target_path, 'r') as file:
            contents = file.read(MAX_CHARS)
            if file.read(1):
                contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            file.close()
            return contents
    except Exception as e:
        return f"    Error: {e}"