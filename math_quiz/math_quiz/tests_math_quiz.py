import unittest
from math_quiz import Random_number as function_A, Random_operator as function_B, Arthmetic_operation as function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # TODO
        rand_op = function_B()
        self.assertIn(rand_op,'+-*','You have entered an invalid character, please enter a valid operator')
        # pass

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8,10,'-','8 - 10', -2),
                (5,5,'*','5 * 5', 25),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                actual_problem,actual_answer = function_C(num1,num2,operator) 
                self.assertEqual(expected_problem,actual_problem)
                self.assertEqual(expected_answer,actual_answer)
                pass

if __name__ == "__main__":
    unittest.main()
