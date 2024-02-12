""" An emotion detection application using Watson NLP library endpoint """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    """ Gets argument string, calls emotion_detector method and return response """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid input ! Try again."
    return f"For the given statement, the system response is 'anger': {response['anger']}, " \
           f"'disgust': {response['disgust']}, 'fear': {response['fear']}, " \
           f"'joy': {response['joy']} and 'sadness': {response['sadness']}. " \
           f"The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """ Prints UI form """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
