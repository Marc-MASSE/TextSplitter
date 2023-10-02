import unittest

from repository import Repository

class TestRepository(unittest.TestCase):
    def setUp(self):
        # To create a text for the tests
        self.test_file = 'test.txt'
        with open(self.test_file, 'w', encoding='utf-8') as file:
            file.write("Ceci est un test.\nCeci est une autre ligne.")

    def tearDown(self):
        # To delete test.txt after each text
        import os
        os.remove(self.test_file)

    def test_text_reader_existing_file(self):
        repos = Repository(self.test_file)
        text = repos.text_reader()
        self.assertIsNotNone(text)
        self.assertEqual(text, "Ceci est un test.\nCeci est une autre ligne.")

    def test_text_reader_non_existing_file(self):
        repos = Repository("non_existing_file.txt")
        text = repos.text_reader()
        self.assertIsNone(text)


if __name__ == '__main__':
    unittest.main()
