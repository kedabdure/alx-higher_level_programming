import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_max_integer(unittest.TestCase):
    """Class inherited form unittest to test the max integer
    """

    # test max at the end
    def test_max(self):
        self.assertEqual(max_integer([4, 5, 6, 56]), 56)

    # test max at the begning
    def test_max2(self):
        self.assertEqual(max_integer([6, 4, 5]), 6)

    # test max at the middle
    def test_max3(self):
        self.assertEqual(max_integer([6, 4, 16, 9, 5]), 16)

    # test max if one negative number in the list
    def test_max4(self):
        self.assertEqual(max_integer([6, 4, 16, -9, 5]), 16)

    # test max if only negative numbers in the list
    def test_max5(self):
        self.assertEqual(max_integer([-6, -4, -16, -9, -5]), -4)

    # test for list of one element
    def test_max6(self):
        self.assertEqual(max_integer([65]), 65)

    # test for list is empty
    def test_max7(self):
        self.assertEqual(max_integer([]), None)
