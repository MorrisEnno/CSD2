import pygame
import time
import os
from midiutil import MIDIFile

# Initialize Pygame
pygame.init()

# PROMPT
# I have added folders in my directory, LOW, MID, and HIGH. 
# I want the generator to use the samples in the folders, where the low folder replaces the kick, 
# MID folder replaces snare, high folder replaces hi hat. 
# The folders are located within the CSD2/CSD2/ directory. 
# If I have for example 8 LOW notes, while the folder LOW contains two samples, 
# it will scroll through that list of samples.

def loadSamplesFromFolder(folderPath):
    samples = []
   
    for fileName in os.listdir(folderPath):
        if fileName.endswith(".wav"):  
            filePath = os.path.join(folderPath, fileName)
            samples.append(pygame.mixer.Sound(filePath))  


lowSamples = loadSamplesFromFolder("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/LOW")
midSamples = loadSamplesFromFolder("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/MID")
highSamples = loadSamplesFromFolder("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/HIGH")


if not lowSamples or not midSamples or not highSamples:
    raise Exception("One or more folders are empty. Please ensure LOW, MID, and HIGH folders contain samples.")


def getIntegerInput(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:  # Ensure positive integer
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:  # Ensure positive number
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive number.")

def getStringInput(prompt):
    while True:
        value = input(prompt).strip()
        if value:  # Ensure input is not empty
            return value
        else:
            print("Input cannot be empty. Please enter a valid string.")


numNotesLow = getIntegerInput("How many notes for the LOW rhythm?: ")
numNotesMid = getIntegerInput("How many notes for the MID rhythm?: ")
numNotesHigh = getIntegerInput("How many notes for the HIGH rhythm?: ")
bpm = getFloatInput("Enter the BPM (Beats Per Minute): ")
measures = getIntegerInput("How many measures should the rhythm last?: ")
growthFactorLow = getFloatInput("Enter the growth factor for the LOW rhythm (less than 1 for acceleration, greater than 1 for deceleration): ")
growthFactorMid = getFloatInput("Enter the growth factor for the MID rhythm (less than 1 for acceleration, greater than 1 for deceleration): ")
growthFactorHigh = getFloatInput("Enter the growth factor for the HIGH rhythm (less than 1 for acceleration, greater than 1 for deceleration): ")
numLoops = getIntegerInput("How many times should the rhythm loop?: ")

# PROMPT
# can you help me create a version of my python code that incorporates 
# the mathematical and logical functions of the supercollider code that I sent you? 
# it's close to what I envisioned, 
# but not quite. 
# Lets take it back a few steps, 
# starting with just one instrument, only the kick. 
# I want to be able to input the amount of kicks, 
# and I want the growthfactor to be dependent on the amount of kicks, 
# so that the acceleration/deceleration fits exactly within the measures of the full rhythm.

def generateTimestamps(numNotes, totalTime, growthFactor):
    timestamps = []
    currentTime = 0
    # Calculate the starting duration for the first note
    startDuration = totalTime * (growthFactor - 1) / (growthFactor**numNotes - 1)

    for i in range(numNotes):
        timestamps.append(currentTime)  
        currentTime += startDuration  
        startDuration *= growthFactor  # Scale the duration by the growth factor for each note
    
    return timestamps


def exportToMidi(lowTimestamps, midTimestamps, highTimestamps, bpm, fileName):
    midiFile = MIDIFile(1) 
    track = 0
    time = 0
    midiFile.addTrackName(track, time, "Polyrhythm Track")  
    midiFile.addTempo(track, time, bpm)  
    
    channel = 9 
    lowNote = 36  
    midNote = 38 
    highNote = 42 
    velocity = 100  

   
    for timestamp in lowTimestamps:
        noteTime = timestamp / (60 / bpm)  
        duration = 0.25  
        midiFile.addNote(track, channel, lowNote, noteTime, duration, velocity)
    
    
    for timestamp in midTimestamps:
        noteTime = timestamp / (60 / bpm)  
        duration = 0.25
        midiFile.addNote(track, channel, midNote, noteTime, duration, velocity)

    
    for timestamp in highTimestamps:
        noteTime = timestamp / (60 / bpm)  
        duration = 0.25
        midiFile.addNote(track, channel, highNote, noteTime, duration, velocity)

    filePath = f"C:/Users/Morris/Desktop/{fileName}.midi"  
    with open(filePath, 'wb') as outf:
        midiFile.writeFile(outf)  
    
    print(f"MIDI file '{filePath}' created successfully!")


totalTime = (60 / bpm) * 4 * measures


lowTimestamps = generateTimestamps(numNotesLow, totalTime, growthFactorLow)
midTimestamps = generateTimestamps(numNotesMid, totalTime, growthFactorMid)
highTimestamps = generateTimestamps(numNotesHigh, totalTime, growthFactorHigh)


print("Low Timestamps:", lowTimestamps)
print("Mid Timestamps:", midTimestamps)
print("High Timestamps:", highTimestamps)

# 
def getSample(samples, index):
    return samples[index % len(samples)]

# Combine all sets of timestamps for playback and sort them
combinedTimestamps = [(timestamp, 'low', i) for i, timestamp in enumerate(lowTimestamps)] + \
                     [(timestamp, 'mid', i) for i, timestamp in enumerate(midTimestamps)] + \
                     [(timestamp, 'high', i) for i, timestamp in enumerate(highTimestamps)]
combinedTimestamps.sort(key=lambda x: x[0])  # Sort combined timestamps by time


def askSampleUsage():
    while True:
        choice = input("Do you want to use the first sample from each folder only? (yes/no): ").strip().lower()
        if choice in ['yes', 'no']: 
            return choice == 'yes'  
        print("Invalid input. Please enter 'yes' or 'no'.")


useFirstSampleOnly = askSampleUsage()

# Playback Function
def playRhythm(combinedTimestamps, numLoops):
    for repeat in range(numLoops):
        print(f"Playback repeat {repeat + 1}/{numLoops}")
        
        timeZero = time.time()  
        
        for timestamp, soundType, index in combinedTimestamps:
            now = time.time() - timeZero  
            
            while now < timestamp:
                time.sleep(0.001)  
                now = time.time() - timeZero
            
            
            if soundType == 'low':
                if useFirstSampleOnly:
                    print(f"Playing LOW sample 0 at timestamp {timestamp}")
                    lowSamples[0].play()  
                else:
                    print(f"Playing LOW sample {index % len(lowSamples)} at timestamp {timestamp}")
                    getSample(lowSamples, index).play()
            elif soundType == 'mid':
                if useFirstSampleOnly:
                    print(f"Playing MID sample 0 at timestamp {timestamp}")
                    midSamples[0].play() 
                else:
                    print(f"Playing MID sample {index % len(midSamples)} at timestamp {timestamp}")
                    getSample(midSamples, index).play()
            elif soundType == 'high':
                if useFirstSampleOnly:
                    print(f"Playing HIGH sample 0 at timestamp {timestamp}")
                    highSamples[0].play()  
                else:
                    print(f"Playing HIGH sample {index % len(highSamples)} at timestamp {timestamp}")
                    getSample(highSamples, index).play()

       
        time.sleep(0.1)

    print("Polyrhythm playback complete!")


playRhythm(combinedTimestamps, numLoops)


def saveMidiPrompt():
    while True:
        save_choice = input("Do you want to save the MIDI file? (yes/no): ").strip().lower()
        if save_choice in ['yes', 'no']:
            return save_choice == 'yes'  # Return True if 'yes', False otherwise
        print("Invalid input. Please enter 'yes' or 'no'.")


if saveMidiPrompt():
    saveFileName = getStringInput("Enter the name for the MIDI file (without extension): ")
    exportToMidi(lowTimestamps, midTimestamps, highTimestamps, bpm, saveFileName)  # Export MIDI file
