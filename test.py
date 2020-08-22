import unittest
from game import read
import numpy as np

class TestGame(unittest.TestCase):

    def test_parsing(self):
        input = "..*\n.*."
        output = np.array([[0,0,1],[0,1,0]])
        self.assertTrue(np.all(output==read(input)))

if __name__=="__main__":
    unittest.main()
