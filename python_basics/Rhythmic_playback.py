import simpleaudio as sa
import time


#Asks to input note repeats
try:
 repeats = int(input("How many times would you like the sound to be repeated?"))
except ValueError:
 print("Invalid input. Please enter a number.")
 repeats = 1

noteAmt = int(input("How many notes should the rhythm contain?"))
#Empty rhythm list
rhythm = []

#Asks to input note values
for i in range(noteAmt):
  noteLength = float(input("Note value?"))
  rhythm.append(noteLength)


bpmToMs = 60000 / int(input("What's the bpm?"))


#wav file gets loaded.
neuroCapture= sa.WaveObject.from_wave_file("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/NC.Neuro.capture.wav")
for _ in range(repeats): 
   for delay in rhythm: 
     play_obj = neuroCapture.play()
     time.sleep(delay * (bpmToMs / 1000))
 
play_obj.wait_done()






#User input gets converted to an integer.
#try:
 #numPlaybackTimes = int(input("How many times would you like the sound to be repeated?"))
#except ValueError:
 #print("Invalid input. Please enter a number.")
#bpm = int(input("What's the bpm?"))
#noteValue = 60000 / bpm * float(input("What shall the note values be?"))




