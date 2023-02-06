
def main():
    x = int(input("what is x:"))
    y = int(input("what is y:"))
    added(x, y)
    sub(x, y)
    divid(x, y)
    multi(x, y)
    moudle(x, y)


def moudle(x, y):
    print(x)
    print(y)
    print(x % y)


def added(x, y):
    print(x)
    print(y)
    print(x+y)


def sub(x, y):
    print(x)
    print(y)
    print(x-y)


def divid(x, y):
    print(x)
    print(y)
    print(x/y)


def multi(x, y):
    print(x)
    print(y)
    print(x*y)


main()
