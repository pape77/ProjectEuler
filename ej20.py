def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
num = factorial(100)
suma = 0
for i in str(num):
    suma += int(i)

print(suma)
    
