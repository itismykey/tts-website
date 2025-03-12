from flask import Flask, render_template, request
from gtts import gTTS  # 使用 gTTS 做簡易 TTS
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        tts = gTTS(text)
        tts.save("static/output.mp3")
        return render_template('index.html', audio_file="output.mp3")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
