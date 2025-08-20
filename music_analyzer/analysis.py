import librosa
import numpy as np

def analyze_structure(y, sr):
    """
    Analyzes the structure of a song.
    Returns a list of segment boundaries (in seconds).
    """
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    # Use a median filter to smooth the features
    chroma_smooth = np.median(chroma, axis=1, keepdims=True)
    # Stack the features to get a representation of the song's harmony
    _, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_chroma = librosa.util.sync(chroma, beat_frames, aggregate=np.median)
    # Get the segment boundaries, we can aim for a certain number of segments, e.g. 10
    boundaries = librosa.segment.agglomerative(beat_chroma, 10)
    # Convert frame boundaries to time
    boundary_times = librosa.frames_to_time(boundaries, sr=sr)
    # Make it a list of start and end times
    segments = []
    for i in range(len(boundary_times) - 1):
        segments.append((boundary_times[i], boundary_times[i+1]))
    return segments

def analyze_audio(filepath):
    """
    Analyzes an audio file to extract tempo and beat timings.
    Returns a dictionary with the analysis results.
    """
    y, sr = librosa.load(filepath)

    # Estimate tempo
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    if hasattr(tempo, 'shape') and tempo.shape:
        tempo_val = tempo[0]
    else:
        tempo_val = tempo

    # Get beat timings
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    # Analyze song structure
    segments = analyze_structure(y, sr)

    return {
        "tempo": round(tempo_val, 2),
        "beat_times": beat_times.tolist(),
        "segments": segments
    }

def analyze_default_track():
    """
    Analyzes the default librosa example track ('nutcracker').
    """
    example_file = librosa.ex('nutcracker')
    return analyze_audio(example_file)

if __name__ == '__main__':
    # This part is for command-line testing
    print("Getting example audio file...")
    example_file = librosa.ex('nutcracker')
    results = analyze_audio(example_file)
    print("Analysis Results:")
    print(results)
