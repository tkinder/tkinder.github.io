import markdown
from pathlib import Path

# INPUT: your markdown filename
markdown_file = "i-hate-github-desktop.md"
output_file = "posts/i-hate-github-desktop.html"

# Basic HTML wrapper
template = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <div class="post">
    {content}
  </div>
</body>
</html>
"""

# Read and convert markdown
md_text = Path(markdown_file).read_text(encoding="utf-8")
html_content = markdown.markdown(md_text)

# First line as title
title = md_text.splitlines()[0].replace("#", "").strip()

# Write the final HTML file
Path(output_file).write_text(template.format(title=title, content=html_content), encoding="utf-8")
print(f"Converted {markdown_file} -> {output_file}")
