import numpy
import scipy
import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load('faded.mp3')
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chromagram')
plt.tight_layout()
plt.show()
