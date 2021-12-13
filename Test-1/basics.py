
def calculator(a, b, expression):
    if expression == 'add':
        return a+b
    elif expression == 'sub':
        return a-b
    else:
        raise Exception('Invalid expression')


class ProductionClass:
    x = 400

    @classmethod
    def prod_method(cls):
        return cls.x * 1000
