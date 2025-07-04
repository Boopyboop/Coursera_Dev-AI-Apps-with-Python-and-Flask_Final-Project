# server.py

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def index():
    """
    Route for the home page. Renders the index.html file.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    API endpoint that detects emotions from the provided input text.

    Query Parameters:
        text (str): The text input from the user for emotion detection.

    Returns:
        str: A formatted string containing emotion scores and the dominant emotion.
    """
    # Get the text input from the request query parameters
    text_to_analyse = request.args.get("text")

    # Return an error if no text is provided
    if not text_to_analyse:
        return "Error: No text provided for emotion analysis.", 400

    # Call the emotion detector function from the EmotionDetection package
    result = emotion_detector(text_to_analyse)

    # If the result is None or incomplete, return an error
    if not result or "dominant_emotion" not in result:
        return "Error: Emotion detection failed. Please try again.", 500

    # Format the output string as required
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

# Run the app locally on port 5000
if __name__ == "__main__":
    app.run(debug=True, port=5000)
