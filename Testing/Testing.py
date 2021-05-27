# Ernst Fanfan
# Testing decorators to test the various components in the project
# 5/27/2021
# Testing class
def ob(ob_func):
    def wrapper(*args):
        obj = ob_func(*args)
        print(f"Testing {type(obj)} object")
        print(obj)
        print("End of Testing")
        return obj
    return wrapper
