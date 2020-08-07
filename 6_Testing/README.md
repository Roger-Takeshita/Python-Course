<h1 id='summary'>Summary</h1>

-   [Testing](#testing)
    -   [Unittest](#unittest)
    -   [Run Multiple Test Files](#runmultipletests)
    -   [setUp(self)](#setup)
    -   [tearDown(self)](#teardown)

<h1 id='testing'>Testing</h1>

[Go Back to Summary](#summary)

-   Python comes with a built-in test module called `unittest`
-   [unittest - Official Docs](https://docs.python.org/3/library/unittest.html)

<h2 id='unittest'>Unittest</h2>

[Go Back to Summary](#summary)

| Method                                                                                                             | Checks that          | New in |
| ------------------------------------------------------------------------------------------------------------------ | -------------------- | ------ |
| [assertEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)                 | a == b               |        |
| [assertNotEqual(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotEqual)           | a != b               |        |
| [assertTrue(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertTrue)                      | bool(x) is True      |        |
| [assertFalse(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertFalse)                    | bool(x) is False     |        |
| [assertIs(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIs)                       | a is b               | 3.1    |
| [assertIsNot(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNot)                 | a is not b           | 3.1    |
| [assertIsNone(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNone)                  | x is None            | 3.1    |
| [assertIsNotNone(x)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsNotNone)            | x is not None        | 3.1    |
| [assertIn(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn)                       | a in b               | 3.1    |
| [assertNotIn(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIn)                 | a not in b           | 3.1    |
| [assertIsInstance(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIsInstance)       | isinstance(a, b)     | 3.2    |
| [assertNotIsInstance(a, b)](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance) | not isinstance(a, b) | 3.2    |

-   To use the `unittest`, we need to:

    -   Import the file that we want to test
    -   Create a new class
        -   Then we inherit the `TestCase` from `unittest`
            -   `unittest.TestCase`
        -   Create a new function that describes what kind of test we are doing
        -   Do all the logic
        -   Then we can call `self.assertEqual` that we inherited from `unittest`
            -   `.assertEqual()` checks if both parameters are equal
    -   Run the `unittest`
        -   `unittest.main()` that will run the entire test file

-   in `main.py`

    ```Python
      def do_stuff(num):
      try:
          return int(num) +5
      except ValueError as error:
          return error
    ```

-   in `test.py`

    ```Python
      import unittest
      import main

      class TestMAin(unittest.TestCase):
          def test_do_stuff(self):
              test_param = 10
              result = main.do_stuff(test_param)
              self.assertEqual(result, 15)

          def test_do_stuff2(self):
              test_param = 'string'
              result = main.do_stuff(test_param)
              self.assertIsInstance(result, ValueError)

      unittest.main()
      # ----------------------------------------------------------------------
      # Ran 2 test in 0.000s
    ```

<h2 id='runmultipletests'>Run Multiple Test Files</h2>

[Go Back to Summary](#summary)

-   To run multiple test files, change directory to the test folder, and run the following command

    ```Bash
      python3 -m unittest
    ```

-   we can add an extra parameter `-v` (verbose)

    -   This command adds more information about each test, there we can see which test passed and which one not passed

    ```Bash
      test_do_stuff_equal_to_15 (test.TestUtility) ... ok
      test_do_stuff_invalid_number (test.TestUtility) ... ok
      test_do_stuff_is_instance_of_value_error (test.TestUtility) ... ok
      test_do_stuff_number_equals_empty (test.TestUtility) ... ok
      test_do_stuff_equal_to_15 (test2.TestUtility) ... ok
      test_do_stuff_invalid_number (test2.TestUtility) ... ok
      test_do_stuff_is_instance_of_value_error (test2.TestUtility) ... ok
      test_do_stuff_number_equals_empty (test2.TestUtility) ... ok

      ----------------------------------------------------------------------
      Ran 8 tests in 0.001s
    ```

<h2 id='setup'>setUp(self)</h2>

[Go Back to Summary](#summary)

-   the `setUp(self)` function, runs every time before each test

    ```Python
      import unittest
      import utility

      class TestUtility(unittest.TestCase):
          def setUp(self):
              print()
              print('dropping database...')
              print('creating database...')
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

      if __name__ == '__main__':
          unittest.main()
      # test_do_stuff_number_equals_empty (test.TestUtility) ...
      # deleting database...
      # creating new users...
      # ok
    ```

<h2 id='teardown'>tearDown(self)</h2>

[Go Back to Summary](#summary)

-   the `tearDown(self)` function, runs every time after each test

    ```Python
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
      # test_do_stuff_number_equals_empty (test.TestUtility) ...
      # deleting database...
      # creating new users...
      # closing connection with database
      # ok
    ```
