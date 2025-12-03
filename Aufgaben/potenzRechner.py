basis = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))

def power(basis, exponent):
    p = basis ** exponent
    return p

p = power(basis, exponent)
print(p)