import pygame
import time
import math

pygame.init()
kick = pygame.mixer.Sound("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/Kick.wav")

# Function to generate timestamps based on growth factor
def generateTimestamps(numNotes, totalTime, growthFactor):
    timestamps = []
    currentTime = 0
    startDuration = totalTime * (growthFactor - 1) / (growthFactor**numNotes - 1)  # Calculating starting duration

    for i in range(numNotes):
        timestamps.append(currentTime)
        currentTime += startDuration
        startDuration *= growthFactor  # Scale the duration by the growth factor for each note
    
    return timestamps

# User inputs
numKicks = int(input("How many kick notes?: "))
totalTime = float(input("How many seconds should the rhythm last?: "))
mode = input("Should the rhythm accelerate or decelerate? (Enter 'a' for accelerate, 'd' for decelerate): ")
numLoops = int(input("How many times should the rhythm loop?: "))  # New user input for the number of repetitions

# Determine growth factor based on acceleration or deceleration
if mode == 'a':
    growthFactor = 0.9  # For acceleration, we want a growth factor less than 1
elif mode == 'd':
    growthFactor = 1.1  # For deceleration, we want a growth factor greater than 1
else:
    print("Invalid input. Please enter 'a' for acceleration or 'd' for deceleration.")
    exit()

# Generate the timestamps based on the user inputs
kickTimestamps = generateTimestamps(numKicks, totalTime, growthFactor)

# Print out the calculated timestamps
print("Kick timestamps:", kickTimestamps)

# Playback the kicks
for repeat in range(numLoops):
    print(f"Playback repeat {repeat + 1}/{numLoops}")
    
    timeZero = time.time()  # Reset the base time for each loop
    
    for i, timestamp in enumerate(kickTimestamps):
        now = time.time() - timeZero
        
        while now < timestamp:
            time.sleep(0.001)
            now = time.time() - timeZero
        
        print(f"Playing kick at timestamp {timestamp}")
        kick.play()

    # Optionally, you can add a small buffer after each loop
    time.sleep(0.1)

print("Rhythm playback complete!")
