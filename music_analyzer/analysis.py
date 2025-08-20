import librosa

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

    return {
        "tempo": round(tempo_val, 2),
        "beat_times": beat_times.tolist() # convert numpy array to list for JSON serialization
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
