import sys
def suma(*args):
    return sum([int(i) for i in args[0]])

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise "Es necesario por lo menos un argumento"
    
    else:
        print(suma(sys.argv[1:]))