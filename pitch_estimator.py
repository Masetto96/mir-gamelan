import numpy as np
import librosa

class PitchEstimator():
    def __init__(self, *args, **kwargs):
        pass

    def estimate_dsp(self, spectrogram, sr):
        """
        https://librosa.org/doc/0.10.1/generated/librosa.piptrack.html#librosa.piptrack
        """
        pitches, magnitudes = librosa.piptrack(S=np.abs(spectrogram), sr=sr)
        return pitches, magnitudes