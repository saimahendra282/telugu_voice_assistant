# API SOURCE: gnews.io
# this code will print the india's trending telugu news
import json
import urllib.request
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
def talk(Command):
    tts = gTTS(Command, lang="te")
    tts.save("newss.mp3")

    # Load the audio file
    audio = AudioSegment.from_mp3("newss.mp3")

    # Play the audio
    play(audio)

    # Remove the audio file after playback
    os.remove("newss.mp3")

apikey = "type u r api key here"
category = "general"
url = f"https://gnews.io/api/v4/top-headlines?category={category}&lang=te&country=in&max=10&apikey={apikey}" # fetching from api

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))
    articles = data["articles"]

    # Iterate through articles in reverse order to print the latest news first
    for i in range(len(articles) - 1, -1, -1):
        print(f"Title: {articles[i]['title']}")
        talk(f"Title: {articles[i]['title']} and ")
        print(f"Description: {articles[i]['description']}")
        print()  # Add an empty line between articles
