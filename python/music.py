
import librosa.display
import librosa
import matplotlib.pyplot as plt
import numpy as np
import time

multiplier = 8

def getSongArray(filename):
  #load a track
  y, sr = librosa.load(filename, sr=2045*multiplier)

  #create a np array
  spec = librosa.feature.melspectrogram(y=y, sr=sr)
  librosa.display.specshow(spec,y_axis='mel', x_axis='s', sr=sr)
  db_spec = librosa.power_to_db(spec, ref=np.max,)

  print(sr)

  #get the sample count
  count = 0
  for x in db_spec[0]:
    count += 1
  print(count)

  #create an array of normalized pitches per time
  array = [[None]*128 for i in range(count)]
  for i in range(count):
    for j,x in enumerate(db_spec):
      array[i][j] = (x[i] + 80) / 80

  return array



array = getSongArray('/Users/maxim/Videos/IM.mp3')

for x in array:
  for y in x:
    if y < .1:
      print("_",end="")
    elif y < .4:
      print("‒",end="")
    else:
      print("¯",end="")

  print("\n\n\n")
  time.sleep(1/4/multiplier)


