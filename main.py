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
listener = sr.Recognizer()
translator = Translator(to_lang='en', from_lang='te')

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
                exec_social()
            elif "మీడియం" in par: # to print my medium blogs headlines.
                exec_medium()
            elif "న్యూస్" in par: # to get 10 trending news topics in telugu.
                exec_news()
            elif "కమాండ్స్" in par or "కొమాండ్స్" in par: # to show all the commands coded till now.
                show_comaands()
            elif "నా క్లాస్" in par: # to print where is my class right now.
                exec_tt()
            elif "మెస్సేజ్" in par or "మెసేజ్" in par: # well this logic is used to send whatsapp messege.
                send_whatsapp_message()
            elif "బాయ్ బాయ్" in par: # to exit the code
                talk("అలాగే code ని ఆపేస్తున్నాను")
                exit()

            else:
                print("command not found")

"""
well now we have written the logic now time to define the methods in if-else logic.
"""
def send_whatsapp_message():  # when  this method was called it asks user to choose the option to send messege and based on that after 50 secs it will send the messege.
    contacts = {
        "myself": "+911234567890",
        "add as many as you want"
    }
    print("Choose a contact:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact}")
    contact_choice = int(input("Enter the number corresponding to your choice: "))
    selected_contact = list(contacts.keys())[contact_choice - 1]
    selected_phone_number = contacts[selected_contact]
    message = input("Enter the message to be sent: ")
    current_time = dt.datetime.now()
    scheduled_time = current_time + dt.timedelta(minutes=1, seconds=30)
    kit.sendwhatmsg(selected_phone_number, message, scheduled_time.hour, scheduled_time.minute)

def exec_tt(): # well dont worry there is no predefined method like this i just invoked the main function in timetable.py file
    timetable.main() # this will print my class timimng like were is my class right now.

def exec_coding():
    # this will ask user to coose what profile to open and open's them on webbrowser.
    talk("అలాగే ఏ ప్రొఫైల్ ఓపెన్ చేయాలో type చేయండి")
    print("These are the coding profiles you can access: 1.codechef\n2.hackerrank\n3.leetcode\n4.atcoder\n5.codepen")

    profile_name = input("Enter the name of the coding profile: ").lower()
    if "codechef" in profile_name:
        webbrowser.open("https://www.codechef.com/users/sai_2200030548")
    elif "hackerrank" in profile_name:
        webbrowser.open("https://www.hackerrank.com/profile/h2200030548")
    elif "leetcode" in profile_name:
        talk("మీ leetcode  ప్రొఫైల్ 28/03/24 తారీఖు కాళ్ళ డిలీట్ అవ్వబోతుంది,so i am opening normal home page.")
        webbrowser.open("https://leetcode.com")
    elif "atcoder" in profile_name:
        webbrowser.open("https://atcoder.jp/users/sai_mahendra")
    elif "codepen" in profile_name:
        webbrowser.open("https://codepen.io/saimahendra")
    else:
        talk("మీరు అవి చేయడమే ఎక్కువ మూసుకొని మీరు చేసే కోడింగ్ ప్రొఫైల్ పేరు మాత్రమే ఇవ్వండి.")
        print("bro give only u r registered copy paste profile only")
def exec_social(): # same to print/open my social media accounts
    talk("ok")
    print("These are the social profiles you can access: 1.linkedin\n2.github\n3.facebook\n4.instagram")
    pro=input("enter profile name:")
    if "linkedin" in pro:
        webbrowser.open("https://www.linkedin.com/in/bejawada-sai-mahendra-b18289212/")
    elif "github" in pro:
        webbrowser.open("https://github.com/saimahendra282")
    elif "facebook" in pro:
        webbrowser.open("https://www.facebook.com/sunny.sunstromium/")
    elif "medium" in pro:
        webbrowser.open("https://medium.com/@bejawadasaimahendra")
    elif "instagram" in pro:
        webbrowser.open("https://www.instagram.com/sai_mahendra_bejawada/")
    else:
        talk("mee social media profiles maathrame ivvandi.")
        print("bro give only u r profiles not others... why r u this dumb? 😒🫤😕🥹🫨")
# next is funciton to set up alarm
def exec_alarm():
    hr = int(input("enter hrs:")) 
    # eg input: 8:34 pm i formatted this as 12 hours cause i am dumb to understand 24 hours clock......🥲
    min = int(input("enter min:"))
    mm = input("am or pm: ")

    if mm == "pm":
        hr += 12
    while True:
        if hr == dt.datetime.now().hour and min == dt.datetime.now().minute:
            print("times up")
            playsound("sample.mp3") # plays when time's up
            break
"""
these below are written on other files so i made them to get execute when the method is being called
"""
def exec_news():
    script_path = r"news.py"
    subprocess.run(["python", script_path])
def exec_medium():
    script_path = r"medium.py"
    subprocess.run(["python", script_path])
def exec_weather():
    script_path = r"weather.py"
    subprocess.run(["python", script_path])
# next is method to show all available commands as the code is not a language model to ans every text we are asking..and i can't remember my the commands i coded on if-else logic so i did that.
def show_comaands():
    print("sure here are the commans u coded.")
    print("""
    సమయం - సమయం చెప్పేందుకు
    youtube - youtube open chesendhuku
    google - google open chesendhuku
    వాతావరణం - వాతావరణం చెప్పేందుకు
    అలారం - అలారం set cheyadaaniki
    కోడింగ్ ప్రొఫైల్ - to open coding profiles
    సోషల్ మీడియా - to open social profiles
    మీడియం - to print medium articles
    న్యూస్ - to print latest news
    మెస్సేజ్ - to send whatsapp message
    బాయ్ బాయ్ - to exit the code.
    """)
    
if __name__ == '__main__':
    main()
