# Jules's Development Notes

This file contains technical notes and reminders for me, Jules, while working on this project.

## Project Structure

*   The main application code is located in the `music_analyzer/` directory.
*   `app.py`: Contains the Flask web server, routes, and API endpoint logic.
*   `analysis.py`: Houses the core audio processing functions. All `librosa`-related code should go here.
*   `static/`: For CSS and JavaScript files.
*   `templates/`: For HTML files.

## Environment & Tooling Notes

*   **File System Inconsistency**: The development environment has shown some unpredictable behavior with file visibility.
    *   Files created with `create_file_with_block` are not always immediately visible to the `run_in_bash_session` tool.
    *   The working directory for tools like `read_file` and `overwrite_file_with_block` is the repository root (`/app`).
    *   The working directory for `run_in_bash_session` seems to be `/app/music_analyzer`, but this has been unreliable.
*   **Best Practice**: To avoid issues, always use full, explicit paths from the repository root (e.g., `music_analyzer/app.py`) when using file-based tools. When using the bash session, `cd` into the `music_analyzer` directory and run commands from there.

## Running the Server

To run the server for development:

```bash
# Navigate to the correct directory
cd music_analyzer

# Run the app
python app.py
```
This will start the server in debug mode, which will automatically reload on code changes.

## Testing the API

The `/analyze` endpoint accepts a `POST` request with a file upload.

**Example `curl` command:**

Find the path to the sample audio file downloaded by `librosa`. It's usually in `~/.cache/librosa/`.

```bash
# Note: The exact file path might differ.
curl -X POST -F "file=@/home/jules/.cache/librosa/Kevin_MacLeod_-_P_I_Tchaikovsky_Dance_of_the_Sugar_Plum_Fairy.ogg" http://127.0.0.1:5000/analyze
```
