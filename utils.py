import numpy as np

def group_and_average_frequencies(frequencies, threshold=10):
    frequencies = sorted(frequencies)
    grouped_frequencies = []
    current_group = [frequencies[0]]
    
    for i in range(1, len(frequencies)):
        if frequencies[i] - frequencies[i-1] <= threshold:
            current_group.append(frequencies[i])
        else:
            grouped_frequencies.append(sum(current_group) / len(current_group))
            current_group = [frequencies[i]]
    
    grouped_frequencies.append(sum(current_group) / len(current_group))
    
    return grouped_frequencies


def get_tuning_vectors():
    """
    Returns 3 gamelan tuning.
    Each entry in the vectors represent the interval in cents between consecutive tones starting from ding.
    """
    begbeg = np.array([120, 114, 432, 81, 453])
    sedang = np.array([136, 155, 379, 134, 396])
    tirus = np.array([197, 180, 347, 104, 372])
    return begbeg, sedang, tirus


def segment_stable_frequency_regions(f0, stdThsld, minNoteDur, winStable, fs, H):
    """Segment the stable regions of a fundamental frequency track.
    
    Args:
        f0 (np.array): f0 values of a sound
        stdThsld (float): threshold for detecting stable regions in the f0 contour (in cents)
        minNoteDur (float): minimum allowed segment length (note duration)  
        winStable (int): number of samples used for computing standard deviation
        
    Result:
        segments (np.array): starting and ending frame indexes of every segment
        
    """
    eps = np.finfo(float).eps
    # convert f0 values from Hz to Cents (as described in pdf document)
    f0Cents = 1200*np.log2((f0+eps)/55.0)  

    # create an array containing standard deviation of last winStable samples
    stdArr = 10000000000*np.ones(f0.shape)
    for ii in range(winStable-1, len(f0)):
        stdArr[ii] = np.std(f0Cents[ii-winStable+1:ii+1])

    # apply threshold on standard deviation values to find indexes of the stable points in melody
    indFlat = np.where(stdArr<=stdThsld)[0]
    flatArr = np.zeros(f0.shape)
    flatArr[indFlat] = 1

    # create segments of continuous stable points such that consecutive stable points belong to same segment
    onset = np.where((flatArr[1:]-flatArr[:-1])==1)[0]+1
    offset = np.where((flatArr[1:]-flatArr[:-1])==-1)[0] 
    
    # remove any offset before onset (to sync them)
    indRem = np.where(offset<onset[0])[0]              
    offset = np.delete(offset, indRem)
    
    minN = min(onset.size, offset.size)
    segments = np.transpose(np.vstack((onset[:minN], offset[:minN])))

    # apply segment filtering, i.e. remove segments with are < minNoteDur in length
    minNoteSamples = int(np.ceil(minNoteDur*fs/H))
    diff = segments[:,1] - segments[:,0]
    indDel = np.where(diff<minNoteSamples)
    segments = np.delete(segments,indDel, axis=0)

    return segments


def select_stable_part(segment, threshold=0.1):
    """
    Selects the most stable part of a segment based on standard deviation.
    
    Parameters:
        segment (ndarray): Array containing the fundamental frequency estimates for the segment.
        threshold (float): Threshold to consider a part as stable. Default is 0.1.
        
    Returns:
        stable_part (ndarray): The most stable part of the segment.
    """
    std_dev = np.std(segment)
    if std_dev < threshold:
        return segment
    else:
        # Split segment into halves and recursively select the stable part
        mid = len(segment) // 2
        left_part = select_stable_part(segment[:mid], threshold)
        right_part = select_stable_part(segment[mid:], threshold)
        return np.concatenate((left_part, right_part))
   

