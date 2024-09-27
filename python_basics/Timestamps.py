import pygame
import time
pygame.init()
hallo = pygame.mixer.Sound("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/Hi.Hat.wav")

hallo.play()


#User inputs
bpm = 120
try:
   print("BPM = 120")
   bpm = int(input("To which value do you want to change the BPM?: "))
  
except: 
   print("BPM Set to Default")
else: 
   print(f"BPM set to {bpm}")   
    

try:
  numRepeats = int(input("How many times do you want to playback your rhythm?: "))
except ValueError:
  print("Invalid input. Setting numRepeats to 1.")
  numRepeats = 1


try:
   numNotes = int(input("How many notes should the rhythm contain?: "))
except ValueError:
   print("Invadlid input. Setting numNotes to 3.")
   numNotes = 1

quarternoteDuration = 60 / bpm


#forLoop in list of noteDurations, userinput is asked for the notelength where 1 = quarternote.
noteDurations = []
for i in range(numNotes):
    try:
        noteDuration = float(input(f"What should the note value be for note number {i + 1}?: "))
        noteDurations.append(noteDuration)
    except ValueError:
        print(f"Invalid input for note {i + 1}. Setting note duration to 1.")
        noteDurations.append(1.0)


#forLoop in list of timeDurations converts the given noteDurations to timeDurations.
timeDurations = []
for noteDuration in noteDurations:
     timeDurations.append(noteDuration * quarternoteDuration)
     print("timeDurations", timeDurations)

#Function to create timeStamps
def durationsToTimestamps16th(timeDurations):
   timeStampSeq = []
   sum = 0
   for duration in timeDurations:
         timeStampSeq.append(sum)
         sum += duration
   print(f"timeStamps: {timeStampSeq}")
   return timeStampSeq

   
timeStampSeq = durationsToTimestamps16th(timeDurations)
#ts = timeStamps.pop(0)

#startTime = time.time()


#playback
hiHat = pygame.mixer.Sound("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/Hi.Hat.wav")


for _ in range(numRepeats):
    timeZero = time.time()  # Reference start time
    timeStamps = timeStampSeq.copy()  # Reset timestamp list for each repeat

    while timeStamps:
        now = time.time() - timeZero
        ts = timeStamps[0]  # Get the first timestamp

        # Check if it's time to play the sound
        if now >= ts:
            hiHat.play()
            timeStamps.pop(0)  # Remove the played timestamp

        time.sleep(0.001)  # Small sleep to prevent CPU overuse

    # Wait for the final note to finish before moving to the next repeat
    time.sleep(timeDurations[-1])

# Exit the program
