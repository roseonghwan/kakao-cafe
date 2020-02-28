import unittest


class TestModule(unittest.TestCase):
    def testDummy(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
