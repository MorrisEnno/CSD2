import simpleaudio as sa
import time

#User inputs
bpm = 120
try:
   print("BPM = 120")
   bpm = int(input("To which value do you want to change the BPM?: "))
except: 
   print("BPM Set to Default")
else: 
   print(f"BPM set to {bpm}")   
    


numRepeats = int(input("How many times do you want to playback your rhythm?: "))

numNotes = int(input("How many notes should the rhythm contain?: "))

noteDurations = []
for i in range(numNotes):
    noteDuration = float(input(f"What should the note value be for note number {i + 1}?: "))
    noteDurations.append(noteDuration)


#Time calculations
quarternoteDuration = 60 / bpm
timeDurations = []
for noteDuration in noteDurations:
   timeDurations.append(noteDuration * quarternoteDuration)

timeStamps = []
totalDuration = 0

for duration in timeDurations:
    timeStamps.append(totalDuration)
    totalDuration = totalDuration + duration

print(timeStamps)

ts = timeStamps.pop(0)

startTime = time.time()


#playback
neuroCapture = sa.WaveObject.from_wave_file("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/NC.Neuro.capture.wav")
for _ in range(numRepeats): 
 while True:
   tCurrent = time.time() - startTime

   if tCurrent >= ts:
      play_obj = neuroCapture.play()
      if len(timeStamps) > 0:
          ts = timeStamps.pop(0)
      else:
        break
   time.sleep(0.001)   


time.sleep(timeDurations[-1])    

#for _ in range(numRepeats): 
   #for tDur in timeDurations: 
    # play_obj = neuroCapture.play()
     #time.sleep(tDur)
 
#play_obj.wait_done()