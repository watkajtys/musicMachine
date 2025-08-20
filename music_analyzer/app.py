from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from analysis import analyze_audio, analyze_default_track

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    try:
        default_analysis = analyze_default_track()
    except Exception as e:
        # In case the default analysis fails, we can pass an error or empty data
        default_analysis = {"error": f"Could not analyze default track: {e}"}
    return render_template('index.html', initial_analysis=default_analysis)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            results = analyze_audio(filepath)
            return jsonify(results)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            # Clean up the uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)


if __name__ == '__main__':
    app.run(debug=True)
