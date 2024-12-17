import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import pyaudio
import os
import time


# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")
            return ""


# Function to translate text
def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"Translation ({target_language}): {translation.text}")
    return translation.text


# Function to convert text to speech
def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language)
    tts_file = "translated.mp3"
    tts.save(tts_file)

    # Play the translated audio
    os.system(f"start {tts_file}")  # For Windows
    # os.system(f"mpg123 {tts_file}")  # For Linux
    time.sleep(5)  # Give it some time before deleting the file
    os.remove(tts_file)  # Remove the file after playing


# Main function to run the translator
def main():
    while True:
        input("Press Enter to start speaking...")
        speech_text = recognize_speech()
        if speech_text:
            target_lang = input("Enter target language code (e.g., 'es' for Spanish, 'fr' for French): ")
            translated_text = translate_text(speech_text, target_lang)
            text_to_speech(translated_text, target_lang)


if __name__ == "__main__":
    main()