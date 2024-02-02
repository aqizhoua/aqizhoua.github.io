import os
import shutil
os.environ["PYTHONIOENCODING"] = "utf-8"
def copy_html_files_and_generate_index(source_dir, dest_dir,lesson_name):
    # 确保目标目录存在
    os.makedirs(dest_dir, exist_ok=True)
    # 存储目录结构
    dir_structure = {}

    for root, dirs, files in os.walk(source_dir):
        html_files = [f for f in files if f.endswith(".html")]
        if html_files:
            relative_path = os.path.relpath(root, source_dir)
            dir_structure[relative_path] = html_files
            for file in html_files:
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest_dir, relative_path, file)
                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                shutil.copy(src_file_path, dest_file_path)

    # 生成目录索引的HTML页面
    with open(os.path.join(dest_dir, "index.html"), "w", encoding="utf-8") as f_index:
        f_index.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n")
        f_index.write(
            f"<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<title>{lesson_name}</title>\n<link rel=\"stylesheet\" href=\"../style.css\"></head>\n<body>\n")
        f_index.write(f"<div class=\"container\">\n<h1>{lesson_name}</h1>\n<ul>\n")
        for subdir in sorted(dir_structure.keys()):
            index_path = os.path.join(subdir, "index.html")
            f_index.write(f"<li><a href=\"{index_path}\">{subdir}</a></li>\n")

            # 为每个子目录生成HTML页面
            with open(os.path.join(dest_dir, index_path), "w", encoding="utf-8") as f_subdir:
                f_subdir.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n")
                f_subdir.write(
                    f"<meta charset=\"UTF-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n<title>{subdir}</title>\n<link rel=\"stylesheet\" href=\"../../style.css\"></head>\n<body>\n")
                f_subdir.write(f"<div class=\"container\">\n<h1>{subdir}</h1>\n<ul>\n")
                for file in sorted(dir_structure[subdir]):
                    # file_path = os.path.join(subdir, file) # 这一行注释似乎是您考虑过的路径问题，但在实际代码中没有使用
                    f_subdir.write(f"<li><a href=\"{file}\">{file}</a></li>\n")
                # 添加返回上一级目录的链接
                f_subdir.write('<li><a href="../index.html">回到专栏</a></li>\n')
                # 添加返回上一级目录的链接
                f_subdir.write('<li><a href="../../index.html">回到geek</a></li>\n')
                f_subdir.write("</ul>\n</div>\n</body>\n</html>")
        # 添加返回上一级目录的链接
        f_index.write('<div><a href="../index.html">回到geek</a></div>\n')
        f_index.write("</ul>\n</div>\n</body>\n</html>")

if __name__ == '__main__':
    source_dir = r'D:\极客时间\MySQL实战45讲'

    lesson_name = os.path.basename(source_dir).split("-")[-1]
    dest_dir = fr'D:\hexo\source\geek\{lesson_name}'
    os.makedirs(dest_dir,exist_ok=True)
    copy_html_files_and_generate_index(source_dir, dest_dir,lesson_name)