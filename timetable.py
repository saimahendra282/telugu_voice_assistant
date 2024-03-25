"""
AND HERE WE ARE THIS FILE HAS A LOGIC THAT PRINT MY CURRENT AND NEXT CLASS DETAILS ALSO SEND NOTIFICATIONS TO MY PHONE LIKE U GOT NEXT CLASS THERE...
"""
# i hade taken 2 json files as data source for my class timetable

data = [
  {
          "timeSlot": "7:10 AM - 8:00 AM",
          "day": "MONDAY",
          "startTime": "7:10 AM",
          "endTime": "8:00 AM",
          "room": "NULL",
          "course": "NULL"
      },
      {
          "timeSlot": "8:00 AM - 8:50 AM",
          "day": "MONDAY",
          "startTime": "8:00 AM",
          "endTime": "8:50 AM",
          "room": "NULL",
          "course": "NULL"
      },

      {
          "timeSlot": "9:20 AM - 10:10 AM",
          "day": "MONDAY",
          "startTime": "9:20 AM",
          "endTime": "10:10 AM",
          "room": "NULL",
          "course": "NULL"
      },
      {
          "timeSlot": "10:10 AM - 11:00 AM",
          "day": "MONDAY",
          "startTime": "10:10 AM",
          "endTime": "11:00 AM",
          "room": "NULL",
          "course": "NULL"
      },
      {
          "timeSlot": "11:10 AM - 12:00 PM",
          "day": "MONDAY",
          "startTime": "11:10 AM",
          "endTime": "12:00 PM",
          "room": "NULL",
          "course": "NULL"
      },
      {
          "timeSlot": "12:00 PM - 12:50 PM",
          "day": "MONDAY",
          "startTime": "12:00 PM",
          "endTime": "12:50 PM",
         "room": "NULL",
          "course": "NULL"
      },
      {
          "timeSlot": "12:51 PM - 1:45 PM",
          "day": "MONDAY",
          "startTime": "12:51 PM",
          "endTime": "1:45 PM",
          "room": "NULL",
          "course": "NULL"
      },
      {
          "timeSlot": "1:45 PM - 2:35 PM",
          "day": "MONDAY",
          "startTime": "1:45 PM",
          "endTime": "2:35 PM",
          "room": "NULL",
          "course": "NULL"
      },
      {
          "timeSlot": "2:35 PM - 3:30 PM",
          "day": "MONDAY",
          "startTime": "2:35 PM",
          "endTime": "3:30 PM",
          "room": "NULL",
          "course": "NULL"
      },
      {
          "timeSlot": "3:40 PM - 4:30 PM",
          "day": "MONDAY",
          "startTime": "3:40 PM",
          "endTime": "4:30 PM",
          "room": "NULL",
          "course": "NULL"
      },
      {
          "timeSlot": "4:30 PM - 5:20 PM",
          "day": "MONDAY",
          "startTime": "4:30 PM",
          "endTime": "5:20 PM",
          "room": "NULL",
          "course": "NULL"
      },
  """ DO THE SAME FOR ALL DAYS 😑 I CANT TYPE MY FULL TIMETABLE YOU CAN MODIFY THIS JSON DATA AS YOU PLEASE.."""

  
]
# OTHER FILE ABOUT MENTOR DETAILS AND COURSE DETAILS
Secmen=[
  {
        "course": "NULL",
        "sec": "",
        "mentor": "",
        "des": "SOME DESCRIPTION ABOUT YOUR COURSE",
        "image": " "
    },
  """
  DO THE SAME FOR ALL COURSES..... 
  """
]
from datetime import datetime, timedelta
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
import pushbullet # we are gonna use this to send notifications to our mobile...
# https://youtu.be/tbzPcKRZlHg?si=e1Vpjjc6gPXRFodL this is refference link i followed to know how to integrste pushbullet api with python 


