from unittest import TestCase

import pytest

import expman.io_utils as io_utils


class TestLoader(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_simple(self):
        meta = io_utils.Metadata(foo="123", bar=[1, 2, 3])

        self.assertEqual(2, len(meta))
        self.assertIsInstance(meta.foo, str)
        self.assertIsInstance(meta.bar, list)

        self.assertEqual("123", meta["foo"])
        self.assertListEqual([1, 2, 3], meta["bar"])

        with pytest.raises(KeyError):
            _ = meta["nope"]

        with pytest.raises(AttributeError):
            _ = meta.nope
