
class MySimpleDecorator:

    def __init__(self, function):
        self.decorated_function = function

    def __call__(self, name):
        print('do something before')
        self.decorated_function(name)
        print('do something after')


# @MySimpleDecorator
def say_hello(name):
    print(f'hello {name}!')


say_hello_decorated = MySimpleDecorator(say_hello)
say_hello_decorated('Tanya')
