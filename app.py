import os
from flask import Flask, render_template, request
from TTS.api import TTS

app = Flask(__name__)
os.makedirs("static", exist_ok=True)

# 載入 Coqui TTS 模型
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        audio_path = "static/output.wav"
        tts.tts_to_file(text=text, file_path=audio_path)
        return render_template('index.html', audio_file="output.wav")
    return render_template('index.html')

if __name__ == '__main__':
    # 取得 Render 自動分配的 PORT，若不存在則預設為 10000
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
