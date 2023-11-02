# write comprehensive unit tests for the functions you wrote in concept_questions.py
""" Testing is a critical part of software development that ensures that your code is doing what you think it is doing. Unit testing involves testing individual components of the program (usually functions or methods) in isolation from the rest of the system. The idea is to validate that each unit of the software performs as designed."""

import unittest

def is_isogram(word):
    word = word.lower()
    seen_letters = []
    for letter in word:
        if letter in seen_letters:
            return False
        seen_letters.append(letter)
    return True

class TestIsogram(unittest.TestCase):
    
    def test_empty_string(self):
        """Test that an empty string is considered an isogram."""
        self.assertTrue(is_isogram(''))

    def test_single_letter(self):
        """Test that a single letter is considered an isogram."""
        self.assertTrue(is_isogram('a'))

    def test_duplicate_letter(self):
        """Test that a string with duplicate letters is not an isogram."""
        self.assertFalse(is_isogram('hello'))

        def test_word_with_hyphen(self):
        # A word with a hyphen should be considered an isogram if the letters are not repeated
         self.assertTrue(is_isogram('six-year-old'))

    def test_word_with_space(self):
        # A phrase with spaces should be considered an isogram if the letters are not repeated
        self.assertTrue(is_isogram('lumber jacks'))

    def test_not_alpha_string(self):
        # A string with non-alphabetic characters is not considered for isogram checks
        self.assertTrue(is_isogram('12345'))

# This allows you to run the tests from the command line
if __name__ == '__main__':
    unittest.main()
