import unittest
from main import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        self.assertEqual(len(generate_password(12)), 12)
        self.assertEqual(len(generate_password(16)), 16)
        self.assertEqual(len(generate_password(20)), 20)
        self.assertEqual(len(generate_password(24)), 24)
        self.assertEqual(len(generate_password(28)), 28)

    def test_password_complexity(self):
        self.assertTrue(any(char.isupper() for char in generate_password()))
        self.assertTrue(any(char.islower() for char in generate_password()))
        self.assertTrue(any(char.isdigit() for char in generate_password()))
        self.assertTrue(any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/~" for char in generate_password()))


    def test_password_too_short(self):
        with self.assertRaises(ValueError):
            generate_password(8)
        with self.assertRaises(ValueError):
            generate_password(11)   

if __name__ == "__main__":
    unittest.main()

