import unittest

from calculus_limits.limits import LimitTable

def add_one(x):
    return x + 1

def add_two(x):
    return x + 2


class TestLimitTable(unittest.TestCase):
    def setUp(self):
        self.limittable = LimitTable(5, 0.1, 3, add_one)

    def test_initialization(self):
        self.assertEqual(self.limittable.rows, 5, 'incorrect rows')
        self.assertEqual(self.limittable.max_delta, 0.1, 'incorrect max_delta')
        self.assertEqual(self.limittable.x_approaches, 3, 'incorrect x_approaches')
        self.assertEqual(self.limittable.func, add_one, 'incorrect func')



if __name__ == "__main__":
    unittest.main()