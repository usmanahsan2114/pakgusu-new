import os

root_dir = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"
patch_file_name = "light-mode-patch.css"

def inject_patch(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if patch_file_name in content:
            print(f"Already patched: {file_path}")
            return

        # Calculate relative path to css folder
        # root_dir/css/light-mode-patch.css
        # file_path is something like root_dir/about/index.html
        
        # Determine depth from root
        rel_path_from_root = os.path.relpath(os.path.dirname(file_path), root_dir)
        
        if rel_path_from_root == ".":
            css_path = f"./css/{patch_file_name}"
        else:
            depth = rel_path_from_root.count(os.sep) + 1
            # For depth 1 (e.g. about), we need ../css
            # For depth 2 (e.g. products/cleanroom-panels), we need ../../css
            # But wait. os.relpath("about", root) is "about". NO separators. Depth is 1 level down.
            # "about" -> need "../css"
            # "products/cleanroom" -> need "../../css"
            
            # Count folder names in rel_path?
            depth = len(rel_path_from_root.split(os.sep))
            css_path = "../" * depth + f"css/{patch_file_name}"

        link_tag = f'    <link href="{css_path}" rel="stylesheet" /> <!-- LIGHT MODE PATCH -->'
        
        # Inject before </head>
        new_content = content.replace("</head>", f"{link_tag}\n</head>")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Patched: {file_path} (Link: {css_path})")
            
    except Exception as e:
        print(f"Error patching {file_path}: {e}")

# Walk directory
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file == "index.html":
            file_path = os.path.join(root, file)
            inject_patch(file_path)

print("Patching complete.")
