import datetime

content_html_inject = """
                <div class="post-preview">
                    <a href="ARTICLE_LINK">
                        <h2 class="post-title">
                            <!--Title-->
                        </h2>
                        <!--Subtitle-->
                    </a>
                    <p class="post-meta">Posted by <a href= "./about.html" >Guilherme Miranda Martins</a> on DATE_HERE</p>
                </div>
                <hr>
                <!--Content-->"""
html_subtitle_inject = """
                        <h3 class="post-subtitle">
                            <!--Subtitle_text-->
                        </h3>"""

date_format = datetime.date.today()
date_format = date_format.strftime("%b %d, %Y")

def create_post(title, subtitle, text, filename, img_ref="post-bg.jpg"):
    input_file = open("./post_base.html", "rt")
    filename = "../html_pages/articles/" + filename
    output_file = open(filename, "wt")
    data = input_file.read()
    data = data.replace('<!--Title-->', f'<h1>{title}</h1>')
    if subtitle != None:
        data = data.replace('<!--Subtitle-->', f'<h2 class="subheading">{subtitle}</h2>')
    data = data.replace('<!--Date-->', f'<span class="meta">Posted by <a href="../about.html">Guilherme Miranda Martins</a> on {date_format}</span>')
    data = data.replace('<!--Text-->', text)
    img_url = f"url('../../img/{img_ref}')"
    data = data.replace("URL_HERE", img_url)
    input_file.close()
    output_file.write(data)
    output_file.close()

def get_html_for_post():
    with open("content.txt", "r", encoding="utf-8") as content_file:
        lines = content_file.read().split('\n') 
        title = lines.pop(0)
        subtitle = lines.pop(0)
        filename = lines.pop(0)
        img_ref = lines.pop(0)
        filename = filename[filename.index(":")+2:] +f"{datetime.date.today()}.html"  
        text = ""
        for line in lines:
            if "big: " in line:
                text += f"<h2>{line[5:]}</h2>\n"
            elif "quote: " in line:
                text += f"<blockquote>{line[7:]}</blockquote>\n"
            else:
                text += f"<p>{line}</p>\n"
    return title, subtitle, text, filename, img_ref
        

def modify_content(title, filename, subtitle = None):
    filename = "./articles/" + filename
    input_file = open("../html_pages/content.html", "rt")
    data = input_file.read()
    data = data.replace("<!--Content-->", content_html_inject)
    if subtitle != None:
        data = data.replace("<!--Subtitle-->", html_subtitle_inject)
        data = data.replace("<!--Subtitle_text-->", subtitle)
    data = data.replace("<!--Title-->", title)
    data = data.replace("ARTICLE_LINK", filename)
    data = data.replace("DATE_HERE", date_format)
    input_file.close()
    output_file = open("../html_pages/content.html", "wt")
    output_file.write(data)
    output_file.close()

def modify_index(title, filename, subtitle=None):
    filename = "./html_pages/articles/" + filename
    input_file = open("./index_copy.html", "r", encoding = "utf-8")
    lines = input_file.read().split('\n')
    content={"post1": None, "post2": None, "post3": None}
    for number in range(1, 4):
        start_index = lines.index("<!--start-->")
        end_index = lines.index("<!--end-->")
        if number == 1:
            content["post2"] = lines[start_index: end_index+1]
        elif number == 2:
            content["post3"] = lines[start_index: end_index+1]
        lines[start_index: end_index+1] = [f"<!--post{number}-->"]
    post1 = content_html_inject
    post1 = "<!--start-->" + post1 + "\n<!--end-->"
    post1 = post1.replace("<!--Title-->", title)
    post1 = post1.replace("ARTICLE_LINK", filename)
    post1 = post1.replace("DATE_HERE", date_format)
    post1 = post1.replace("./about.html", "./html_pages/about.html")
    if subtitle != None:
        post1 = post1.replace("<!--Subtitle-->", html_subtitle_inject)
        post1 = post1.replace("<!--Subtitle_text-->", subtitle)
    input_file.close()
    content["post1"] = [post1]
    output_file = open("../index_bis.html", "wt")
    lines = "\n".join(lines)
    for key in content.keys():
        lines = lines.replace(f"<!--{key}-->","\n".join(content[key]))
    output_file.write(lines)
    output_file.close()
    

#MAIN#


title, subtitle, text, filename, img_ref = get_html_for_post()
title = title[7:]
subtitle = subtitle[10:]
img_ref = img_ref[5:]

create_post(title, subtitle, text, filename, img_ref)
modify_content(title, filename, subtitle)

modify_index(title, filename, subtitle)

