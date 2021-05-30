# Ernst Fanfan
# Testing decorators to test the various components in the project
# 5/27/2021
# Testing class
def ob(ob_func):
    def wrapper(*args, **kwargs):
        obj = ob_func(*args, **kwargs)
        print(f"Testing {type(obj)} object")
        print(obj)
        print("End of Testing")
        return obj

    return wrapper


def func_tester(func):
    def wrapper(*args, **kwargs):
        print("Testing Function")
        result = func(*args, **kwargs)
        print(result)
        print("End of Testing")
        return result

    return wrapper
