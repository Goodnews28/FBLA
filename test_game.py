import unittest
from unittest.mock import patch
from main import (
    initial_choice, get_choice, slowprint, 
    get_a_job, college, start_a_business,
    random_events, financial_decisions
)

class TestHeadStart(unittest.TestCase):
    def setUp(self):
        self.initial_net_worth = 1000
        self.initial_age = 18

    def test_get_choice_valid_input(self):
        with patch('builtins.input', return_value='1'):
            result = get_choice("Test prompt", ["1", "2", "3"])
            self.assertEqual(result, "1")

    def test_get_choice_invalid_then_valid(self):
        with patch('builtins.input', side_effect=['invalid', '2']):
            result = get_choice("Test prompt", ["1", "2", "3"])
            self.assertEqual(result, "2")

    def test_get_a_job_income_range(self):
        career, income = get_a_job()
        self.assertIsInstance(career, str)
        self.assertIsInstance(income, int)
        self.assertGreaterEqual(income, 15000)
        self.assertLessEqual(income, 52000)

    def test_college_in_state_choice(self):
        with patch('builtins.input', return_value='1'):
            career, income = college()
            self.assertIsInstance(career, str)
            self.assertIsInstance(income, int)
            self.assertGreaterEqual(income, 79000)

    def test_start_business_investment(self):
        net_worth, career, income = start_a_business()
        self.assertEqual(career, "Entrepreneur")
        self.assertIsInstance(income, int)
        self.assertGreaterEqual(income, 50000)
        self.assertLessEqual(income, 400000)

    def test_random_events_impact(self):
        initial_worth = 10000
        age = 25
        new_worth = random_events(age, initial_worth)
        self.assertIsInstance(new_worth, (int, float))

    @patch('random.random')
    def test_random_events_probability(self, mock_random):
        mock_random.return_value = 0.2  # Trigger event
        new_worth = random_events(25, 10000)
        self.assertNotEqual(new_worth, 10000)

    def test_slowprint_output(self):
        with patch('time.sleep'):  # Skip delays
            with patch('builtins.print') as mock_print:
                slowprint("Test message")
                mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()
