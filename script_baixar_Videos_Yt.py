from pytube import YouTube
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def baixar(link):
    url = YouTube(link)
    url = url.streams.get_highest_resolution()
    titulo = url.title
    if input("\nVocê deseja fazer o download do vídeo '{}'? (s/n) ".format(titulo.upper())) =="s":
        try:
            url.download()
            print("SUCESSO!")
        except:
            print("Ocorreu um erro, atualize e tente novamente.")

link = input("Informe o link do vídeo que será baixado do Youtube: ")
baixar(link)

if __name__ == '__main__':
    app.run(debug=True)