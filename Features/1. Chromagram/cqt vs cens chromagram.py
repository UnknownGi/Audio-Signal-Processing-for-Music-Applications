import numpy
import scipy
import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load('faded.mp3', offset=10, duration=15)
chroma_cens = librosa.feature.chroma_cens(y=y, sr=sr)
chroma_cqt = librosa.feature.chroma_cqt(y=y, sr=sr)

plt.figure()
plt.subplot(2,1,1)
librosa.display.specshow(chroma_cqt, y_axis='chroma')
plt.title('Chroma_CQT')
plt.colorbar()
plt.subplot(2,1,2)
librosa.display.specshow(chroma_cens, y_axis='chroma', x_axis='time')
plt.title('Chroma_CENS')
plt.colorbar()
plt.tight_layout()
plt.show()

