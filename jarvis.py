import os
import platform
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import pywhatkit
import openai
import smtplib
from dotenv import load_dotenv

load_dotenv()
engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')
engine.setProperty('volume', 1.0)
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello! I'm Jarvis here. How can I assist you today?")

def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    r.pause_threshold = 1.5
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(os.getenv("YOUR_EMAIL"), os.getenv("YOUR_PASSWORD"))
    server.sendmail(os.getenv("YOUR_EMAIL"), to, content)
    server.close()

def browserOpen(url):
    webbrowser.open(url)

def search_file(filename, root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if filename.lower() in file.lower():
                return os.path.join(root, file)
    return None

def callGPT(question):
    openai.api_key = os.getenv("OPENAI_KEY")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )

    response = completion.choices[0].message['content']
    speak(response)

if __name__ == "__main__":
    wishMe()

    # Detect the operating system
    if platform.system() == "Windows":
        root_dirs = ['C:\\', 'D:\\']
    elif platform.system() == "Darwin":
        root_dirs = ['/']
    else:
        print("Unsupported operating system.")
        exit()

    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except Exception as e:
                print(e)
                speak("Unable to search please say again")
        elif 'hi' in query:
            speak("Hii Boss")
        elif 'jarvis' in query:
            speak("yes boss")
        elif 'thank you' in query:
            speak("You are Welcome ")
        elif 'open youtube' in query:
            bName = ""
            url = 'https://youtube.com'
            browserOpen(bName, url)
        elif 'open google' in query:
            bName = ""
            url = 'https://google.com'
            browserOpen(bName, url)
        elif 'open drive' in query:
            bName = ""
            url = 'https://drive.google.com'
            browserOpen(bName, url)
        elif 'open whatsapp' in query:
            """ bName=""
            url = 'https://web.whatsapp.com'
            browserOpen(bName,url) """
            pywhatkit.sendwhatmsg("+918637258307",
                                  "Geeks For Geeks!",
                                  18, 30)
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")
        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)
        elif 'send mail to sam' in query:
            try:
                speak("What's the message??")
                content = takeCommand()
                to = "rinkandas2@gmail.com"
                sendEmail(to, content)
                speak('mail sent')
            except Exception as e:
                print(e)
        elif 'search' in query:
            try:
                speak("File Name Sir")
                fname = takeCommand().lower()

                for fpath in root_dirs:
                    try:
                        file_path = search_file(fname, fpath)
                        if file_path:
                            speak(f"Found file at: {file_path}")
                            print(f"Found file at: {file_path}")
                        else:
                            speak("File not found")
                            print("File not found")
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
        elif 'stop jarvis' in query:
            speak('Ok Boss')
            exit()
        else: 
            speak
            #callGPT(query)