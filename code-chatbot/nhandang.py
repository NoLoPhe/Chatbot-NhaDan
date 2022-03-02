#!/uspeech_recognition/bin/python
# encoding=utf8

from googletrans import Translator
import speech_recognition 
from gtts import gTTS
import os
import sys
import pyttsx
import time
import datetime
import gsearch
import mywiki
import myweather
import sqlite3

conn = sqlite3.connect('dataspeech.sqlite')
c = conn.cursor()

sample_rate = 48000
chunk_size = 2048

reload(sys)

sys.setdefaultencoding('utf8')
translator = Translator()

speech_identifier = speech_recognition.Recognizer()

def say(text):
    print(text)
    tts = gTTS(text, lang='vi')
    tts.save("good.mp3")
    os.system("mpg321 -o alsa good.mp3")

def sayen(text):
    print(text)
    tts = gTTS(text, lang='en')
    tts.save("good.mp3")
    os.system("mpg321 -o alsa good.mp3")

def phrase():

        with speech_recognition.Microphone(sample_rate = sample_rate,
                        chunk_size = chunk_size) as source:
                speech_identifier.adjust_for_ambient_noise(source)
                audio = speech_identifier.listen(source)
                
        try:
                return speech_identifier.recognize_google(audio, language="vi-VN")

        except speech_recognition.UnknownValueError:
                print("I'm waiting for your command")


        return ""

localtime = time.asctime( time.localtime(time.time()) )

now = datetime.datetime.now()
hr=now.hour

guest = "say hello to "
google = "Google about "
search = u"Tìm kiếm "
wiki = "Wiki about "
wiki1 = u"nói cho anh nghe về "
wiki2 = "who is "
wiki3 = "what is an "
wiki4 = "what is a "
weather = u"nói cho anh nghe thời tiết "
status = "how is the weather in "
temp = "what is the temperature in "
wspeed = "what is the wind speed in "
humidity = "what is the humidity in "
pressure = "how much is the weather pressure in "
trantv= u"dịch cho anh câu "
# Bây giờ là mấy giờ
# bài hát
'''
if hr < 12:
    text =u"Chào ngài buổi sáng, chúc ngài có một ngày làm việc tốt đẹp"
    say(text)
    
elif hr >= 12 and hr < 17:
    text =u"Chào ngài buổi chiều"
    say(text)
    
elif hr >= 17 and hr <= 23:
    text =u"Chào ngài buổi tối, chúc ngài có một buổi tối vui vẻ"
    say(text)
   '''

