import os

def generate_main_index(dest_dir, style_css_path):
    index_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>geek</title>
<link rel="stylesheet" href="{style}">
</head>
<body>
<div class="container">
<h1>geek</h1>
<ul>
""".format(style=style_css_path)

    # 遍历当前目录下的所有子目录
    for subdir in os.listdir(dest_dir):
        subdir_path = os.path.join(dest_dir, subdir)
        if os.path.isdir(subdir_path):
            index_path = os.path.join(subdir_path, "index.html")
            # 检查子目录中是否存在index.html
            if os.path.exists(index_path):
                index_content += '<li><a href="{0}/index.html">{0}</a></li>\n'.format(subdir)

    index_content += """
</ul>
</div>
</body>
</html>
"""

    # 写入最外层的index.html文件
    with open(os.path.join(dest_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_content)

# 使用示例
dest_dir = "."  # 当前目录
style_css_path = "style.css"  # CSS样式文件的路径
generate_main_index(dest_dir, style_css_path)
