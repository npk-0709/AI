import speech_recognition as sr 
from gtts import gTTS
import playsound,time
import webbrowser as wb
class  __AI__:
    def __init__(self) -> None:
        pass
    def speak(text,lang):
        tss=gTTS(text=text,lang=lang)
        filename="C:/Users/Admin/Desktop/AI/audio.mp3"
        tss.save(filename)
        playsound.playsound(filename)
    def speak2(text,lang):
        tss=gTTS(text=text,lang=lang)
        filename="C:/Users/Admin/Desktop/AI/audio2.mp3"
        tss.save(filename)
        playsound.playsound(filename)
    def play_music(path):
        playsound.playsound(path)
    def listen():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio_data=r.record(source,duration=3)
            try:
                text=r.recognize_google(audio_data,language='vi')
            except:
                text='Vui Lòng Nói Lại'
            return text
    def listen_hey():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio_data=r.record(source,duration=1)
            try:
                text=r.recognize_google(audio_data,language='vi')
            except:
                text=''
            return text
    def xuly_text_yt(text):
        text=str(text)
        try:text=text.split('youtube')[1]
        except:text=text.replace('youtube','')
        return text
    def open_youtube(text):
        if text=="":
            wb.open('https://www.youtube.com')
        else:
            wb.open('https://www.youtube.com/results?search_query='+text)
    def open_facebook():
        wb.open('https://www.facebook.com')
    def open_translate():
        wb.open('https://translate.google.com')    
if __name__=='__main__':
    while True:
        text=__AI__.listen_hey().lower()
        if "hello" in text or "hey" in text:
            __AI__.speak('Vui Lòng Nói',lang='vi')
            text=__AI__.listen().lower()
            if text=='Vui Lòng Nói Lại':
                __AI__.speak(text)
            elif "facebook" in text:
                __AI__.speak2('đang mở facebook nè ',lang='vi')
                __AI__.open_facebook()
            elif "youtube" in text:
                __AI__.speak2('đang mở diu túp nè ',lang='vi')
                __AI__.open_youtube(__AI__.xuly_text_yt(text))
            elif "google translate" in text:
                __AI__.speak2('đang mở google dịch nè ',lang='vi')
                __AI__.open_translate()
            elif "music" in text:
                __AI__.speak2('Nhập link để hát',lang='vi')
                playsound.playsound(input('Nhập Link= '))
