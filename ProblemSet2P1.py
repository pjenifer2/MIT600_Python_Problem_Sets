

x = 1
countOfPrime = 1000
countReturned = 1
maxDivisor = 0
primeNumber = 0


while (countReturned < countOfPrime):
    #print (x)
    if (x < 3):
        primeNumber = x
    elif (x >= 3):
            y = x -1
            divisorCount = 0
            while (y > 1):
                if ( x % y == 0 ):
                    divisorCount = divisorCount + 1
                    if (y > maxDivisor):
                        maxDivisor = y
                    y = y - 1
                else:
                    y = y - 1
            if (divisorCount == 0):
                primeNumber = x
                countReturned = countReturned + 1
    x = x + 1

print ('The 1000th prime number is ' + str(primeNumber))
print ('The max divisor found in the numbers not prime is: ' + str(maxDivisor))




