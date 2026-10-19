import request


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
    response = request.post(url, headers=headers, json=input_json)
    # Will check for text response only for 200 status-code
    if response.status_code == 200:
        response_emotion_prediction = response.text

    return response_emotion_prediction
