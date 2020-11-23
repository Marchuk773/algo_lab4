import unittest

from main import algorithm


class AlgorithmTests(unittest.TestCase):
    
    def testAlgorithm(self):
        self.assertEqual(algorithm('ijones1.in'), 5)
        self.assertEqual(algorithm('ijones2.in'), 2)
        self.assertEqual(algorithm('ijones3.in'), 201684)
        print('Tests passed!')
