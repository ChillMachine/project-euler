#Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#Найдите сумму всех простых чисел меньше двух миллионов.
def checkPrime(num):
    d = 2
    while d * d <= num and num % d != 0:
        d += 1
    return d * d > num
result = 5
for x in range(5,2000000,2):
    if checkPrime(x): 
        print(x)
        result+=x
print(result)
