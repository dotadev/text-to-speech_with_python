from flask import Flask, render_template, request, send_file
from gtts import gTTS, lang
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    languages = lang.tts_langs()
    return render_template('index.html', languages=languages)

@app.route('/preview', methods=['POST'])
def preview():
    text = request.form['text']
    language = request.form['language']
    tts = gTTS(text, lang=language)
    mp3_fp = BytesIO()
    tts.save(mp3_fp)
    mp3_fp.seek(0)
    return send_file(mp3_fp, mimetype='audio/mpeg', as_attachment=False, attachment_filename='preview.mp3')

@app.route('/download', methods=['POST'])
def download():
    text = request.form['text']
    language = request.form['language']
    tts = gTTS(text, lang=language)
    tts.save('output.mp3')
    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run()
