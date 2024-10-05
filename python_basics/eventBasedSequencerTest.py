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
kick = pygame.mixer.Sound("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/Kick.wav")
snare = pygame.mixer.Sound("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/Snare.wav")
hiHat = pygame.mixer.Sound("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/HiHat.wav")
hallo = pygame.mixer.Sound("C:/Users/Morris/Desktop/AttractorSamples/CA.textureHit.wav")

#hallo.play()
print("Hallo!")


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



#Define note durs and offsets for different samples used
KickNoteDurs = [2.5, 1.5, 2.5, 1.5]
KickNoteOffset = 0

SnareNoteDurs = [2, 2, 2, 2]
SnareNoteOffset = 1

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

SnareNote16th = DursTo16ths(SnareNoteDurs)
SnareNoteOffset16th = OffsetTo16ths(SnareNoteOffset)

HiHatNote16th = DursTo16ths(HiHatNoteDurs)
HiHatNoteOffset16th = OffsetTo16ths(HiHatNoteOffset)


print("KickNote16th:", KickNote16th)
print("ClapNote16th:", SnareNote16th)
print("HiHatNote16th:", HiHatNote16th)


# Function to convert timestamps to time durations, back to timestamps
def ToTimestamp(timestamps, BPM, offset):
    QuarterNoteDur = 60 / BPM
    SixteenthNoteDur = QuarterNoteDur  / 4
    
    stamps = []
    for timestamp in timestamps:
      timeValue = (timestamp + offset) * SixteenthNoteDur
      stamps.append(timeValue)
      print("Time durations:", stamps)
    return stamps

kickTimestamps = ToTimestamp(KickNote16th, bpm, KickNoteOffset16th)
snareTimestamps = ToTimestamp(SnareNote16th, bpm, SnareNoteOffset16th)
hiHatTimestamps = ToTimestamp(HiHatNote16th, bpm, HiHatNoteOffset16th)
   
   #function that generates events from timestamplist, event name and instrument
def GenerateEvents(timestamps, eventName, instrument):
    events = []
    for timestamp in timestamps:
        event = {
            'timestamp': timestamp, 
            'name': eventName,
            'instrument': instrument
        }
        events.append(event)
    return events


def getTimestamp(event):
    return event['timestamp']   

kickEvents = GenerateEvents(kickTimestamps, 'kickEvent', kick)
snareEvents = GenerateEvents(snareTimestamps, 'snare', snare)
hiHatEvents = GenerateEvents(hiHatTimestamps, 'hiHat', hiHat)

events = kickEvents+snareEvents+hiHatEvents
events.sort(key=getTimestamp)

#eventHandler
def handleEvent(event):
    print(event['timestamp'])
    print(now-timeZero)
    event['instrument'].play()
    print(event['name'])
   
   
timeZero = time.time()

for repeat in range(numRepeats):
    print(f"Playback repeat {repeat + 1}/{numRepeats}")
     
      # Reinitialize the events list
    events = kickEvents + snareEvents + hiHatEvents
    events.sort(key=getTimestamp)

    timeZero = time.time()  # Reset timeZero for each repeat
  
    while events:
            now = time.time() - timeZero
            ts = events[0]['timestamp']  # Get the first timestamp

        # Check if it's time to play the sound
            if now >= ts:
                simultaneousEvents = []
            
                while events and events[0]['timestamp'] == ts:
                   simultaneousEvents.append(events.pop(0))
                for event in simultaneousEvents:
                       handleEvent(event)

            else:
             time.sleep(0.001)  # Small sleep to prevent CPU overuse

    # Wait for the final note to finish playing before moving to the next repeat
    time.sleep(0.1) # Add a small buffer to ensure sound finishes

  