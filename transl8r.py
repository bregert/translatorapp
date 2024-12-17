import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Initialize recognizer and translator
r = sr.Recognizer()
translator = Translator()


def listen_and_translate(source_lang, target_lang):
    """
    Listens to user speech, translates it, and speaks the translated text.
    """
    with sr.Microphone() as source:
        print("Speak now:")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said:", text)

            translation = translator.translate(text, dest=target_lang).text
            print(f"Translation: {translation}")

            engine = pyttsx3.init()
            engine.say(translation)
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


# Example usage
source_language = "en"  # Source language (e.g., "en" for English)
target_language = "es"  # Target language (e.g., "es" for Spanish)

listen_and_translate(source_language, target_language)