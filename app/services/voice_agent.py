import whisper
from gtts import gTTS
import os

def transcribe_audio(audio_path: str) -> str:
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

def generate_voice(text: str, output_file: str):
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)
    os.system(f"start {output_file}")  # This will play the file on Windows
