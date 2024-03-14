import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class TuningSimilarityComputer(object):
    def __init__(self, fqs, *args, **kwargs):
        self.fqs = fqs
        print(f"Estimated freqs (Hz): {self.fqs}")
        self.begbeg, self.sedang, self.tirus = self._get_tuning_vectors()

    def _construct_invervals_from_fqs(self):

        # convert f0 values from Hz to Cents
        eps = np.finfo(float).eps
        f0Cents = 1200 * np.log2((self.fqs + eps) / 55.0)

        intervals = []
        for i in range(0, len(f0Cents) - 1):
            # simply take the diff between consecutive f0 values
            inter = np.abs(f0Cents[i + 1] - f0Cents[i])
            intervals.append(inter)

        print("Computed intervals (cents) ", intervals)
        return np.array(intervals)

    def _get_tuning_vectors(self):
        """
        Returns 3 gamelan tuning.
        Each entry in the vectors represent the interval in cents between consecutive tones starting from ding.
        """
        begbeg = np.array([120, 114, 432, 81, 453])
        sedang = np.array([136, 155, 379, 134, 396])
        tirus = np.array([197, 180, 347, 104, 372])
        return begbeg, sedang, tirus

    def compute_tuning_similarity(self):

        intervals = self._construct_invervals_from_fqs()
        assert len(intervals) == len(self.begbeg)

        # TODO: check other way of computing similarity
        sim = cosine_similarity(intervals.reshape(1, -1), [self.begbeg, self.sedang, self.tirus])

        return sim
