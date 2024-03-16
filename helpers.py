import numpy as np
import librosa

def detect_pitch(S, sr, fmin, fmax):
    """
    Detects the pitch of the audio signal using the specified sample rate.

    Parameters:
    S (np.ndarray): The input spectrogram of the audio signal
    sr (number): The sample rate of the input audio signal

    Returns:
    np.ndarray: An array containing the detected pitches
    """
    # https://stackoverflow.com/questions/43877971/librosa-pitch-tracking-stft"""
    pitches, magnitudes = librosa.core.piptrack(S=S, sr=sr, fmin=fmin, fmax=fmax)
    # get indexes of the maximum value in each time slice
    max_indexes = np.argmax(magnitudes, axis=0)
    # get the pitches of the max indexes per time slice
    pitches = pitches[max_indexes, range(magnitudes.shape[1])]
    return pitches

def find_stable_regions(frequencies, window_size, threshold):
    """
    Generate stable regions based on input frequencies, window size, and threshold.
    
    Parameters:
    - frequencies (list): List of input frequencies.
    - window_size (int): Size of the window for calculating stable regions.
    - threshold (float): Threshold value for standard deviation to determine stability.
    
    Returns:
    - stable_regions (list): List of tuples indicating the start and end indices of stable regions.
    - segments (list): List of mean values of segments within stable regions.
    """
    # Initialize empty lists to store stable regions and segments
    stable_regions = []
    segments = []
    
    # Iterate over the input frequencies using a sliding window of size window_size
    for i in range(len(frequencies) - window_size + 1):
        # Extract the current segment
        segment = frequencies[i:i+window_size]
        
        # Calculate the standard deviation of the segment
        std_dev = np.std(segment)
        
        # If the standard deviation is below the threshold, consider the segment stable
        if std_dev < threshold:
            # Record the indices of the stable region
            stable_regions.append((i, i+window_size))
            
            # Calculate the mean value of the segment and round it to 2 decimal places
            segment_mean = round(np.mean(segment), 2)
            
            # Store the mean value of the segment
            segments.append(segment_mean)
    
    # Return the lists of stable regions and segments
    return stable_regions, segments
        

def group_and_average_frequencies(frequencies, threshold=10):
    """
    Group and average frequencies based on a given threshold.

    Parameters:
    - frequencies (list): List of frequencies.
    - threshold (int): Threshold value for grouping frequencies.

    Returns:
    - grouped_frequencies (list): List of averaged frequencies.
    """
    # Sort the input frequencies
    frequencies = sorted(frequencies)
    
    # Initialize empty list to store averaged frequencies
    grouped_frequencies = []
    
    # Initialize a list to store frequencies in the current group
    current_group = [frequencies[0]]

    # Iterate over the frequencies
    for i in range(1, len(frequencies)):
        # Check if the difference between the current and previous frequency is less than or equal to the threshold
        if frequencies[i] - frequencies[i - 1] <= threshold:
            # Add the current frequency to the current group
            current_group.append(frequencies[i])
        else:
            # Calculate the average of the current group and append it to the list of averaged frequencies
            grouped_frequencies.append(sum(current_group) / len(current_group))
            
            # Start a new group with the current frequency
            current_group = [frequencies[i]]

    # Calculate the average of the last group and append it to the list of averaged frequencies
    grouped_frequencies.append(sum(current_group) / len(current_group))

    # Return the list of averaged frequencies
    return grouped_frequencies


def compute_distance(tone_a, tone_b):
    if tone_a == 0: return 0
    distance_in_cents = 1200 * np.log2(tone_b / tone_a)
    return distance_in_cents


def find_scale(tone_group):
    """
    Find a scale in a given group of tones.

    Parameters:
    - tone_group (list): List of tones.

    Returns:
    - scale_distances (numpy.ndarray): Array of distances in cents between tones in the scale.
    """
    # Calculate the distance between each tone
    distances = []

    # Iterate over the tones
    for i in range(len(tone_group) - 1):
        # Calculate the distance between the current and next tone
        tone_a = tone_group[i]
        tone_b = tone_group[i + 1]
        d = compute_distance(tone_a, tone_b)
        # Append the distance to the list of distances
        distances.append(round(d, 2))

    # Iterate over the distances
    for i in range(len(distances) - 1):
        # Check if the consecutive distances are smaller than 200 cents
        if distances[i] < 200 and distances[i + 1] < 200:
            # Extract the scale from the tone group
            scale = tone_group[i : i + 6]
            # Print an error message if the scale is incomplete
            if len(scale) < 6:
                print(f"Could not find a complete scale... only found {len(scale)} tones")
                break
            # Unpack the scale
            ding, dong, deng, dung, dang, hiding = scale
            # Print the scale information
            print(f"Ding: {ding}")
            print(f"Dong: {dong}")
            print(f"Deng: {deng}")
            print(f"Dung: {dung}")
            print(f"Dang: {dang}")
            print(f"Hi-ding: {hiding}")
            # Extract the distances of the scale
            scale_distances = np.array(distances[i : i + 5])
            # Print the scale distances
            print(f"Scale distances: {scale_distances}")

    # Return the distances of the scale
    return scale_distances
