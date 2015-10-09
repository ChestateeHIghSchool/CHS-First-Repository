__author__ = 'darrell.skogman'
def addemup(a, b, c):
    return a+b+c

def subtract(a, b, c):
    return a-b-c

def main():
    a = int(input("first number "))
    b = int(input("second number "))
    c = int(input("third number "))

    print(addemup(a, b, c))
    print(subtract(a, b, c))

main()


