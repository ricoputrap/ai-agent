import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        common_path = os.path.commonpath([working_dir_abs, target_dir])
        is_target_dir_valid = common_path == working_dir_abs

        # target dir is outside of the permitted working directory
        if is_target_dir_valid == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # target_dir is NOT a directory
        if os.path.isdir(target_dir) == False:
            return f'Error: "{directory}" is not a directory'

        target_dir_name = "current" if directory == "." else f'"{directory}"'
        results = f"Result for {target_dir_name} directory:\n"

        for item in os.listdir(target_dir):
            path = os.path.join(target_dir, item)
            size = os.path.getsize(path)
            is_dir = os.path.isdir(path)

            results += f" - {item}: file_size={size} bytes, is_dir={is_dir}\n"

        return results
        # return f'Success: "{directory}" is within the working directory'

    except Exception as e:
        return f"Error: {e}"
