
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
        print("hello", end=" ")
        func(*args,**kwargs)
        print("bye")
    return wrapper


@decorator
def printname1(name):
    print(name,end=" ")

@decorator
def printname2(name):
    print(name,end=" ")



if __name__ == '__main__':
    # testing()
    printname1("ketu")
    printname1("sanjana")
