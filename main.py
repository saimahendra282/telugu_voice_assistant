# coding starts 
import subprocess
import webbrowser
import pywhatkit as kit
import speech_recognition as sr
import pushbullet
import timetable
from gtts import gTTS
import datetime as dt
import pywhatkit as pk
from pydub import AudioSegment
from pydub.playback import play
from translate import Translator
import os
from playsound import playsound
# refer to requirement.txt for packages installing.....
# first module to make our code to speak telugu language..
# as we dont have predefined packages to make it talk telugu we are gonna use mp3 files like create and delete'em on the spot after task is finished
def talk(Command):
    tts = gTTS(Command, lang="te")
    tts.save("sai.mp3")
    # Load the audio file
    audio = AudioSegment.from_mp3("sai.mp3")
    # Play the audio
    play(audio)
    # Remove the audio file after playback
    os.remove("sai.mp3")
"""next to make it listen telugu words.
the below method will take telugu voice input and change to text and return it
Later we are going to use that text in if-else logical statements.
"""
def takeCmd():
    command = ""
    try:
        with sr.Microphone() as source:
            print("I am listening")
            audio = listener.listen(source)
            command = listener.recognize_google(audio, language="te")
            print(command)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except Exception as e:
        print("An error occurred: {0}".format(e))
    return command
  """
  now let's add  a greeting line like every time we execute the code it greets us.
  i did that using datetime,so it will greet us according to time of execution...
  """
def greet():
    print("initiating..........")
    current_time = dt.datetime.now()
    hour = current_time.hour
    if 0 <= hour < 12:
        greeting = "శుభోదయం "  
    elif 12 <= hour < 15:
        greeting = "శుభ మధ్యాహ్నం "  
    elif 15 <= hour < 19:
        greeting = "శుభ సాయంత్రం "  
    else:
        greeting = "శుభ రాత్రి "  
    print(greeting)

    talk(f"{greeting} sai mahendra sir, and welcome to  sunstromium A.I TELUGU VERSION")
    talk("intiating")
"""
real logic .. i mean  if else logic starts 
"""
# first greeting method
greet()
# next logic i written in main() seperate method.
def main():
    while True:
        par = takeCmd()
        # par=input("enter command") # for typing input
        if par:
            if "సమయం" in par: # to display and talk time 
                time = dt.datetime.now().strftime('%I:%M %p')
                print(time)
                talk(time)
            elif "youtube" in par: # it is predefined method in pywhatkit package used to play video dirctly on youtube
                talk("ఏ టాపిక్  ప్లే చేయాలో చెప్పండి")
                see = takeCmd()
                translated_input = translator.translate(see) # well it passes telugu text according to takecmd() so i used google translater to change to eng text and pass it to next statement.
                pk.playonyt(translated_input)
            elif "google" in par:
                talk("ఏ టాపిక్ సెర్చ్ చేయాలో చెప్పండి.")
                par = takeCmd()
                translated_input = translator.translate(par) # same here translating telugu text to eng txt
                pk.search(translated_input)
            elif "వాతావరణం" in par: # to print the weather details 
                exec_weather()
            elif "అలారం" in par: # to set up hacking
                exec_alarm()
            elif "కోడింగ్ ప్రొఫైల్ " in par: # to display my coding profiles
                exec_coding()
            elif "సోషల్ మీడియా" in par: # to display my social media profiles
              # ⚠️⚠️⚠️⚠️⚠️⚠️⚠️
                exec_social()
            elif "మీడియం" in par:
                exec_medium()
            elif "న్యూస్" in par:
                exec_news()
            elif "కమాండ్స్" in par or "కొమాండ్స్" in par:
                show_comaands()
            elif "నా క్లాస్" in par:
                exec_tt()
            elif "మెస్సేజ్" in par or "మెసేజ్" in par:
                send_whatsapp_message()
            elif "బాయ్ బాయ్" in par:
                talk("అలాగే code ని ఆపేస్తున్నాను")
                exit()

            else:
                print("command not found")


if __name__ == '__main__':
    main()
