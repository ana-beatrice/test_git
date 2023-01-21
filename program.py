from contextlib import nullcontext


def div(a,b):
    if b == 0:
        print("Ana are mere")
        print("you can't divide a number by 0")
        return None
    return a/b

def sum(a, b):
    return a + b
