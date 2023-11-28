import os
from app import IMGS_DIR
import flor


def parse_page(filename):
    fn, _ = os.path.splitext(filename)
    return flor.log("page", int(fn.replace("page_", "")))


def list_files_in_directory(directory, key=None):
    if key:
        return sorted(os.listdir(directory), key=key)
    else:
        return sorted(os.listdir(directory))


def is_directory(path):
    return os.path.isdir(path)


def get_full_path(directory, file):
    return os.path.join(directory, file)


if __name__ == "__main__":
    if os.path.exists(IMGS_DIR):
        for file in list_files_in_directory(IMGS_DIR):
            full_path = get_full_path(IMGS_DIR, file)
            if not is_directory(full_path):
                continue
            flor.log("document", file)
            for i, file2 in enumerate(
                list_files_in_directory(full_path, key=parse_page)
            ):
                flor.log("first_page", 1 if i == 0 else 0)
