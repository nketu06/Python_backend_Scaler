
def testing():
    try:
        print('A')
        print(10/0)
        print('B')
    except Exception as e:
        raise e
        print("C")
    
    except ZeroDivisionError:
        print('D')
    finally:
        print("E")


def decorator(func):
    def wrapper(*args,**kwargs):
        print("this is args of deco",args,kwargs)
        print("hello")
        func(*args,**kwargs)
        print("bye")
    return wrapper


def is_admin(func):
    def wrapper(*args,**kwargs):
        print("this is args of isadmin",args,kwargs)
        if not args[0]:
            print(f"{args[1]} is not a admin!")
            return False
        return func(args[1])
    return wrapper



@decorator
def printname1(name):
    print(name)

@is_admin
def printname2(name):
    print(name)


@decorator
@is_admin
def printname3(name):
    print(name)
# printname3 = decorator(is_admin(printname3))
# printname3(False,"k")


if __name__ == '__main__':
    # testing()
    # printname1("ketu")
    # printname2(True,"sanjana")
    printname3(False,"time")



