# %%
import librosa.display
import librosa
import matplotlib.pyplot as plt
import numpy as np
import time

# %%
multiplier = 8
y, sr = librosa.load('/Users/maxim/Videos/IM.mp3', sr=2045*multiplier)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# %%
spec = librosa.feature.melspectrogram(y=y, sr=sr)
librosa.display.specshow(spec,y_axis='mel', x_axis='s', sr=sr)
db_spec = librosa.power_to_db(spec, ref=np.max,)

for i,x in enumerate(db_spec):
  db_spec[i] = x[::1]

#librosa.display.specshow(db_spec,y_axis='mel', x_axis='s', sr=sr)
#plt.colorbar();

# %%
print(sr)

count = 0
for x in db_spec[0]:
  count += 1
print(count)

for x in beat_times:
  #print(x)
  pass


# %%
volArray = [0]*count
for x in db_spec:
  for i,y in enumerate(x):
    volArray[i] = volArray[i] + y + 80

# %%
#fig, ax = plt.subplots()
#ax.plot(range(count), volArray)
#plt.show()

# %%
array = [[None]*128 for i in range(count)]


for i in range(count):
  for j,x in enumerate(db_spec):
    array[i][j] = (x[i] + 80) / 80

#print(array)

# %%
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


