import math

x = 1
countOfPrime = 500
countReturned = 1
maxDivisor = 0
primeNumber = 0
sumOfLogs = 0


while (countReturned < countOfPrime):
    #print (x)
    if (x < 3):
        primeNumber = x
    elif (x >= 3):
            y = int(math.sqrt(x))
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
                sumOfLogs = sumOfLogs + math.log(x)
                primeNumber = x
                countReturned = countReturned + 1
    x = x + 1

print ('The ' + str(countOfPrime) + 'th prime number is ' + str(primeNumber))
print ('The max divisor found in the numbers not prime is: ' + str(maxDivisor))
print ('Sum of the logs of primes: ' + str(sumOfLogs))
print ('Ratio is ' + str(sumOfLogs / primeNumber)) 