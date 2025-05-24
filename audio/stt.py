import speech_recognition as sr
from playsound import playsound

def transcribe_audio_to_text():
    """
    Transcribes audio input from the microphone to text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("static/sounds/start_alert.mp3")  # Play start recording sound
        audio = recognizer.listen(source)
        playsound("static/sounds/stop_alert.mp3")  # Play stop recording sound

        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            return None