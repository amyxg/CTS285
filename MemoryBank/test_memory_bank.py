import unittest
from unittest.mock import patch
from memory_bank import MemoryBank

class TestMemoryBank(unittest.TestCase):
    def setUp(self):
        """Set up a new game instance before each test"""
        self.game = MemoryBank()

    def test_initial_values(self):
        """Test initial game values are set correctly"""
        self.assertEqual(self.game.level, 1)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.numbers_to_show, 2)
        self.assertEqual(self.game.display_time, 2)

    def test_generate_sequence(self):
        """Test sequence generation"""
        sequence = self.game.generate_sequence()
        self.assertEqual(len(sequence), self.game.numbers_to_show)
        for num in sequence:
            self.assertTrue(0 <= num <= 9)

    def test_check_sequence(self):
        """Test sequence checking"""
        original = [1, 2, 3]
        correct = [1, 2, 3]
        incorrect = [1, 2, 4]
        
        self.assertTrue(self.game.check_sequence(original, correct))
        self.assertFalse(self.game.check_sequence(original, incorrect))

    def test_update_difficulty(self):
        """Test difficulty updates correctly"""
        initial_numbers = self.game.numbers_to_show
        
        # Test successful round
        self.game.update_difficulty(True)
        self.assertEqual(self.game.level, 2)
        
        # Test if numbers_to_show increases every two levels
        self.game.update_difficulty(True)
        self.assertEqual(self.game.numbers_to_show, initial_numbers + 1)

if __name__ == '__main__':
    unittest.main()