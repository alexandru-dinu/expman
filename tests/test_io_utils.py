from unittest import TestCase

import src.io_utils as io_utils

class TestLoader(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_simple(self):
        meta = io_utils.Metadata(**{'foo': 1, 'bar': 2})
        self.assertEqual(2, len(meta))
