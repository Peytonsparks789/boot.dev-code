import os

def _validate_path(working_directory, path, *, check, outside_msg, invalid_msg):
    working_dir_abs = os.path.abspath(working_directory)
    target = os.path.normpath(os.path.join(working_dir_abs, path))

    if os.path.commonpath([working_dir_abs, target]) != working_dir_abs:
        raise Exception(outside_msg.format(path=path))
    if not check(target):
        raise Exception(invalid_msg.format(path=path))

    return target


def validate_file(working_directory, file_path):
    return _validate_path(
        working_directory,
        file_path,
        check=os.path.isfile,
        outside_msg='Cannot read "{path}" as it is outside the permitted working directory',
        invalid_msg='File not found or is not a regular file: "{path}"'
    )


def validate_directory(working_directory, directory):
    return _validate_path(
        working_directory,
        directory,
        check=os.path.isdir,
        outside_msg='Cannot list "{path}" as it is outside the permitted working directory',
        invalid_msg='"{path}" is not a directory'
    )

def validate_file_to_write(working_directory, file_path):
    return _validate_path(
        working_directory,
        file_path,
        check=lambda p: not os.path.isdir(p),
        outside_msg='Error: Cannot write to "{path}" as it is outside the permitted working directory',
        invalid_msg='Error: Cannot write to "{path}" as it is a directory'
    )

def validate_file_to_execute(working_directory, file_path):
    return _validate_path(
        working_directory,
        file_path,
        check=os.path.isfile,
        outside_msg='Error: Cannot execute "{path}" as it is outside the permitted working directory',
        invalid_msg='Error: "{path}" does not exist or is not a regular file'
    )