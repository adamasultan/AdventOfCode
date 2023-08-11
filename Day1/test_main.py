import unittest
import main

class TestMain(unittest.TestCase):
    def test_givencase(self):
        self.assertEquals(main.main([[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]), 24000)
    def test_simple(self):
        self.assertEquals(main.main([[1000], [2000]]), 2000)
        
    def test_open_file(self):
        self.assertEquals(len(main.open_file('elves.txt')), 246)
        self.assertEquals(type(main.open_file('elves.txt')[0][0]), int)



if __name__ == '__main__':
    unittest.main()