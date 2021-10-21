import random

soma = 0
qtde = int(input('insira um numero de 1 a 10: '))

for i in range (qtde):
    num = random.randint(1, 10)
    print(num)
    soma += num
print('A soma total é ',soma)