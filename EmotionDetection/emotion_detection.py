import requests
import json

def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text by sending it to the sentiment analysis API.
    Handles empty input and API errors gracefully.

    Parameters:
        text_to_analyse (str): The input text to analyze.

    Returns:
        dict: Dictionary with keys 'anger', 'disgust', 'fear', 'joy', 'sadness', and 'dominant_emotion'.
              If the input is blank or API returns 400, all values are None.
    """
    if not text_to_analyse.strip():  # Check if input is empty or just whitespace
        # Return dictionary with None values for blank input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        # Bad request: treat as blank input or invalid text
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse JSON response from API
    formatted_response = json.loads(response.text)

    # Extract emotion scores
    emotions = formatted_response['documentSentiment']['emotion']
    anger_score = emotions.get('anger')
    disgust_score = emotions.get('disgust')
    fear_score = emotions.get('fear')
    joy_score = emotions.get('joy')
    sadness_score = emotions.get('sadness')

    # Find dominant emotion by max score
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
