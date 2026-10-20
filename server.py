"""
Flask module to deploy and run a web application for Emotion Prediction
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Initiate flask app
app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def emotion_detect():
    response_string = ""
    # Retrieve parameter from request object
    text_to_analyze = request.args.get('textToAnalyze')

    # Retrieve the emotion prediction response
    response = emotion_detector(text_to_analyze)
    if len(response) != 0 and response.get('dominant_emotion') is not None:
        response_string = "For the given statement, the system response is"
        for key, val in response.items():
            if key != "dominant_emotion":
                response_string += f", '{key}': {val}"

        response_string += f". The dominant emotion is {response.get('dominant_emotion')}."
    elif response.get('dominant_emotion') is None:
        response_string = "Invalid text! Please try again!"
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
    app.run(host="localhost", port=5000)
