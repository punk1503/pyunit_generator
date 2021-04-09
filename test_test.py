import unittest

class TESTNAME(unittest.TestCase):
    def test_0(self):
        self.assertEqual(test(123, 'Hello World'), 'test1')

    def test_1(self):
        self.assertEqual(test('Abrikoa', 'Hello World'), 'test2')

    def test_2(self):
        self.assertEqual(test(16.6, 'Hi'), 'testHi)

