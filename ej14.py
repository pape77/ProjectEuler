def longuestChainUnder(n):
    maximo = 1
    longuestChain = 0
    for i in range(1,n+1):
        actualLonguestChain = lChain(i)
        if ( len(actualLonguestChain) > longuestChain):
            maximo = i
            longuestChain = len(actualLonguestChain)
    return maximo

def lChain(n):
    if n == 1:
        return [1]
    elif n % 2:
        return [n]+ lChain(3*n +1)
    else:
        return [n]+lChain(int(n/2))



print(longuestChainUnder(1000000))
