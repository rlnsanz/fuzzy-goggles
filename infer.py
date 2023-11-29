import os
from app import IMGS_DIR
import flor
import torch

def parse_page(filename):
    fn, _ = os.path.splitext(filename)
    return int(fn.replace("page_", ""))


def list_files_in_directory(directory, key=None):
    if key:
        return sorted(os.listdir(directory), key=key)
    else:
        return sorted(os.listdir(directory))


def is_directory(path):
    return os.path.isdir(path)


def get_full_path(directory, file):
    return os.path.join(os.path.abspath(directory), file)


if __name__ == "__main__":
    from train import device
    model = torch.load("model.pth", map_location=device) if os.path.exists("model.pth") else None
    if model:
        print("Model loaded")
        print(model.device)
    if os.path.exists(IMGS_DIR):
        for file in flor.loop("docs", list_files_in_directory(IMGS_DIR)):
            full_path = get_full_path(IMGS_DIR, file)
            if not is_directory(full_path):
                continue
            for i, file2 in flor.loop(
                "pages", enumerate(list_files_in_directory(full_path, key=parse_page))
            ):
                flor.log("page_path", os.path.join(full_path, file2))
                if model:
                    print("Predicting...")
                    flor.log("first_page", 1 if model.predict(full_path, file2) else 0)
                else:
                    print("Defaulting...")
                    flor.log("first_page", 1 if i == 0 else 0)
