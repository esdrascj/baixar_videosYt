from pytube import YouTube
from flask import Flask, render_template, request, session, url_for, redirect, send_file
from flask.helpers import url_for
from io import BytesIO

app = Flask(__name__)
@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == 'POST':
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
            url = url.streams.get_highest_resolution()
            titulo = url.title
        except:
            return render_template('error.html')
        return render_template('download.html')
    return render_template("index.html")

@app.route("/download", methods=["GET", "POST"])
def baixar():
    if request.method == "POST":
        buffer = BytesIO()
        url = YouTube(session['link'])
        video = url.streams.get_highest_resolution()
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name='video.mp4', mimetype='video/mp4')
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)