import subprocess
import time
p1state = True
state = True #loop state
verselocation= "/media/pi/Y9&10CITIPO/bible/"
songList = [verselocation +"song.mp3", verselocation + "The Book of Genesis.mp3", verselocation + "The Book of Exodus.mp3", verselocation + "The Book of Leviticus.mp3", verselocation + "The Book of Numbers.mp3"] #list of audio files you wish to use
totalTimeMin = [3.32, 781.75, 660, 478, 642] #final time of audio file eg 3min 30 sec = 3.50 

trackList = 1 #track song and Total Time Min list

audioFile = songList[trackList] #set first file

place2 = 45 #intro melody
place = 4428.0 #where to start in audio file *60 converts to min
increase = 23.5 # because this audio stops after 24 seconds a little overlap is made to allow full audio
p1 = None
p2 = None

while state == True:
    hour = time.localtime().tm_hour
    minu = time.localtime().tm_min
    
    totalTime = totalTimeMin[trackList] * 60 #convert totalTimeMin to seconds
    
    if hour == 6 and (minu >= 0 and minu <= 2):
        
        if p1state == True:
            p1 = subprocess.Popen(["mplayer", songList[0], "-ss", str(place2),"-softvol", "-volume", "10"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p1state = False
            if p2 != None:
                p2.kill() #ensure p2 sub is clear
        else:
            p2 = subprocess.Popen(["mplayer", songList[0], "-ss", str(place2), "-softvol", "-volume", "10"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p1state = True
            
            if p1 != None:
                p1.kill() #ensure p1 sub is clear       
        time.sleep(increase)

        place2 += increase-1
            
        #print(place2, totalTime) #Check Place of intro vid
        
        
        
        
        
        
    
    if hour == 6 and (minu >= 3 and minu <= 5):
        place2 = 45
        print("Au cycle.")
        if p1state == True:
            if trackList == 0:
                p1 = subprocess.Popen(["mplayer", audioFile, "-ss", str(place),"-softvol", "-volume", "10"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                p1 = subprocess.Popen(["mplayer", audioFile, "-ss", str(place),"-softvol", "-volume", "200"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            p1state = False
            if p2 != None:
                p2.kill() #ensure p2 sub is clear
        else:
            if trackList == 0:
                p2 = subprocess.Popen(["mplayer", audioFile, "-ss", str(place), "-softvol", "-volume", "10"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                p2 = subprocess.Popen(["mplayer", audioFile, "-ss", str(place), "-softvol", "-volume", "200"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p1state = True
            
            if p1 != None:
                p1.kill() #ensure p1 sub is clear
            
        
        time.sleep(increase)
        
        if trackList >= 1:
            place += increase+56
        else:
            place += increase-1
            
        print("Place:", place, "Total Place:",totalTime)
    
    
    
    
    if place >= totalTime+23:
        #state = False
        print("Finished")
        place = 0
        
        print("songList vs Track List", len(songList)-1, trackList)
        
        if (len(songList)-1) >= trackList:
            trackList += 1
            audioFile = songList[trackList]
        else:
            trackList = 1
            audioFile = songList[trackList]
