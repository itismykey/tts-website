import os
from flask import Flask, render_template, request
from gtts import gTTS

app = Flask(__name__)

# 確保 static 資料夾存在
os.makedirs("static", exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        tts = gTTS(text)
        audio_path = "static/output.mp3"
        tts.save(audio_path)
        return render_template('index.html', audio_file="output.mp3")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
