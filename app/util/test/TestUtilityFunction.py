import unittest

from app.util.UtilityFunction import transform, key


class TestUtilityFunction(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    def testTransform(self):
        self.assertEqual(transform(["a","b"],["c","d"]), "A,C,B,D")


    def testKey(self):
        self.assertEqual(key(["a","b"],["c","d"]), "a,c,b,d")
