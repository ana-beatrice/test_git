from contextlib import nullcontext


def div(a, b):
    if b == 0:
        print("you can't divide a number by 0")
        return None
    return a / b


def diff(a, b):
    return a - b
    #as
