##TO DO:
##EVENT HANDLER FUNCTION 
##THINK ABOUT RANDOM
#1ST ORDER MARKOV CHAIN
# EUCLIDEAN RHYTHM
#MIDPOINT DISPLACEMENT ALGORHYTHM
#FIBONACCI EXPONENTIAL RHYTHM GENERATION
#for i in range(num_iterations):
#   num_splits = 2 ^ i
#   for j in range(num_splits):
#      index = j * 2
#      print(index)
#split_amount = random.choice([o.5, 0.25, 0,125])
#note = notes[index]
#dur = note["qnote_dur"]       
#new_dur = dur * split_amount
#rest_dur = dur - new_dur

#note["qnote_dur"] = new_dur


import pygame
import time
pygame.init()
Kick = pygame.mixer.Sound("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/Kick.wav")
Snare = pygame.mixer.Sound("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/Snare.wav")
HiHat = pygame.mixer.Sound("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/HiHat.wav")
hallo = pygame.mixer.Sound("C:/Users/Morris/Desktop/AttractorSamples/CA.textureHit.wav")

hallo.play()
print("Hallo!")


#User inputs
bpm = 120
numRepeats = 1

#Define note durs and offsets for different samples used
KickNoteDurs = [1, 1, 1, 1, 1, 1, 1, 1]
KickNoteOffset = [0]

ClapNoteDurs = [2, 2, 2, 2]
ClapNoteOffset = 1

HiHatNoteDurs = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
HiHatNoteOffset = 0

#convert durs to 16th timestamps
def DursTo16ths(noteDurations):
    sixteenths = []
    CurrentTimestamp = 0
    for duration in noteDurations:
        sixteenths.append(CurrentTimestamp)
        CurrentTimestamp += duration * 4
    return sixteenths

def OffsetTo16ths(offset):
    return offset * 4

KickNote16th = DursTo16ths(KickNoteDurs)
KickNoteOffset16th = OffsetTo16ths(KickNoteOffset)

ClapNote16th = DursTo16ths(ClapNoteDurs)
ClapNoteOffset16th = OffsetTo16ths(ClapNoteOffset)

HiHatNote16th = DursTo16ths(HiHatNoteDurs)
HiHatNoteOffset16th = OffsetTo16ths(HiHatNoteOffset)


print("KickNote16th:", KickNote16th)
print("ClapNote16th:", ClapNote16th)
print("HiHatNote16th:", HiHatNote16th)


# Function to convert timestamps to time durations (in seconds)
def ToTimeDur(timestamps, BPM, offset):
    QuarterNoteDur = 60 / BPM
    SixteenthNoteDur = QuarterNoteDur  / 4
    
    stamps = []
    for timestamp in timestamps:
      timeValue = (timestamp + offset) * SixteenthNoteDur
      stamps.append(timeValue)
      print("Time durations:", stamps)
    return stamps
   


#playback
textureHit = pygame.mixer.Sound("C:/Users/Morris/Desktop/AttractorSamples/CA.textureHit.wav")
textureHitRev = pygame.mixer.Sound("C:/Users/Morris/Desktop/AttractorSamples/CA.textureHitRev.wav")
perc1 = pygame.mixer.Sound("C:/Users/Morris/Desktop/AttractorSamples/CA.perc1.wav")

""""
for repeat in range(numRepeats):
    print(f"Playback repeat {repeat + 1}/{numRepeats}")
    timeZero = time.time()  # Reference start time
    timeStamps = timeStampSeq.copy()  # Reset timestamp list for each repeat

    # Loop through each timestamp and play the sound
    while timeStamps:
        now = time.time() - timeZero
        ts = timeStamps[0]  # Get the first timestamp

        # Check if it's time to play the sound
        if now >= ts:
            perc1.play()
            timeStamps.pop(0)  # Remove the played timestamp

        time.sleep(0.001)  # Small sleep to prevent CPU overuse

    # Wait for the final note to finish playing before moving to the next repeat
    time.sleep(timeDurations[-1] + 0.1)  # Add a small buffer to ensure sound finishes
    """