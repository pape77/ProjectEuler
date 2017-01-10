from math import sqrt

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(int(n / i))
    for divisor in reversed(large_divisors):
        yield divisor


def findResult(numberOfDivisors):
    i =0
    actualTriangleNumber = 0
    largo = 0
    while(numberOfDivisors > largo):
        i+=1
        actualTriangleNumber += i
        largo = len(list(divisorGenerator(actualTriangleNumber)))
    return actualTriangleNumber


print(findResult(500))




        
