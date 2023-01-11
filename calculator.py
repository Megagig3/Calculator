x = int(input("input a number: "))
y = int(input("input next number: "))

def calculate( p, x, y):
    if p == "a":
        print(x + y)
    elif p == "s":
        print(x - y)
    elif p == "m":
        print(x * y)
    elif p == "d":
        print(x / y)
    elif p == "squ":
        print( x ** 2)
        print( y ** 2)
    else:
        print("error, invalid operator")

print(" a = addition")
print(" s = subtraction")
print(" m = multipication")
print(" d = division")
print(" squ = square")

p = input( "-> ")


calculate( p, x, y)