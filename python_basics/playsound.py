import simpleaudio as sa
import time
#User input gets converted to an integer.
try:
 repeats = int(input("How many times would you like the sound to be repeated?"))
except ValueError:
 print("Invalid input. Please enter a number.")


#wav file gets loaded.
wave_obj = sa.WaveObject.from_wave_file("C:/Users/Morris/Desktop/HKU/HKU_jaar2/CSD2/CSD2/NC.Neuro.capture.wav")
#for loop lets the sound play the amount of times the user has input
for x in range(repeats):
  play_obj = wave_obj.play()
  #play_obj.wait_done()
  time.sleep(2)
