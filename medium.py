#  NO API USED THERE IS A PACKAGE CALLED feedparser to do these things
import feedparser
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
def talk(Command):
    tts = gTTS(Command, lang="te")
    tts.save("mediumm.mp3")

    # Load the audio file
    audio = AudioSegment.from_mp3("mediumm.mp3")

    # Play the audio
    play(audio)

    # Remove the audio file after playback
    os.remove("mediumm.mp3")
def get_medium_articles(username):
    medium_rss_url = f"https://medium.com/feed/@{username}"
    feed = feedparser.parse(medium_rss_url)
    articles = []

    for entry in feed.entries:
        articles.append(entry.title)

    return articles
username = 'bejawadasaimahendra'
articles = get_medium_articles(username)

print("Your Medium Articles:")
talk("మీ Medium Articles:")
for idx, article in enumerate(articles, start=1):
    print(f"{idx}. {article}")
    talk(f"{idx}. {article}")
