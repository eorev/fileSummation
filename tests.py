import unittest
from answer import answer

class TestAnswer(unittest.TestCase):
    def testBasic(self):
        self.assertEqual(answer([6, 5, 10, -3, 15, -999, 13]), 30)

    def testNegative(self):
        self.assertEqual(answer([6, -20 ,-4, -3, -1, -4, -5]), 0)

    def testZero(self):
        self.assertEqual(answer([6, 0, 0, 0, 0, 0, 0]), 0)
    
    def testEmpty(self):
        self.assertEqual(answer([]), 0)

    def testSingle(self):
        self.assertEqual(answer([2, 5, -999]), 5)

    def testNegativeNineFirst(self):
        self.assertEqual(answer([3, -999, 2, 3]), 0)


if __name__ == '__main__':
    unittest.main()