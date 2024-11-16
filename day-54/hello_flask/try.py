import time

def delay_decorator(function):
    def another_func():
        time.sleep(3)
        function()

    return another_func

@delay_decorator
# new=delay_decorator(say_hello)
# new() this is short way of doing this
def say_hello():
    print("hello world")
@delay_decorator
def greetings():
    print("How are you doing?")
@delay_decorator
def that_works():
    print("You are the best!")

say_hello()
greetings()
that_works()