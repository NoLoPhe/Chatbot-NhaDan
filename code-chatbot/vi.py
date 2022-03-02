#!/usr/bin/python
# encoding=utf8

from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import os
import sys
import datetime
import time
import mymusic

sample_rate = 48000
chunk_size = 2048

reload(sys)

sys.setdefaultencoding('utf8')
translator = Translator()

localtime = time.asctime( time.localtime(time.time()) )

now = datetime.datetime.now()
hr=now.hour

if hr < 12:
    texta =u"Chào ngài buổi sáng, chúc ngài có một ngày làm việc tốt đẹp"
    print(texta)
    tts = gTTS(texta, lang='vi')
    tts.save("good.mp3")
    os.system("mpg321 -o alsa good.mp3")
    
elif hr >= 12 and hr < 17:
    textb =u"Chào ngài buổi chiều"
    print(textb)
    tts = gTTS(textb, lang='vi')
    tts.save("good.mp3")
    os.system("mpg321 -o alsa good.mp3")

elif hr >= 17 and hr <= 19:
    textc =u"Chào ngài buổi tối, chúc ngài có một buổi tối vui vẻ"
    print(textc)
    tts = gTTS(textc, lang='vi')
    tts.save("good.mp3")
    os.system("mpg321 -o alsa good.mp3")

    
while True:
# obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone( sample_rate = sample_rate, chunk_size = chunk_size) as source:
    #wait for a second to let the recognizer adjust the
    #energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

    try:
        nhandien1 = r.recognize_google(audio, language="vi-VN")
        print("Google Speech Recognition thinks you said " + nhandien1 )
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text2 = nhandien1.split()
        n = len(text2)
        i=0
        for i in range(i,n):
            if u"chào" in nhandien1 and text2[i]== u"Nguyễn" and text2[i+1]== u"Thành" and text2[i+2]== u"Tín":
                chao = u"chào ngài"
                print(chao)
                tts=gTTS(chao, lang='vi')
                tts.save("good.mp3")
                os.system("mpg321 -o alsa good.mp3")
                
            elif u"giờ" in nhandien1:
                    print(localtime +"\n")
                    tts=gTTS(localtime, lang='vi')
                    tts.save("good.mp3")
                    os.system("mpg321 -o alsa good.mp3")
                                 
            elif u"mẹ" in nhandien1:
                text3 = u"Chào mẹ, con yêu mẹ nhiều lắm!"
                print(text3)
                tts=gTTS(text3, lang='vi')
                tts.save("good.mp3")
                os.system("mpg321 -o alsa good.mp3")
                
            elif u"phát nhạc" in nhandien1:
                text4 = u"song is play!"
                print(text4)
                os.system("mpg321 -o alsa nl.mp3")
            
            elif u"play" in nhandien1:
                print("yes sir")
                mymusic.playsong()
                
            elif u"pause" in nhandien1:
                print("pausing the song")
                mymusic.pausesong()
                
            elif u"unpause" in nhandien1:
                print("resuming the song")
                mymusic.unpausesong()
                
            elif u"stop" in nhandien1:
                print("as you say")
                mymusic.stopsong()
                           
                
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

        
        
    '''    voice = r.recognize_google(audio, language='ko-KR')
        voicejp = translator.translate(voice,dest='ja')
        voicezh = translator.translate(voice,dest='zh-cn')
        voiceen = translator.translate(voice,dest='en')
        print voicezh
        
        tts=gTTS(text=str(voicezh.text),lang='zh-cn')
        tts.save("good.mp3")
        os.system("mpg321 -o alsa good.mp3")
        print voicejp
        tts=gTTS(text='일본어로',lang='ko')
        tts.save("good.mp3")
        os.system("mpg321 -o alsa good.mp3")
        tts=gTTS(text=str(voicejp.text),lang='ja')
        tts.save("good.mp3")
        os.system("mpg321 -o alsa good.mp3")
        print voiceen
        tts=gTTS(text='영어로',lang='ko')
        tts.save("good.mp3")
        os.system("mpg321 -o alsa good.mp3")
        tts=gTTS(text=str(voiceen.text),lang='en')
        tts.save("good.mp3")
        os.system("mpg321 -o alsa good.mp3")  '''
    