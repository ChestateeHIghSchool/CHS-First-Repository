__author__ = 'Nicholas Poole'
def addemup(a, b, c):
return a+b+c

def subc(a, b, c):
return a+b-c

def main():
a = int(input("first number "))
b = int(input("second number "))
c = int(input("third number "))

print(addemup(a, b, c))
print(subc(a, b, c))

main()
