import json
import requests


# This variable initializes the formated returned values with None
formatted_emotion = {
    'anger': None,
    'disgust': None,
    'fear': None,
    'joy': None,
    'dominant_emotion': None
}


def emotion_detector(text_to_analyze):
    """
    This function detects the emotion from a provided input text
        - It uses the Watson emotion prediction NLP library
    """

    # If user supplies empty input or string not containing 'emotionPredictions' or 'emotion'
    # return default object
    if text_to_analyze == "":
        return formatted_emotion

    # Default response value
    response_emotion_prediction = None
    # URL of service endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Header value that specifies the model to be used by NLP
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    # Dict representation of the required json input
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Post call to service endpoint
    response = requests.post(url, headers=headers, json=input_json)
    # Will check for text response only for 200 status-code
    if response.status_code == 200:
        if process_emotion(response.text) is None:
            response_emotion_prediction = formatted_emotion
    elif response.status_code == 400:
        response_emotion_prediction = formatted_emotion

    return response_emotion_prediction


def process_emotion(text_emotion):
    """
    The function is responsible for re-formatting the emotion output.
    It will record emotion scores and the dominant emotion
    """
    dominant_emotion = None

    # Convert text response to json
    json_emotion = json.loads(text_emotion)

    # Build dict with emotion scores and dominant score
    emotion_predictions = json_emotion.get("emotionPredictions")
    if emotion_predictions is not None:
        for emotion_prediction in emotion_predictions:
            # Default variable used to track dominant emotion
            dominant_emotion = {"emotion": "", "score": 0.0}

            emotions = emotion_prediction["emotion"]
            if emotions is not None:
                # We will overwrite emotions for duplications across multiple emotion predictions
                for emotion, score in emotions.items():
                    # Add emotion : score value pair
                    formatted_emotion[emotion] = score

                    # update dominant_emotion for higher scores or missing emotion value,
                    # update to capture greater value
                    if dominant_emotion == "" or score > dominant_emotion["score"]:
                        dominant_emotion = {"emotion": emotion, "score": score}

        # Add dominant_emotion key to the emotion having the highest score
        formatted_emotion["dominant_emotion"] = dominant_emotion["emotion"]

    return
