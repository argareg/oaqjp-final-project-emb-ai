import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    predicted_emotions = formatted_response["emotionPredictions"][0]["emotion"]
    return {
        'anger': predicted_emotions["anger"],
        'disgust': predicted_emotions["disgust"],
        'fear': predicted_emotions["fear"],
        'joy': predicted_emotions["joy"],
        'sadness': predicted_emotions["sadness"],
        'dominant_emotion': list(filter(lambda x: predicted_emotions[x] == max(predicted_emotions.values()), predicted_emotions))[0]
    }