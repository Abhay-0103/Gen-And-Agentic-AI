import speech_recognition as sr

def main():
    r = sr.Recognizer() # Speech to Text

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        print("Kuch Bol NA BSDK: ")
        audio = r.listen(source)

        print("Speak Something: ")
        stt = r.recognize_google(audio)

        print("You Said:", stt)

if __name__ == "__main__":
    main()