primeNumber = 1 

while primeNumber <=100:
    if primeNumber >1:
        for i in range (2, primeNumber):
            if (primeNumber % i) == 0:
                break
        else:
            print(primeNumber)
    primeNumber +=1 