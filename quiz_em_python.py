print('Olá, jovem guerreiro! Como devo chama-lo?')

nome = input()

print('Pronto para se aventurar no Reino de Perguntation', ',', nome, '?')

print('Digite S/N.')

resposta = input()

if resposta == 'S' or 's':
    print('Então, daremos início ao desafio!')
else:
    print('Achou que iria fugir do desafio? Um guerreiro brasileiro nunca foge à luta! Começaremos mesmo assim!'
          )

print(
    'Vamos à primeira pergunta: Em que ano foi lançado o primeiro filme da franquia Harry Potter?'
)
print('')
print('A - 2002 |', ' B - 2001 |', ' C - 2003|', ' D - 2022')
opcao = input()

if opcao == 'B' or 'b':
    print('Parabéns', ',', nome,
          'você está no caminho para a glória, 10 pontos para Grifinória!')
else:
    print(
        'Desculpe, jovem bruxo! A resposta correta é: Alternativa B. -10 pontos para Grifinória!'
    )

print('______________________________________________')

print(
    'Vamos ao próximo desafio: Qual o nome do grande dragão que guarda as montanhas em O Hobbit?'
)
print('')
print('A - Smeagol | ', ' B - Godzilla |', ' C - King Kong |', ' D - Smaug')
opcao2 = input()

if opcao2 == 'D' or 'd':
    print('Parabéns', ',', nome,
          'você descobriu seu inimigo, não sofrerão a ira de Smaug!')
else:
    print(
        'Desculpe, pequeno Hobbit! A resposta correta é: Alternativa D. Smaug sentiu o seu cheiro e o pulverizou!'
    )

print('______________________________________________')

print(
    'Terceiro e último desafio: Qual o nome dado as revistinhas desenhadas em quadrinhos de heróis?'
)
print('')
print('A - Gibi |', ' B - Livrinho |', ' C - HQ |', ' D - Jornal do Comércio')
opcao3 = input()

if opcao3 == 'C' or 'c':
    print(
        'Parabéns', ',', nome,
        'você é um ótimo conhecedor da cultura geek e chegou ao final do desafio!'
    )
else:
    print(
        'Desculpe, jovem nerd! A resposta correta é: Alternativa C. Busque o conhecimento do mestre Yoda!'
    )

print('______________________________________________')

print('Fim do desafio!')
