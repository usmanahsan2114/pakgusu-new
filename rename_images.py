import os
import shutil

base_dir = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza\images\resources"

def to_kebab_case(name):
    # Remove parentheses, handle double spaces, ampersands
    name = name.replace("(", "-").replace(")", "")
    return name.lower().replace("  ", "-").replace(" & ", "-").replace(" – ", "-").replace(" ", "-").replace("---", "-").replace("--", "-")

def rename_recursive(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        # Rename files first
        for name in files:
            new_name = to_kebab_case(name)
            if name != new_name:
                old_path = os.path.join(root, name)
                new_path = os.path.join(root, new_name)
                print(f"Renaming file: {old_path} -> {new_path}")
                os.rename(old_path, new_path)
        
        # Rename directories
        for name in dirs:
            new_name = to_kebab_case(name)
            if name != new_name:
                old_path = os.path.join(root, name)
                new_path = os.path.join(root, new_name)
                print(f"Renaming directory: {old_path} -> {new_path}")
                os.rename(old_path, new_path)

if __name__ == "__main__":
    rename_recursive(base_dir)
