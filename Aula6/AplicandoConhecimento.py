cont = 1
num = int(input())
while num < 0 or num > 10:
    print('VALOR INVÁLIDO')
    num = int(input())
for cont in range (1,11):
    x = num * cont
    cont += 1
    print('%dx%d=%d' %(num, cont-1, x))