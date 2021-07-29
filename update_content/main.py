import datetime

def create_post(title, subtitle, text, filename):
    input_file = open("./post_base.html", "rt")
    output_file = open(filename, "wt")
    data = input_file.read()
    data = data.replace('<!--Title-->', f'<h1>{title}</h1>')
    if subtitle != None:
        data = data.replace('<!--Subtitle-->', f'<h2 class="subheading">{subtitle}</h2>')
    data = data.replace('<!--Date-->', f'<span class="meta">Posted by <a href="./about.html">Guilherme Miranda Martins</a> on {datetime.date.today()}</span>')
    data = data.replace('<!--Text-->', text)
    input_file.close()
    output_file.write(data)
    output_file.close()

def get_html():
    with open("content.txt", "r", encoding="utf-8") as content_file:
        lines = content_file.read().split('\n') 
        title = lines.pop(0)
        subtitle = lines.pop(0)
        filename = lines.pop(0)
        filename = filename[filename.index(":")+2:] +f"{datetime.date.today()}.html"
        filename = "../html_pages/articles/" + filename
        text = ""
        print(lines)
        for line in lines:
            if "big: " in line:
                text += f"<h2>{line[5:]}</h2>\n"
            elif "quote: " in line:
                text += f"<blockquote>{line[7:]}</blockquote>\n"
            else:
                text += f"<p>{line}</p>\n"
    return title, subtitle, text, filename
        

title, subtitle, text, filename = get_html()
create_post(title, subtitle, text, filename)

content_html_inject = """
                <div class="post-preview">
                    <a href="post.html">
                        <h2 class="post-title">
                            The reasons why I didn't make my website on Squarespace
                        </h2>
                        <!--Here-->
                    </a>
                    <p class="post-meta">Posted by <a href="./about.html">Guilherme Miranda Martins</a> on September 24, 2014</p>
                </div>
                <hr>
"""
html_subtitle_inject = """
                        <h3 class="post-subtitle">
                            Is it still relevant to use programming in order to make a blog ? 
                        </h3>
"""