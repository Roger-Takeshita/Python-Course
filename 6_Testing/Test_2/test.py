import unittest
import main

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = main.run_guess(guess, answer)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        answer = 5
        guess = 3
        result = main.run_guess(guess, answer)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()