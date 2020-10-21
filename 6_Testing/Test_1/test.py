import unittest
import utility

class TestUtility(unittest.TestCase):
    def setUp(self):
        print()
        print('deleting database...')
        print('creating new users...')

    def test_do_stuff_equal_to_15(self):
        test_param = 10
        result = utility.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_is_instance_of_value_error(self):
        test_param = 'string'
        result = utility.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff_invalid_number(self):
        test_param = None
        result = utility.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff_number_equals_empty(self):
        test_param = ''
        result = utility.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def tearDown(self):
        print('cleaning up variables')
        print('closing connection with database')

if __name__ == '__main__':
    unittest.main()
