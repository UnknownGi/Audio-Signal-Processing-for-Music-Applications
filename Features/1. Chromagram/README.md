# Chromagram

## What is Chromagram? 

Chroma(also known as pitch class profile)- closely relates to 12 different pitch classes. Powerful tool for analyzing music whose pitches can be meaningfully categorized(often into 12 categories) and whose tuning approximates to the equal tempered scale. Main property of the chroma feature is that they capture harmonic and melodic characteristics of music, while being robust to changes in timbre and instrumentation. 

Pitch Class Set: {C, C♯, D, D♯, E ,F, F♯, G, G♯, A, A♯, B}

## Different Types of Chromagram

- STFT: Short-Time Fourier Transform, or alternatively short-term Fourier transform, is a Fourier-related transform used to determine the sinusoidal frequency and phase content of local sections of a signal as it changes over time.
- CQT: Constant-Q Transform transforms a data series to the frequency domain. It is related to the Fourier transform and very closely related to the complex Morlet wavelet transform.
- CENS: Chroma Energy Normalized.

## Comparison

Here we contrast by plotting graph of a Song **Alan Walker Faded:** https://www.youtube.com/watch?v=60ItHLz5WEA

![Comparison](http://i.imgur.com/Gkc3id5.png)

## References

1. Chroma STFT
    1. https://en.wikipedia.org/wiki/Short-time_Fourier_transform
    2. http://librosa.github.io/librosa/generated/librosa.feature.chroma_stft.html#librosa.feature.chroma_stft
2. Chroma CQT
    1. https://en.wikipedia.org/wiki/Constant-Q_transform
    2. http://librosa.github.io/librosa/generated/librosa.feature.chroma_cqt.html#librosa.feature.chroma_cqt
3. Chroma CENS: http://librosa.github.io/librosa/generated/librosa.feature.chroma_cens.html#librosa.feature.chroma_cens
