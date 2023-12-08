import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')                        
# SAPI5 also known as Microsoft Speech API is the technology for voice recognition and synthesis provided by Microsoft.
# It can be used to convert Text into Speech.

voices = engine.getProperty('voices')
print(voices)

# print(voices[0].id)         --> It will show voice of DAVID

engine.setProperty('voice', voices[1].id)
# To set the voice

def speak(audio):                        # It is given audio argument to fetch whatever the audio is given by user.
    engine.say(audio)                    # Engine will say whatever is present in audio string.
    engine.runAndWait()                  # This function runs the voice assistant to speak.

def wishMe():
    hour = int(datetime.datetime.now().hour)      # hour variable get the value of hour in int from 0 to 24.
    if hour >=0 and hour < 12 :                         # speak() function is used to pass the message to speak.
        speak("Good Morning Pratham!")

    elif hour >=12 and hour < 18 :
        speak("Good Afternoon Pratham!")

    else:
        speak("Good Evening Pratham!")

    speak("I am here, please tell me how may I help you...")
    
def takeCommand():
    # Initialize the Recognizer
    r = sr.Recognizer()
    
    # Use the microphone as a source
    with sr.Microphone() as source:
        print("Speak:")
        #r.pause_threshold = 2  # Increase the pause threshold to 2 seconds, for example.
        
        # Listen to the audio from the microphone
        audio = r.listen(source)
    
    # Try to use Google's Speech Recognition API to convert audio to text,
    # catch and report errors if any
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said:", query)
        
    except Exception as e:
        print("Say that again please...")
        return 'None'
    
    return query

if __name__=="__main__":        #__ is used when we have to perform that task on GPU.
    wishMe()
    if 1:
        query = takeCommand().lower()
    
        # Logic for executing tasks based on queries
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            
        elif 'open google' in query:
            webbrowser.open('google.com')
            
        elif 'open my website' in query:
            webbrowser.open('https://prathameshdalviportfolio18.on.drv.tw/www.myportfolio.cf/website2.html')
            
        elif 'play music' in query or 'play song' in query:
            music_dir = "C:\\Users\\Dell\\Music"
            webbrowser.open(music_dir)
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'bye jarvis' in query:
            exit()
    
    