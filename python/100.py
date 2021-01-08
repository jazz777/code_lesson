import librosa
import IPython

def beepr():
  audio_path = librosa.util.example_audio_file()
  y_full, sr_full = librosa.load(audio_path)
  return IPython.display.Audio(data = y_full, rate=sr_full, autoplay = True)
print('what is my favorites  food ? 1 コロッケ　２　パエリア　３　天ぷら')
soul_food=input()
if int(soul_food) == 1:
    print('正解、なんで分かったの？')
    beepr()
elif int(soul_food) == 2:
    print('おしい')
elif int(soul_food) == 3:
    print('確かに')