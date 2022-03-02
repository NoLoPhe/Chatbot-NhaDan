#!/usr/bin/python
# encoding=utf8

from googletrans import Translator
import speech_recognition
from gtts import gTTS
import sys
import pyttsx
import time
import datetime
import gsearch
import mywiki
import myweather
import paho.mqtt.client as mqtt
import os, urlparse
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

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
    
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/Temp/Two")
    client.subscribe("/Temp/Three")

def on_message(client, userdata, msg):
    if(str(msg.topic) == "/Temp/Two"):
        a1 = str(msg.payload)
        text = u"nhiệt độ"+a1+ u"độ C"
        say(text)
    elif(str(msg.topic) == "/Temp/Three"):
        a2 = str(msg.payload)
        text = u"độ ẩm" + a2 + u"%"
        say(text)
        client.disconnect()
    
def on_disconnect(self):
        return self._on_disconnect
    
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
trantv= u"dịch cho anh câu"
# Bây giờ là mấy giờ
# bài hát

if hr < 12:
    text =u"Chào ngài buổi sáng, chúc ngài có một ngày làm việc tốt đẹp"
    say(text)
    
elif hr >= 12 and hr < 17:
    text =u"Chào ngài buổi chiều"
    say(text)
    
elif hr >= 17 and hr <= 23:
    text =u"Chào ngài buổi tối, chúc ngài có một buổi tối vui vẻ"
    say(text)
   

while 1:
    #time.sleep(2)
    #if GPIO.input(23):
        
        #text =u"chào bạn, tôi có thể giúp gì cho bạn"
        #say(text)
        a= 1
        
        while a:

            stra=phrase()
            print (stra)

            #say(stra)
        
        
            if u"tên gì" in stra :
                text = u"Nhỏ tên Nhã Đan. Anh là người lập trình ra nhỏ hả"
                say(text)
    

            elif u"mục đích" in stra :
                text = u"là để nói chuyện như một người bạn."
                say(text)
    

            elif u"làm được những gì" in stra or u"làm được gì" in stra:
                text = u"Nhỏ có thể nói giờ, thời tiết và tìm kiếm thông tin, anh dạy cho nhỏ thêm nhiều nữa nhé"
                say(text)
    

            elif u"tốt" in stra or u"công việc" in stra:
                text = "Nhỏ nghĩ nhỏ sẽ làm tốt nếu như phần lập trình không có vấn đề gì"
                say(text)
        
            elif u"Ăn gì" in stra or u"ăn gì" in stra:
                text = "Anh thích ăn gì? Nhỏ thì mì quảng là nhất"
                say(text)
        
            elif u"Sách gì hay" in stra or u"sách gì hay" in stra:
                text = "Có rất nhiều sách hay anh có thể đọc đấy. Nhỏ thì thích văn học Việt Nam trung đại lắm"
                say(text)
                
            elif u"Buồn quá" in stra or u"buồn quá" in stra:
                text = "chuẩn bị có Deadpool 2 ngoài rạp. Anh đi coi với nhỏ chứ?"
                say(text)
                
            elif "Nóng quá" in stra or u"nóng quá" in stra:
                text = "còn nhỏ thì mát lắm"
                say(text)
                
            elif u"tuổi" in stra or u"bao nhiêu tuổi" in stra:
                text = "nhỏ mới 3 tháng tuổi"
                say(text)
                
            elif u"ở đâu" in stra :
                text = "còn nhỏ thì mát lắm"
                say(text)
                
            elif stra == u"Bây giờ là mấy giờ" or stra == u"Mấy giờ rồi" or stra == u"what's the time" or stra == "time" or stra == "what is today" or stra == "what's today" :
                print(localtime +"\n")
                tts = gTTS(localtime , lang='vi')
                tts.save("good.mp3")
                os.system("mpg321 -o alsa good.mp3")
    
                
            elif "hẹn gặp lại" in stra or u"cám ơn" in stra or "thank you" in stra or u"Hẹn gặp lại" in stra or "Thank you" in stra:
                text = u"Bye anh"
                say(text)
                time.sleep(5)
                a = 0

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
                say(u"Vâng")
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
            
            elif stra == trantv+stra[16:] :
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
        
            elif u"nhiệt độ" in stra:
                client = mqtt.Client()
                client.on_connect = on_connect
                client.username_pw_set("ooynwevt", "c4r32V5VJQ9J")
                client.connect('m11.cloudmqtt.com', 17816, 60)
                client.on_message = on_message
                client.loop_forever()
        
            elif u"bật đèn" in stra:
                client = mqtt.Client()
                client.on_connect = on_connect
                client.username_pw_set("ooynwevt", "c4r32V5VJQ9J")
                client.connect('m11.cloudmqtt.com', 17816, 60)
                client.publish("/Light/Two", "0")
            
            elif u"Tắt Đèn" in stra:
                client = mqtt.Client()
                client.on_connect = on_connect
                client.username_pw_set("ooynwevt", "c4r32V5VJQ9J")
                client.connect('m11.cloudmqtt.com', 17816, 60)
                client.publish("/Light/Two", "1")
            
            

  

        
