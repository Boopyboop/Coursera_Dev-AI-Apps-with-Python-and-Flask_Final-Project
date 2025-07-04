"""
Unit tests for the EmotionDetection package's emotion_detector function.

This test suite verifies that the emotion_detector correctly identifies
the dominant emotion from given text statements.

Test cases cover:
- Joy
- Anger
- Disgust
- Sadness
- Fear

Usage:
    Run the tests with the command:
    python -m unittest test_emotion_detection.py
"""

import unittest
from EmotionDetection import emotion_detector  # Import the function to test

class TestEmotionDetection(unittest.TestCase):
    """
    TestCase class to test emotion detection functionality.
    """

    def test_dominant_emotions(self):
        """
        Test emotion_detector for various statements with expected dominant emotions.

        Asserts that the returned dominant emotion matches the expected emotion for each input.
        """
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for text, expected_emotion in test_cases:
            with self.subTest(text=text):
                # Call the emotion_detector function with the test text
                result = emotion_detector(text)

                # Extract the dominant emotion from the result
                dominant_emotion = result.get('dominant_emotion')

                # Assert the dominant emotion is as expected
                self.assertEqual(dominant_emotion, expected_emotion,
                                 msg=f"Failed for input: '{text}'")

if __name__ == "__main__":
    # Run all unit tests
    unittest.main()
