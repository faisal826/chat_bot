import tkinter as tk
from urllib import response
from keras.models import load_model
import nltk
import pickle
import json
import random
import numpy as np
import tkinter.scrolledtext as st
from nltk.stem import WordNetLemmatizer
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Load the model and other necessary data
model = load_model('chatbot_model.h5')
intents = json.loads(open('English.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# Utility Methods (You can reuse your existing methods)
# ...

def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        user_input = r.recognize_google(audio)
        print("You: " + user_input)
        chatbot_response(user_input)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def chatbot_response(text):
    # Your chatbot response logic here
    # ...

    # Use gTTS for voice output
    tts = gTTS(response)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")  # You might need to adjust this command based on your system

# GUI Initialization
def send_message():
    user_message = entry.get()
    chat_display.insert(tk.END, "You: " + user_message + "\n")
    entry.delete(0, tk.END)
    chatbot_response(user_message)

root = tk.Tk()
root.title("Chatbot GUI")

frame = tk.Frame(root)
frame.pack(pady=10)

chat_display = st.ScrolledText(frame, width=50, height=20)
chat_display.pack()

entry = tk.Entry(frame, width=50)
entry.pack(pady=10)

voice_button = tk.Button(frame, text="Voice Input", command=voice_input)
voice_button.pack()

send_button = tk.Button(frame, text="Send", command=send_message)
send_button.pack()

root.mainloop()
