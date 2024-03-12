import numpy as np
import librosa
import crepe

class PitchEstimator():
    def __init__(self, *args, **kwargs):
        pass

    def estimate_dsp(self, spectrogram, sr):
        """
        https://librosa.org/doc/0.10.1/generated/librosa.piptrack.html#librosa.piptrack
        """
        pitches, magnitudes = librosa.piptrack(S=np.abs(spectrogram), sr=sr)
        return pitches, magnitudes

    def estimate_crepe(self, audio, sr, use_viterbi=True):
        """
        The current version only supports WAV files as input.
        The model is trained on 16 kHz audio, so if the input audio has a different sample rate, it will be first resampled to 16 kHz using resampy.
        TODO: remeber the threshold of crepe?
        """
        # time, frequency, confidence, activation = crepe.predict(audio, sr, viterbi=use_viterbi)
        return crepe.predict(audio, sr, viterbi=use_viterbi)

    # def estimate_pyin(self, audio):
    #     """
    #     Fundamental frequency (F0) estimation using probabilistic YIN (pYIN).
    #     https://librosa.org/doc/0.10.1/generated/librosa.pyin.html
    #     """
    #     # f0, voiced_flag, voiced_probs = librosa.pyin(audio)
    #     return librosa.pyin(audio)
