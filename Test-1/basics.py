
def calculator(a, b, expression):
    if expression == 'add':
        return a+b
    elif expression == 'sub':
        return a-b
    else:
        raise Exception('Invalid expression')
