from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        emotion_response = emotion_detector("I am glad this happened")
        self.assertEqual(emotion_response["dominant_emotion"], "joy")
        emotion_response = emotion_detector("I am really mad about this")
        self.assertEqual(emotion_response["dominant_emotion"], "anger")
        emotion_response = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotion_response["dominant_emotion"], "disgust")
        emotion_response = emotion_detector("I am so sad about this")
        self.assertEqual(emotion_response["dominant_emotion"], "sadness")
        emotion_response = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotion_response["dominant_emotion"], "fear")

unittest.main()