from flask import Flask, render_template, request
from gtts import gTTS
import os
import uuid

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    # Get form values
    text = request.form.get('text')
    language = request.form.get('language')
    voice_gender = request.form.get('voice_gender')  # Corrected key
    speed = float(request.form.get('speed', 1.0))
    pitch = float(request.form.get('pitch', 1.0))

    # Generate the audio file
    tts = gTTS(text=text, lang=language, slow=(speed < 1))
    file_name = f"{uuid.uuid4()}.mp3"
    audio_path = os.path.join('static', 'audio', file_name)
    tts.save(audio_path)

    # Return the generated file to the template
    return render_template('index.html', audio_file=file_name)


if __name__ == '__main__':
    app.run(debug=True)
