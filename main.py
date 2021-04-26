import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()


def SpeakText(command):
    engine = pyttsx3.init()
    engine.setProperty('volume', 10)
    engine.setProperty('rate', 130)
    engine.say(command)
    engine.runAndWait()

while(1):

    try:

        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)

            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say " + MyText)
            SpeakText(MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occured")
