# Project TODO List

This file tracks the planned features and next steps for the Music Analyzer project.

## High Priority

- [ ] **Frontend Development**:
    - [ ] Create a user interface with a file upload form.
    - [ ] Add JavaScript to handle the file upload and send it to the `/analyze` endpoint.
    - [ ] Display the returned tempo and beat analysis results on the page.
    - [ ] Implement a loading indicator to show while the analysis is in progress.

## Medium Priority

- [ ] **YouTube Integration**:
    - [ ] Add a text input field for YouTube URLs.
    - [ ] Implement backend logic using `yt-dlp` to download audio from the provided URL.
    - [ ] Feed the downloaded audio into the analysis pipeline.

- [ ] **Drum Transcription & Visualization**:
    - [ ] Integrate a source separation library (e.g., `spleeter`) to isolate the drum track.
    - [ ] Use onset detection on the drum track to identify individual drum hits.
    - [ ] Design and implement a front-end visualization for the drum pattern (e.g., using dots and dashes).

## Low Priority / Future Ideas

- [ ] **Advanced Analysis Features**:
    - [ ] Research and implement time signature detection.
    - [ ] Research and implement song structure analysis (e.g., identifying verse, chorus).

- [ ] **Refinements & Infrastructure**:
    - [ ] Add comprehensive error handling for both backend and frontend.
    - [ ] Implement a background task queue (e.g., Celery) to handle long-running analysis jobs without tying up the server.
    - [ ] Write unit and integration tests for the backend API and analysis functions.
