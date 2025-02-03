import unittest
from unittest.mock import patch
from io import StringIO

from main import age_transition, college, financial_decisions, get_a_job, initial_choice, start_a_business

class TestHeadStartGame(unittest.TestCase):

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_a_job(self, mock_stdout, mock_input):
        career, income = get_a_job()
        output = mock_stdout.getvalue().strip()
        self.assertIn("You got a job", output)
        self.assertIsInstance(income, int)
        self.assertGreater(income, 0)

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=StringIO)
    def test_college(self, mock_stdout, mock_input):
        career, income = college()
        output = mock_stdout.getvalue().strip()
        self.assertIn("You chose to go to college", output)
        self.assertIsInstance(income, int)
        self.assertGreater(income, 0)

    @patch('builtins.input', return_value="2")
    @patch('sys.stdout', new_callable=StringIO)
    def test_start_a_business(self, mock_stdout, mock_input):
        net_worth, career, income = start_a_business()
        output = mock_stdout.getvalue().strip()
        self.assertIn("You started a business", output)
        self.assertIsInstance(income, int)
        self.assertGreater(income, 0)
        self.assertLess(net_worth, 1000)  # Business expense should reduce net worth

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=StringIO)
    def test_financial_decisions_save(self, mock_stdout, mock_input):
        global net_worth, income
        net_worth = 10000  # Set a starting net worth for the test
        income = 20000  # Set a starting income
        financial_decisions()
        output = mock_stdout.getvalue().strip()
        self.assertIn("You saved 50% of your income", output)
        self.assertEqual(net_worth, 20000)  # 50% of income should be saved

    @patch('builtins.input', return_value="2")
    @patch('sys.stdout', new_callable=StringIO)
    def test_financial_decisions_invest(self, mock_stdout, mock_input):
        global net_worth, income
        net_worth = 10000  # Set a starting net worth for the test
        income = 20000  # Set a starting income
        financial_decisions()
        output = mock_stdout.getvalue().strip()
        self.assertIn("You invested in stocks", output)
        self.assertGreater(net_worth, 10000)  # Net worth should increase due to investment

    @patch('builtins.input', return_value="3")
    @patch('sys.stdout', new_callable=StringIO)
    def test_financial_decisions_spend(self, mock_stdout, mock_input):
        global net_worth, income
        net_worth = 10000  # Set a starting net worth for the test
        income = 20000  # Set a starting income
        financial_decisions()
        output = mock_stdout.getvalue().strip()
        self.assertIn("You spent", output)
        self.assertLess(net_worth, 10000)  # Net worth should decrease due to spending

    @patch('builtins.input', return_value="5")
    @patch('sys.stdout', new_callable=StringIO)
    def test_age_transition(self, mock_stdout, mock_input):
        global age
        age = 18
        age_transition()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Congratulations! You have retired", output)

    @patch('builtins.input', return_value="1")
    @patch('sys.stdout', new_callable=StringIO)
    def test_initial_choice_job(self, mock_stdout, mock_input):
        global net_worth, income
        net_worth = 5000  # Set initial net worth for testing
        income = 20000  # Set initial income for testing
        career, income = initial_choice()
        output = mock_stdout.getvalue().strip()
        self.assertIn("You got a job", output)
        self.assertEqual(net_worth, 5000 + income)  # Net worth should increase by the income from the job

    @patch('builtins.input', return_value="stop")
    @patch('sys.stdout', new_callable=StringIO)
    def test_initial_choice_stop(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            initial_choice()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Game Over", output)

if __name__ == '__main__':
    unittest.main()
