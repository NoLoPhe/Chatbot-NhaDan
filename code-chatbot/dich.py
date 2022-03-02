#!/usr/bin/python
# encoding=utf8

from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import os
import sys

sample_rate = 48000
chunk_size = 2048

reload(sys)

sys.setdefaultencoding('utf8')
translator = Translator()

while True:
# obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone( sample_rate = sample_rate,
                        chunk_size = chunk_size) as source:
    #wait for a second to let the recognizer adjust the
    #energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio,language="vi-VN"))
        voice = r.recognize_google(audio, language='vi-VN')
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
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))