import mp3play


def music():
    global clip
    clip = mp3play.load("\home\pi\Downloads\ultron-master\hello.mp3")

def playsong():
    global clip
    music()
    clip.play()
    print"Playing music"


def pausesong():
    global clip
    music()
    clip.pause()
    print "music is paused"

def unpausesong():
    global clip
    music()
    clip.unpause()
    print "music is unpaused"

def stopsong():
    global clip
    music()
    clip.stop()
    print "music is stopped"


