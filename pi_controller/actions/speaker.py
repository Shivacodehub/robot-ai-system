import pyttsx3

engine = pyttsx3.init()

def speak(text):
    """
    SOFTWARE TEAM:
    This text comes from LLM output.

    """
    if text:
        engine.say(text)
        engine.runAndWait()
