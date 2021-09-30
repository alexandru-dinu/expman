from unittest import TestCase

from src.singleton import Singleton


class TestLoader(TestCase):
    def test_same_object(self):
        class MyClass(metaclass=Singleton):
            def __init__(self, x, y, z="hello"):
                self.x = x
                self.y = y
                self.z = z

        m1 = MyClass(1, y=2)  # args=(1,); kwargs={'y': 2}
        self.assertDictEqual(m1.__dict__, {"x": 1, "y": 2, "z": "hello"})

        # args and kwargs are ignored
        m2 = MyClass(x=2, y=3)
        self.assertDictEqual(m2.__dict__, {"x": 1, "y": 2, "z": "hello"})

        # don't need to specify args / kwargs, since m1 already provides the instance
        m3 = MyClass()
        print(f"{m3.__dict__=}")  # {'x': 1, 'y': 2, 'z': 'hello'}
        self.assertDictEqual(m3.__dict__, {"x": 1, "y": 2, "z": "hello"})

        # same object (id)
        self.assertTrue(m1 is m2)
        self.assertTrue(m2 is m3)
