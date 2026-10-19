import json
import requests


def emotion_detector(text_to_analyze):
    """
    This function detects the emotion from a provided input text
        - It uses the Watson emotion prediction NLP library
    """

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
        response_emotion_prediction = process_emotion(response.text)

    return response_emotion_prediction


def process_emotion(text_emotion):
    """
    The function is responsible for re-formatting the emotion output.
    It will record emotion scores and the dominant emotion
    """
    # Variable used to track dominate score
    dominant_emotion_score = 0.0
    # Dictionary of re-formatted emotion data
    formatted_emotion = {"dominant_emotion": ""}

    # Convert text response to json
    json_emotion = json.loads(text_emotion)

    # Build dict with emotion scores and dominant score
    emotion_predictions = json_emotion["emotionPredictions"]
    for emotion_prediction in emotion_predictions:
        # We will overwrite emotions for duplications across multiple emotion predictions
        for emotion, score in emotion_prediction["emotion"].items():
            formatted_emotion[emotion] = score
            # If an emotion's score is greater than value currently in dominant_emotion,
            # update to capture greater value
            if score > dominant_emotion_score:
                # Update variable used to track the highest score
                dominant_emotion_score = score
                formatted_emotion["dominant_emotion"] = emotion

    return formatted_emotion