while 1:

        stra=phrase()

        #say(stra)
        print (stra)
        
        if u"tên gì" in stra :
                text = u"Nhỏ tên Nhã Đan. Anh là người lập trình ra nhỏ hả"
                say(text)
    

        elif u"mục đích" in stra :
                text = u"là để nói chuyện như một người bạn."
                say(text)
    

        elif u"làm được những gì" in stra or u"làm những gì" in stra:
                text = u"Nhỏ có thể nói giờ, thời tiết và tìm kiếm thông tin, anh dạy cho nhỏ thêm nhiều nữa nhé"
                say(text)
    

        elif "tốt" in stra or u"công việc" in stra:
                text = "Nhỏ nghĩ nhỏ sẽ làm tốt nếu như phần lập trình không có vấn đề gì"
                say(text)
        
        elif u"hỏi" in stra:
            text = u"Vâng, anh hỏi đi"
            say(text)
                

        elif stra == "Bây giờ là mấy giờ" or stra == "Mấy giờ rồi" or stra == "what's the time" or stra == "time" or stra == "what is today" or stra == "what's today" :
                print(localtime +"\n")
                tts = gTTS(localtime , lang='vi')
                tts.save("good.mp3")
                os.system("mpg321 -o alsa good.mp3")
    
                
        elif "hẹn gặp lại" in stra or "tạm biệt" in stra:
                text = "ahihi, Bye anh"
                say(text)

        elif stra == "bye" or stra == "buy" or stra == "break" or stra == "bye Ultron" or stra == "buy Ultron" or stra == "brake" or stra == "terminate":
                if hr >= 20 and hr <=24:
                    print("Good night sir\n")
                    say("Good night sir")
                else:
                    print("see you again sir\n")
                    say("see you again sir")
                break

        elif stra == "how are you":
                print("I'm good sir. How are you?\n")
                say("I'm good sir. How are you?")

        elif stra == "great" or stra == "nice" or stra == "fine" or stra == "good" or stra == "ok" or stra == "okay" or stra == "alright" or stra == "cool":
                print("sir\n")
                say("sir")

        elif stra == guest+stra[13:] :  #say hello to ------
                print("hello "+stra[13:] +"\n")
                say("hello "+stra[13:])

        elif stra == google+stra[13:] :
            say("here we go")
            gsearch.search(stra[13:])

        elif stra == search+stra[9:] :
            say("I'm on it sir")
            gsearch.search(stra[9:])

        
        elif stra == wiki+stra[11:] :
            say("Vâng")
            data = mywiki.wiki(stra[11:])
            print (data+"\n")
            #time.sleep(5)
            say(data)

        elif stra == wiki1+stra[20:] :
            say(u"Vâng")
            data = mywiki.wiki(stra[20:])
            #time.sleep(5)
            print (data+"\n")
            say(data)
                    

        elif stra == weather+stra[27:] :
            thoitiet = stra[26:]
            if u"Hà Nội" in thoitiet :
                thoitiet = "Hanoi"
            if u"Đà Nẵng" in thoitiet :
                thoitiet = "Danang"
            if u"Hồ Chí Minh" in thoitiet :
                thoitiet = "Thanh pho Ho Chi Minh"
            say(u"Vâng")
            report = myweather.completeWeather(thoitiet)
            print(report+"\n")
            say(report)
            # http://openweathermap.org/help/city_list.txt

        elif stra == status+stra[22:] :
            status = myweather.statusWeather(stra[22:])
            print(status+"\n")
            say(status)

        elif stra == temp+stra[27:] :
            temp = myweather.tempWeather(stra[27:])
            print(temp+"\n")
            say(temp)

        elif stra == wspeed+stra[26:]:
            wspeed = myweather.wspeedWeather(stra[26:])
            print(wspeed+"\n")
            say(wspeed)

        elif stra == humidity+stra[24:]:
            humdty = myweather.humidityWeather(stra[24:])
            print(humdty+"\n")
            say(humdty)

        elif stra == pressure+stra[36:] :
            press = myweather.pressureWeather(stra[36:])
            print(press+"\n")
            say(press)
        
        elif u"bài hát" in stra:
            text = u"Vâng"
            say(text)
            os.system("mpg321 -o alsa nl.mp3")
            
               
        elif stra == trantv+stra[17:] :
            voice = stra[16:]
            voicejp = translator.translate(voice,dest='ja')
            voicezh = translator.translate(voice,dest='zh-cn')
            voiceen = translator.translate(voice,dest='en')
            print voicezh
            tts=gTTS(text=u'Tiếng Trung Quốc',lang='vi')
            tts.save("good.mp3")
            os.system("mpg321 -o alsa good.mp3")
            tts=gTTS(text=str(voicezh.text),lang='zh-cn')
            tts.save("good.mp3")
            os.system("mpg321 -o alsa good.mp3")
            print voicejp
            tts=gTTS(text=u'Tiếng Nhật',lang='vi')
            tts.save("good.mp3")
            os.system("mpg321 -o alsa good.mp3")
            tts=gTTS(text=str(voicejp.text),lang='ja')
            tts.save("good.mp3")
            os.system("mpg321 -o alsa good.mp3")
            print voiceen
            tts=gTTS(text=u'Tiếng Anh',lang='vi')
            tts.save("good.mp3")
            os.system("mpg321 -o alsa good.mp3")
            tts=gTTS(text=str(voiceen.text),lang='en')
            tts.save("good.mp3")
            os.system("mpg321 -o alsa good.mp3")
            
        elif u"kịch bản" in stra:
            #ai soạn kịch bản cho anh và nhỏ nói chuyện
            c.execute("SELECT cauhoi FROM hoi")# WHERE cauhoi = ?",[stra])
            data = c.fetchall()
            if stra in [i[0] for i in data]:
                c.execute("SELECT ma FROM hoi WHERE cauhoi = ?",[stra])
                dataa = c.fetchall()
                for j in dataa:
                    straa = j[0]
                
                c.execute("SELECT name FROM traloi WHERE ma = ?",[straa])
                datab = c.fetchall()
                for k in datab:
                    strab = k[0]
                print(strab)
                say(strab)
            
            else:
                c.execute("INSERT INTO hoi(cauhoi,ma) VALUES (?,'kxd')",[stra])
                conn.commit()
                print("Nhỏ không biết câu trả lời, dạy nhỏ đi ")
                say("Nhỏ không biết câu trả lời, dạy nhỏ đi ")
                r1 = speech_recognition.Recognizer()
                with speech_recognition.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source1:
                    r1.adjust_for_ambient_noise(source1)
                    audio1 = r1.listen(source1)
                    print ('Done!')
                    stra1 = r1.recognize_google(audio1,language ="vi-VN")
                    print("Toi nghi rang ban da noi: " + stra1)
                    c.execute("INSERT INTO traloi(name,ma) VALUES (?,'kxd')",[stra1])
                    conn.commit()

                            

  

        

