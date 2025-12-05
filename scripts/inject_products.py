import os

root_dir = r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza"
css_file_name = "products-redesign.css"

def inject_patch(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if css_file_name in content:
            print(f"Already injected in: {file_path}")
            return

        # Calculate relative path
        file_dir = os.path.dirname(file_path)
        rel_path = os.path.relpath(os.path.join(root_dir, "css", css_file_name), file_dir)
        rel_path = rel_path.replace("\\", "/")

        injection_string = f'<link href="{rel_path}" rel="stylesheet" />'
        
        # Inject after turnkey-redesign.css if it exists, otherwise before </head>
        target_marker = 'turnkey-redesign.css" rel="stylesheet" />'
        
        if target_marker in content:
            new_content = content.replace(target_marker, target_marker + "\n    " + injection_string)
        else:
            # Fallback to before head
            new_content = content.replace("</head>", injection_string + "\n</head>")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Successfully injected into: {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file == "index.html":
            file_path = os.path.join(root, file)
            inject_patch(file_path)
