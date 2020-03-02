from com.kakao.cafe.module.cafeWorker import CafeWorker
import unittest
from unittest.mock import patch
import io


class TestCafeWorker(unittest.TestCase):
    def setUp(self):
        try:
            self.impossible = CafeWorker()

        except TypeError as TE:
            self.impossible = TE.__str__()

    def testInstantiation(self):
        self.assertEqual(
            self.impossible,
            "Can't instantiate abstract class CafeWorker with abstract methods Print"
        )


if __name__ == '__main__':
    unittest.main()