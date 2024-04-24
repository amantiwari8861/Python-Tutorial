from multipledispatch import dispatch

class MyClass:
    @dispatch(int)
    def my_method(self, arg1):
        print(f"One argument: {arg1}")

    @dispatch(int, int)
    def my_method(self, arg1, arg2):
        print(f"Two arguments: {arg1}, {arg2}")

obj = MyClass()
obj.my_method(10)          # Output: One argument: 10
obj.my_method(10, 20)      # Output: Two arguments: 10, 20
