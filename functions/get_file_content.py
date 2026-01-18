import os

def get_file_content(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        max_chars = 10000
        with open(target_file, "r") as f:
            content = f.read(max_chars + 1)

        if len(content) > max_chars:
            content = content[:max_chars]
            return content + f"\n[...File truncated at {max_chars} characters...]"

        return content
    except Exception as e:
        return f"Error: {e}"
