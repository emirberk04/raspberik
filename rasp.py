import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='tr-TR')
            print("You said: " + command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

def main():
    speak("Merhaba, size nasıl yardımcı olabilirim?")
    
    while True:
        command = listen()
        
        if "merhaba" in command:
            speak("Merhaba! Size nasıl yardımcı olabilirim?")
        elif "nasılsın" in command:
            speak("Ben bir yapay zekayım, duygularım yok ama iyi olduğumu söyleyebilirim!")
        elif "çıkış" in command:
            speak("Görüşmek üzere!")
            break
        else:
            speak("Maalesef bu komutu anlayamadım.")

if __name__ == "__main__":
    main()