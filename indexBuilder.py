import os

# The start and end of your HTML file
html_top = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My CS Interactive Guides</title>
    <style>
        body { font-family: system-ui, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; }
        h1 { border-bottom: 2px solid #eee; padding-bottom: 10px; }
        .category { margin-top: 30px; }
        ul { line-height: 1.8; }
        a { color: #0366d6; text-decoration: none; font-weight: 500; }
        a:hover { text-decoration: underline; }
        h2 { text-transform: capitalize; }
    </style>
</head>
<body>
    <h1>Interactive Computer Science Guides</h1>
"""

html_bottom = """
</body>
</html>
"""

content = ""

# Folders to ignore (like git or css folders)
ignore_folders = ['.git', 'css', 'assets']

# Scan the directory
for item in sorted(os.listdir('.')):
    if os.path.isdir(item) and item not in ignore_folders:
        folder_name = item.replace('-', ' ') # Make 'data-structures' look like 'data structures'
        
        # Add the category header
        content += f'\n    <div class="category">\n        <h2>📂 {folder_name}</h2>\n        <ul>\n'
        
        # Scan for HTML files inside the folder
        for file in sorted(os.listdir(item)):
            if file.endswith('.html'):
                file_path = f"./{item}/{file}"
                clean_name = file.replace('.html', '').replace('-', ' ').title()
                content += f'            <li><a href="{file_path}">{clean_name}</a></li>\n'
                
        content += '        </ul>\n    </div>\n'

# Write everything to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_top + content + html_bottom)

print("index.html has been successfully rebuilt!")