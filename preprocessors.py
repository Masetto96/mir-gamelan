import librosa
import numpy as np


class Preprocessor(object):
    def __init__(self, *args, **kwargs):
        pass

    def compute_spectrogram(self, y):
        return np.abs(librosa.stft(y))
        # spectrogram = librosa.stft(y)
        # return spectrogram

    def apply_median_filtering(self, spectrogram):
        """
        Divides harmonic from percussive components.
        Returns harmonic.

        - you might want to have a look at this (https://librosa.org/librosa_gallery/auto_examples/plot_hprss.html)
        - note that librosa is already applying wiener masking
        - consider tweaking margin and kernel parameters of _librosa.decompose.hpss()_
        """
        D_harmonic, D_percussive = librosa.decompose.hpss(spectrogram)
        return D_harmonic

    def apply_NMF(self, spectrogram):
        """
        Applies non negative matrix factorization.
        Returns activations.
        https://librosa.org/doc/0.10.1/generated/librosa.decompose.decompose.html#librosa.decompose.decompose
        """
        comps, acts = librosa.decompose.decompose(np.abs(spectrogram))
        return acts
