import numpy
import scipy
import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load('force.mp3')
S = numpy.abs(librosa.stft(y, n_fft=4096))**2
chroma = librosa.feature.chroma_stft(S=S, sr=sr)
librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chromagram')
plt.tight_layout()
plt.show()
