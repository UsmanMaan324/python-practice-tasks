
def singleton(cls):

    instance = [None]

    def wrapper(*args, **kwargs):
        print(cls.__name__)
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper


@singleton
class SomeSingletonClass:
    x = 2

    def __init__(self):
        print("Created!")


if __name__ == '__main__':
    print("hello")
    instance = SomeSingletonClass()
    instance = SomeSingletonClass()
    print(instance.x)
    instance.x = 3
    print(SomeSingletonClass().x)