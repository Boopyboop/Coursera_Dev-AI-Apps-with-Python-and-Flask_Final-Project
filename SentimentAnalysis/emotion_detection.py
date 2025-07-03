import requests
import json
from typing import Dict, Any


def emotion_detector(text_to_analyze: str) -> Dict[str, Any]:
    """
    Analyze the emotions in a given piece of text using the Watson NLP Emotion API.

    Parameters:
        text_to_analyze (str): The input text to be analyzed for emotions.

    Returns:
        Dict[str, Any]: A dictionary containing the scores for anger, disgust, fear, joy,
                        and sadness, along with the dominant emotion.
                                        
    Raises:
        RuntimeError: If the API response is invalid or the request fails.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, json.JSONDecodeError) as err:
        raise RuntimeError("Failed to get a valid response from the emotion API") from err

    try:
        emotions = data["emotionPredictions"][0]["emotion"]
        relevant_emotions = {
            "anger": emotions.get("anger", 0.0),
            "disgust": emotions.get("disgust", 0.0),
            "fear": emotions.get("fear", 0.0),
            "joy": emotions.get("joy", 0.0),
            "sadness": emotions.get("sadness", 0.0),
        }
        dominant_emotion = max(relevant_emotions, key=relevant_emotions.get)
        relevant_emotions["dominant_emotion"] = dominant_emotion
        return relevant_emotions
    except (KeyError, IndexError, TypeError) as err:
        raise RuntimeError("Unexpected response format from emotion API") from err
