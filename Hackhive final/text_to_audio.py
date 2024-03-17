import os
import pyttsx3
from gtts import gTTS

# Text to be converted to audio
statement = "Good Morning Mansi, have a good day"

# Using gTTS to convert text to audio file
tts = gTTS(statement)
tts.save("output44478.mp3")

# Using pyttsx3 to play the audio file
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
engine.say(statement)
engine.runAndWait()

# Playing the saved audio file
# os.system("start output.mp3")