def talk(Command): # to make our code talk telugu
    tts = gTTS(Command, lang="te")
    tts.save("timetaple.mp3")
    audio = AudioSegment.from_mp3("timetaple.mp3")
    play(audio)
    os.remove("timetaple.mp3")


def send_notification(title, message):
    push = pushbullet.Pushbullet("u r access token")
    push.push_note(title, message)


def get_current_time():
    # Get the current time in the format "H:mm AM/PM"
    return datetime.now().strftime("%I:%M %p")


def get_current_day():
    # Get the current day as a string (e.g., "MONDAY")
    return datetime.now().strftime("%A").upper()


def parse_time(time_str):
    # Parse time string to datetime object
    return datetime.strptime(time_str, "%I:%M %p")

# here is filtering the current class logic based on starting time and date it filter the data from  json files and print it
def print_and_notify_class(class_info, title):
    room = class_info['room']
    course = class_info['course']
    time_slot = class_info['timeSlot']

    print(f"{title}: Room {room}, Course {course}, Time Slot {time_slot}")
    talk(f"Sir ప్రస్తుత క్లాస్రూమ్ నెంబర్ {room}.. and ప్రస్తుత కోర్స్ పేరు {course}, for టైమ్ స్లాట్ {time_slot}")
    talk("దయచేసి మీ టైం వేస్ట్ చేయకుండా బుద్ధిగా classes కి attend అవ్వండి. proxy లు చెప్పకండి మరియు చెప్పనివ్వకండి.")
  # below statement to send present class notification
    # send_notification(title, f"sir sai u have class at Room {room}, Course {course}, Time Slot {time_slot} right now so please stop wasting u r life and attend to class.")


def print_next_class(class_info):
    room = class_info['room']
    course = class_info['course']
    start_time = class_info['startTime']

    print(f"Next class: Room {room}, Course {course}, Start Time {start_time}")
    talk(f"mee తదుపరి క్లాస్: రూమ్ నెంబర్ {room} దగ్గర,and  కోర్స్ పేరు {course},and ప్రారంభ సమయం {start_time}")
    send_notification("Next Class Reminder", f"sir you have next class at Room {room},for  Course {course},and  Starting Time is {start_time} if u know where your class is, ignore this(ofcourse u dont know as ant have good memory than you), if u dont know then stop wasting your life on anime and go to class..")

# print the extra details like mentor and description
def check_current_class(data, current_time, current_day):
    selected_data = [item for item in data if
                     item["day"] == current_day and parse_time(item["startTime"]) <= current_time <= parse_time(
                         item["endTime"])]
    if selected_data:
        current_class = selected_data[0]
        print_and_notify_class(current_class, "Current Class")

        matching_secmen = [item for item in Secmen if item["course"] == current_class["course"]]
        if matching_secmen:
            next_secmen = matching_secmen[0]
            print(f"Mentor: {next_secmen['mentor']}, Description: {next_secmen['des']}")
            talk(f"మీ mentor విషయాలు: Mentor: {next_secmen['mentor']}, Description: {next_secmen['des']}")
        else:
            print("No mentor information found for the course.")
            talk("No mentor information found for the course.")
    else:
        print("No ongoing classes at the moment, Sir!")
        talk("No ongoing classes at the moment.")

# ...................................................................................................................................................................................................
def check_next_class(data, current_time, current_day):
    next_classes = [item for item in data if
                    item["day"] == current_day and parse_time(item["startTime"]) > current_time]
    if next_classes:
        next_class = next_classes[0]
        print_next_class(next_class)
    else:
        print("No more classes for today.")
        talk("No more classes for today.")


def main():
    current_time = parse_time(get_current_time())
    current_day = get_current_day()

    print(f"Current day: {current_day}, Current time: {current_time.strftime('%I:%M %p')}")

    check_current_class(data, current_time, current_day)
    check_next_class(data, current_time, current_day)


if __name__ == "__main__":
    main()
