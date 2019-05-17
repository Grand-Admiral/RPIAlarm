import subprocess
import time
p1state = True
state = True #loop state
songList = ["song.mp3"] #list of audio files you wish to use
audioFile = songList[0] #set first file

place = 0 #where to start in audio file
increase = 23.7 # because this audio stops after 24 seconds a little overlap is made to allow full audio

totalTimeMin = [3.32] #final time of audio file eg 3min 30 sec = 3.30
totalTime = totalTimeMin[0] * 60 #convert totalTimeMin to seconds
p1 = None
p2 = None

while state == True:
    hour = time.localtime().tm_hour
    minu = time.localtime().tm_min
    #sec = time.localtime().tm_sec
    
    if hour == 6 and (minu >= 0 and minu <= 3):
        print("Print in cycle.")
        if p1state == True:
            if p1 != None:
                p1.kill() #ensure p1 sub is clear
            p1 = subprocess.Popen(["mplayer", audioFile, "-ss", str(place)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p1state = False
        else:
            if p2 != None:
                p2.kill() #ensure p2 sub is clear
            p2 = subprocess.Popen(["mplayer", audioFile, "-ss", str(place)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p1state = True
            
        time.sleep(increase)
        place += increase
        
    if place >= totalTime:
        #state = False
        print("Finished")
        place = 0
        audioFile = songList[0]
        
