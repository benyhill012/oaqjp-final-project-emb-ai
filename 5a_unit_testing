import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test joy emotion result
        joy_emotion = emotion_detector("I am glad this happened")
        self.assertEqual(joy_emotion["dominant_emotion"].lower(), "joy")

        # Test anger emotion result
        anger_emotion = emotion_detector("I am really mad about this")
        self.assertEqual(anger_emotion["dominant_emotion"].lower(), "anger")

        # Test disgust emotion result
        disgust_emotion = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(disgust_emotion["dominant_emotion"].lower(), "disgust")

        # Test sadness emotion result
        sadness_emotion = emotion_detector("I am so sad about this")
        self.assertEqual(sadness_emotion["dominant_emotion"].lower(), "sadness")

        # Test fear emotion result
        fear_emotion = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fear_emotion["dominant_emotion"].lower(), "fear")


unittest.main()
