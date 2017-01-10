from math import sqrt

def PythagoreanTriplet1000():
    lista = []
    for i in range(1,1000):
        for j in range(i,1000):
            if j+i > 1000:
                break
            for h in range(j,1000):
                if i+j+h > 1000:
                    break
                if ((i**2+j**2) == h**2)and (i+j+h == 1000):
                    lista =[i,j,h]
                    print(lista)
    return lista



def prod(lista):
    result = 1
    for i in lista:
        result *= i
    return result

print(prod(PythagoreanTriplet1000()))
                    

        




