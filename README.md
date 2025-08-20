# Music Analyzer

This project is an interactive web application designed to act like a science museum exhibit about music. It allows users to upload a music track (or provide a YouTube URL) and visualizes its underlying structure.

The goal is to create a simple, engaging tool to show that music has structure and involves counting, making music theory concepts more accessible and fun.

## Features (Planned)

*   **Audio Input**: Analyze audio from local file uploads and YouTube videos.
*   **Core Analysis**:
    *   Extract tempo (BPM) and beat timings.
    *   Determine the time signature.
    *   Identify the song's structure (e.g., verse, chorus, bridge).
*   **Drum Visualization**: Isolate the drum track and display the pattern visually, similar to a drum machine interface.

## Tech Stack

*   **Backend**: Python with the Flask web framework.
*   **Audio Processing**: `librosa` library for music and audio analysis.
*   **Frontend**: HTML, CSS, and vanilla JavaScript.

## How to Run Locally

1.  **Clone the repository.**

2.  **Install dependencies:**
    ```bash
    pip install -r music_analyzer/requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python music_analyzer/app.py
    ```

4.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000`.
