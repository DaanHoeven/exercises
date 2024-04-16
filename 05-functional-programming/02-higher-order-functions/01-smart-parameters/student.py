def repeat(function, n):
    for x in range(n):
        function()


def say_hello():
    print("Hello")


repeat(say_hello, 4)
