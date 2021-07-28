import datetime

def create_post(title, text, filename, subtitle=None):
    input_file = open("./base.html", "rt")
    output_file = open(filename, "wt")
    data = input_file.read()
    data = data.replace('<!--Title-->', f'<h1>{title}</h1>')
    if subtitle != None:
        data = data.replace('<!--Subtitle-->', f'<h2 class="subheading">{subtitle}</h2>')
    data = data.replace('<!--Date-->', f'<span class="meta">Posted by <a href="./about.html">Guilherme Miranda Martins</a> on {datetime.date.today()}</span>')
    data = data.replace('<!--Texte-->', get_html_text(text))
    input_file.close()
    output_file.write(data)
    output_file.close()

def get_html_text(text):
    return "hello text"


#<h2 class="subheading">Problems look mighty small from 150 miles up</h2>
#<span class="meta">Posted by <a href="./about.html">Guilherme Miranda Martins</a>""</span>.format(datetime.date())


create_post("titre", "texte", "fichier.html")
