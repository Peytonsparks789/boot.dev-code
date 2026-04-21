import os
import subprocess
from functions.path_validator import validate_file_to_execute
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the working directory and returns its output.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python (.py) file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of command-line arguments to pass to the script.",
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        target_path = validate_file_to_execute(working_directory, file_path)

        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_path]

        if args: command.extend(args)

        completed_process = subprocess.run(
            command,
            cwd=working_directory,
            capture_output = True,
            text = True,
            timeout = 30
        )

        if completed_process.returncode != 0:
            return f"Process exited with code {completed_process.returncode}"
        if not completed_process.stdout and not completed_process.stderr:
            return "No output produced"
        return f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"

    except Exception as e:
        return f"Error: executing Python file: {e}"