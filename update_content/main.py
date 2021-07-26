from datetime import datetime

def create_post(title, text, filename, subtitle=None):
    input_file = open("./base.html", "rt")
    output_file = open(filename, "wt")
    data = input_file.read()
    data = data.replace('<!--Title-->', title)
    if subtitle != None:
        data = data.replace('<!--Subtitle-->', subtitle)
    data = data.replace('<!--Date-->', datetime.date())
    data = data.replace('<!--Texte-->', get_html_text(text))
    input_file.close()
    output_file.write(data)
    output_file.close()

def get_html_text(text):
    pass


#<h2 class="subheading">Problems look mighty small from 150 miles up</h2>
#<span class="meta">Posted by <a href="#">Guilherme Miranda Martins</a> on August 24, 2014</span>

create_post("titre", "texte", "fichier.html")
print(datetime.now())