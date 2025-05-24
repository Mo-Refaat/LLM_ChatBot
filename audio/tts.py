from gtts import gTTS
import io

def convert_text_to_audio(text):
    """
    Converts text to audio using gTTS and returns the audio as a byte stream.
    """
    try:
        tts = gTTS(text=text, lang="en")
        audio_stream = io.BytesIO()
        tts.write_to_fp(audio_stream)
        audio_stream.seek(0)  
        return audio_stream
    except Exception as e:
        print(f"Error in TTS: {e}")
        return None
