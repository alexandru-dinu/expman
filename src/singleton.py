class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


if __name__ == "__main__":

    class MyClass(metaclass=Singleton):
        def __init__(self, x, y, z="hello"):
            self.x = x
            self.y = y
            self.z = z

    m1 = MyClass(1, y=2)  # args=(1,); kwargs={'y': 2}
    print(f"{m1.__dict__=}")  # {'x': 1, 'y': 2, 'z': 'hello'}

    # args and kwargs are ignored
    m2 = MyClass(x=2, y=3)
    print(f"{m2.__dict__=}")  # {'x': 1, 'y': 2, 'z': 'hello'}

    # don't need to specify args / kwargs, since m1 already provides the instance
    m3 = MyClass()
    print(f"{m3.__dict__=}")  # {'x': 1, 'y': 2, 'z': 'hello'}

    # same object (id)
    assert m1 is m2 and m2 is m3
