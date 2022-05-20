"""
UNDER DEVELOPMENT
This script allows you to control the ant using voice commands. 
It listens for the wake word and awaits a command.
"""

import pyttsx3
import speech_recognition as sr
from ax12.movement import flip, rotate, walk, sit, stand, connect


WAKE = "tiger"


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_sphinx(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()


def main():

    servos = connect()

    while True:
        print("\nSay 'tiger' to wake . . .")
        text = get_audio()

        if text.count(WAKE) > 0:
            speak("hello")
            text = get_audio()
            print("COMMAND:", text)

            FLIP_STRS = ["flip", "show us a flip"]
            for phrase in FLIP_STRS:
                if phrase in text:
                    speak("sure")
                    flip(servos)

            LEFT_STRS = ["rotate to left", "rotate to the left",
                         "spin to the left", "spin left"]
            for phrase in LEFT_STRS:
                if phrase in text:
                    speak("yes sir")
                    rotate(servos, "CCW")

            RIGHT_STRS = ["rotate to right", "rotate to the right",
                          "spin to the right", "spin right"]
            for phrase in RIGHT_STRS:
                if phrase in text:
                    speak("spinning to the right now")
                    rotate(servos, "CW")

            ROTATE_STRS = ["rotate", "spin"]
            for phrase in ROTATE_STRS:
                if phrase in text:
                    speak("left or right")
                    text = get_audio()

                    LEFT_STRS = ["left"]
                    for phrase in LEFT_STRS:
                        if phrase in text:
                            speak("copy that")
                            rotate(servos, "CCW")

                    RIGHT_STRS = ["right"]
                    for phrase in RIGHT_STRS:
                        if phrase in text:
                            speak("spinning to right now")
                            rotate(servos, "CW")

            WALK_STRS = ["walk", "go"]
            for phrase in WALK_STRS:
                if phrase in text:
                    speak("here i go")
                    walk(servos)

            SIT_STRS = ["sit", "sit down"]
            for phrase in SIT_STRS:
                if phrase in text:
                    speak("okay")
                    sit(servos)

            STAND_STRS = ["stand", "stand up"]
            for phrase in STAND_STRS:
                if phrase in text:
                    speak("okay")
                    stand(servos)


if __name__ == "__main__":
    main()
