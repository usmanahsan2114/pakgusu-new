import re

# Read the file
with open(r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza\index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace ./../ with just the path (for root level, no ../ needed)
content = content.replace('href="./../', 'href="./')
content = content.replace('src="./../', 'src="./')

# Write back
with open(r"c:\xampp\htdocs\pakgusu-1\intoriza\pakgusu-new\intoriza\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Cleaned up root index.html links to proper format")
