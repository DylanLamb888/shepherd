import os

from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_directory = os.path.normpath(os.path.join(abs_working_dir, directory))
        abs_directory = os.path.abspath(target_directory)

        if os.path.commonpath([abs_working_dir, abs_directory]) != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_directory):
            return f'Error: "{directory}" is not a directory'

        result = []
        for item in os.listdir(abs_directory):
            item_path = os.path.join(abs_directory, item)
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            result.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(result)
    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files and directories in a specified directory. Use this to see what files exist, not to execute them.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory",
            ),
        },
    ),
)