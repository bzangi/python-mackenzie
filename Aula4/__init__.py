alunos = int(input())
if alunos == 0:
    print('NÃO HOUVE PROCESSAMENTO')
else:
    cont = 0
    nota = 0
    media = 0
    
    while cont < alunos:
        nota = float(input())
        if nota >= 6:
            print('PARABÉNS VOCÊ ESTÁ APROVADO')
        cont += 1
        media += nota
    mediageral = media/alunos
    print(mediageral)