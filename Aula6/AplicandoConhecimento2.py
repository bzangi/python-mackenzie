num = int(input())
while num <= 0:
    print('VALOR INVÁLIDO')
    num = int(input())
for i in range (1,num+1,1):
    if num % i == 0:
        print(i, end = ' ')