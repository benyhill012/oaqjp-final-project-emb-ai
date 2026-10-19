"""
Flask module to deploy and run a web application for Emotion Prediction
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initiate flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector():
    response_string = ""
    # Retrieve parameter from request object
    text_to_analyze = request.args.get('textToAnalyze')

    # Retrieve the emotion prediction response
    response = emotion_detector(text_to_analyze)
    if len(response) != 0:
        response_string = "For the given statement, the system response is"
        for key, val in response:
            if key != "dominant_emotion":
                response_string.join(f" '{key}': {val}")
            else:
                response_string.join(f" The dominant emotion is {val}.")
    else:
        response_string = "Failed to retrieve an Emotion Detection response"

    return response_string

@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    ''' 
    Deploy app on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)