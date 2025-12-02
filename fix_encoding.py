import os

root_path = r"c:\xampp\htdocs\pakgusu-new\intoriza"

# Replacements map
replacements = {
    "â€“": "–",  # En-dash
    "Ã—": "×",   # Multiplication sign
    "Â©": "©",   # Copyright
    "Â ": " ",   # Non-breaking space artifact
    "â€™": "’",  # Right single quote
    "â€œ": "“",  # Left double quote
    "â€": "”"    # Right double quote (incomplete?)
}

for root, dirs, files in os.walk(root_path):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                for bad, good in replacements.items():
                    content = content.replace(bad, good)
                
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Fixed: {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")
