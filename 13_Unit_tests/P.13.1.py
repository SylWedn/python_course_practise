import unittest
import datetime
from test_P4_1 import function_3, function_2, function_4, function_5, function_6, function_7, function_8, function_9, function_10


class TestFunction2(unittest.TestCase):

    def test_function_2(self):
        expectation_1 = 8
        expectation_2 = 2
        expectation_3 = 4
        result_1 = function_2([1, 1, 1, 1, 1, 1, 1, 1])
        result_2 = function_2([1, 1])
        result_3 = function_2([2, 2])
        self.assertEqual(expectation_1, result_1)
        self.assertEqual(expectation_2, result_2)
        self.assertEqual(expectation_3, result_3)


class TestFunction3(unittest.TestCase):

    def test_function_3(self):
        expectation_1 = 4
        expectation_2 = 16
        expectation_3 = 1
        result_1 = function_3(1, 2, 3, 4)
        result_2 = function_3(4, 12, 11, 16)
        result_3 = function_3(1, 21, 334, 46)
        self.assertEqual(expectation_1, result_1)
        self.assertEqual(expectation_2, result_2)
        self.assertNotEqual(expectation_3, result_3)


class TestFunction4(unittest.TestCase):

    def test_function_4(self):
        expectation_1 = 'saraviA'
        expectation_2 = 'olleH'
        expectation_3 = 'dlroW'
        result_1 = function_4("Aivaras")
        result_2 = function_4("Hello")
        result_3 = function_4("World")
        self.assertEqual(expectation_1, result_1)
        self.assertEqual(expectation_2, result_2)
        self.assertEqual(expectation_3, result_3)


class TestFunction5(unittest.TestCase):

    def test_function_5(self):
        expectation_1 = 7, 3, 4
        expectation_2 = 1, 12, 2
        expectation_3 = 1, 5, 4
        result_1 = function_5("13 AIVARAI 59 lol")
        result_2 = function_5("Judita aha taip 15")
        result_3 = function_5("Markas 12 46")
        self.assertEqual(expectation_1, result_1)
        self.assertEqual(expectation_2, result_2)
        self.assertEqual(expectation_3, result_3)


class TestFunction6(unittest.TestCase):

    def test_function_6(self):
        expectation_1 = [1, 2, 3, 4, 'dog']
        expectation_2 = [1, 2, 3, 4, 'cat']
        expectation_3 = [1, 2, 3, 4, 'mouse']
        result_1 = function_6([1, 1, 2, "dog", 3, 4, 4])
        result_2 = function_6([1, 1, 2, "cat", 3, 4, 4])
        result_3 = function_6([1, 1, 2, "mouse", 3, 4, 4])
        self.assertEqual(expectation_1, result_1)
        self.assertEqual(expectation_2, result_2)
        self.assertEqual(expectation_3, result_3)


class TestFunction7(unittest.TestCase):

    def test_function_7(self):
        expectation_1 = True
        expectation_2 = False
        expectation_3 = False
        result_1 = function_7(17)
        result_2 = function_7(33)
        result_3 = function_7(66)
        self.assertEqual(expectation_1, result_1)
        self.assertEqual(expectation_2, result_2)
        self.assertEqual(expectation_3, result_3)


class TestFunction8(unittest.TestCase):

    def test_function_8(self):
        expectation_1 = ['13', 'lol', 'dog', 'Python']
        expectation_2 = ['555', 'Python', 'of', 'Zen']
        expectation_3 = ['89', '45', 'world', 'Hello']
        result_1 = function_8("Python dog lol 13")
        result_2 = function_8("Zen of Python 555")
        result_3 = function_8("Hello world 45 89")
        self.assertEqual(expectation_1, result_1)
        self.assertEqual(expectation_2, result_2)
        self.assertEqual(expectation_3, result_3)


class TestFunction9(unittest.TestCase):

    def test_function_9(self):
        expectation_1 = True
        expectation_2 = False
        expectation_3 = True
        result_1 = function_9(2000)
        result_2 = function_9(2000)
        result_3 = function_9(1996)
        self.assertEqual(expectation_1, result_1)
        self.assertNotIsInstance(expectation_2, str)
        self.assertEqual(expectation_3, result_3)


class TestFunction10(unittest.TestCase):

    def test_function_10(self):
        expectation_1 = 360.0
        expectation_2 = 240.0
        expectation_3 = 720.0
        result_1 = function_10(datetime.datetime.now() - datetime.timedelta(days=15))
        result_2 = function_10(datetime.datetime.now() - datetime.timedelta(days=10))
        result_3 = function_10(datetime.datetime.now() - datetime.timedelta(days=30))
        self.assertEqual(expectation_1, result_1)
        self.assertEqual(expectation_2, result_2)
        self.assertEqual(expectation_3, result_3)


if __name__ == '__main__':
    unittest.main()
