__author__ = 'darrell.skogman'
def addemup(a, b, c):
    return a+b+c

def subtract(a, b, c):
    return a-b-c
    
def multiply(a,b,c):
    return a*b*c

def average(a,b,c):
    return a+b+c/3

def main():
    a = int(input("first number "))
    b = int(input("second number "))
    c = int(input("third number "))

    print(addemup(a, b, c))
    print(subtract(a, b, c))
    print(multiply(a,b,c))
    print(average(a,b,c))

main()


