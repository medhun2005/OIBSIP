import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk
#from distutils.version import LooseVersion

class AssistanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        # Initialize the text-to-speech engine
        self.engine = pyttsx3.init()

        # Initialize recognizer and microphone
        self.listener = sr.Recognizer()
        self.microphone = sr.Microphone()
        #self.pyaudio_module = self.get_pyaudio()

        
        self.bg = ImageTk.PhotoImage(file="backvoice.jpg")
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover full frame

        # Load center image
        self.centre = ImageTk.PhotoImage(file="vs.webp")
        center_label = Label(self.root, image=self.centre)
        center_label.place(relx=0.5, rely=0.5, anchor=CENTER)  # Place in center
        center_label.config(width=170, height=170)  # Set width and height

        # Start button
        start = Button(self.root, text='START', font=("times new roman", 14), command=self.start_option)
        start.place(x=150, y=420)

        # Close button
        close = Button(self.root, text='CLOSE', font=("times new roman", 14), command=self.close_window)
        close.place(x=350, y=420)



        # Call the start method
        self.start()

    # Default Start
    def start(self):
        # Wish Start
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            wish = "Good Morning!"
        elif 12 <= hour < 18:
            wish = "Good Afternoon!"
        else:
            wish = "Good Evening!"
        self.speak('Hello Medhun sir, ' + wish + ' I am your voice assistant. Please tell me how may I help you')

    # Voice Control
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    # Take Command
    def take_command(self):
        try:
            with self.microphone as data_taker:
                print("Listening...")
                voice = self.listener.listen(data_taker)
                print("Recognizing...")
                instruction = self.listener.recognize_google(voice)
                instruction = instruction.lower()
                return instruction
        except Exception as e:
            print(e)
            return ''

    # Run command
    def run_command(self):
        instruction = self.take_command()
        print(instruction)
        try:
            if 'who are you' in instruction:
                self.speak('I am your personal voice Assistant, joro')
            elif 'what can you do for me' in instruction:
                self.speak('I can play songs, tell time, and help you go with wikipedia')
            elif 'current time' in instruction:
                time = datetime.datetime.now().strftime('%I: %M')
                self.speak('current time is ' + time)
            elif 'open google' in instruction:
                self.speak('Opening Google')
                webbrowser.open('https://www.google.com')
            elif 'open youtube' in instruction:
                self.speak('Opening Youtube')
                webbrowser.open('https://www.youtube.com')
            elif 'open facebook' in instruction:
                self.speak('Opening Facebook')
                webbrowser.open('https://www.facebook.com')
            elif 'open PythonGeeks' in instruction:
                self.speak('Opening PythonGeeks')
                webbrowser.open('https://www.pythongeeks.org')
            elif 'open linkedin' in instruction:
                self.speak('Opening Linkedin')
                webbrowser.open('https://www.linkedin.com')
            elif 'open gmail' in instruction:
                self.speak('Opening Gmail')
                webbrowser.open('https://mail.google.com')
            elif 'open stack overflow' in instruction:
                self.speak('Opening Stack Overflow')
                webbrowser.open('https://stackoverflow.com')
            elif 'shutdown' in instruction:
                self.speak('I am shutting down')
                self.close_window()
                return False
            else:
                self.speak('I did not understand, can you repeat again')
                return True
        except Exception as e:
            print(e)
            self.speak('Waiting for your response')
            return True

    # To run assistance continuously
    def start_option(self):
        while True:
            if self.run_command():
                self.run_command()
            else:
                break

    # Close window
    def close_window(self):
        self.root.destroy()

root = Tk()
obj = AssistanceGUI(root)
root.mainloop()
