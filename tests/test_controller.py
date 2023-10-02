import unittest

from controller import Controller

class TestController(unittest.TestCase):
    def setUp(self):
        # To create a Controller instance with test text
        self.controller = Controller("C'est un texte de test !")

    def test_remove_punctuation(self):
        result = self.controller.remove_punctuation()
        expected_text = "C est un texte de test  "
        self.assertEqual(result, expected_text)

    def test_text_splitter(self):
        result = self.controller.text_splitter()
        expected_words = ["C", "est", "un", "texte", "de", "test"]
        self.assertEqual(result, expected_words)


if __name__ == '__main__':
    unittest.main()
