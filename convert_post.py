import markdown
from pathlib import Path

# INPUT: your markdown filename
markdown_file = "i-hate-github-desktop.md"
output_file = "posts/i-hate-github-desktop.html"

# Basic HTML wrapper
template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>
    body {{
      background-color: #000;
      color: #00FF00;
      font-family: "Courier New", monospace;
      padding: 2em;
    }}
    a {{
      color: #00FFFF;
    }}
    code {{
      background: #111;
      padding: 2px 4px;
      border-radius: 4px;
      font-size: 90%;
    }}
  </style>
</head>
<body>
  <h1>{title}</h1>
  <div class="post">
    {content}
  </div>
  <p><a href="../index.html">← Back to blog</a></p>
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
