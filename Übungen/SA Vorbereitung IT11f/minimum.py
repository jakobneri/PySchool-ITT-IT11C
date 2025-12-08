def minimum(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c
    
result = minimum(9, 3, 4)
print("The minimum is:", result)