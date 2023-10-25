nota1 = float(input('primeira nota'))
nota2 = float(input('segunda nota'))
media = (nota1 + nota2) / 2
print('media:',media)

if media<7.0:
    print('reprovado melhore na próxima')
elif media<10:
    print('aprovado')
else:
    print('aprovado bom aluno')