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



quarternoteDuration = 60 / bpm


#forLoop in list of noteDurations, userinput is asked for the notelength where 1 = quarternote.
try:
 noteDurationsInput = (input("Give a list of note values: "))
 noteDurations = [float(note.strip()) for note in noteDurationsInput.split(",")]   
  
 if len(noteDurations ==0):
    raise ValueError("Enter atleast one note value.")
except ValueError:
    print("invalid input setting note durations to 1.")
    noteDurations = [1.0]

#forLoop converts the given noteDurations to timeDurations.
timeDurations = [noteDuration * quarternoteDuration for noteDuration in noteDurations]   
print("timeDurations", timeDurations)



#Function to create timeStamps
def durationsToTimestamps16th(timeDurations):
   timeStampSeq = []
   sum = 0
   for duration in timeDurations:
         timeStampSeq.append(sum)
         sum += duration
 
   return timeStampSeq

#convert durations to timestamps
timeStampSeq = durationsToTimestamps16th(timeDurations)
print(f"timeStamps: {timeStampSeq}")


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
exit()