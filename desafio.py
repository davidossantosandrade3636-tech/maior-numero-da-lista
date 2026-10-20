from random import randint
itens=('Pedra','Papel','Tesoura')
computador=randint(0,2)
print('''suas opções
[0] pedra
[1] papel
[2] tesoura''')
jogador=int(input('qual é sua jogada'))
print('o computador escolheu {}'.format(itens[computador]))
print('o jogador escolheu {}'.format(itens[jogador]))
if computador==0:
    if jogador==0:
     print('=|'*17)desafio.py:13
     print('EMPATE')
     print('=|'*17)
    elif jogador==1:
        print('=|'*17)
        print('jogador vence')
        print('=|'*17)
    elif jogador==2:
         print('=|'*17)
         print('computador vence')
         print('=|'*17)

if computador==1:
    if jogador==0:
        print('=|'*17)
        print('computador vence')
        print('=|'*17)
    elif jogador==1:
        print('=|'*17)
        print('empate')
        print('=|'*17)
    elif jogador==2:
        print('=|'*17)
        print('jogador vence')
        print('=|'*17)
if computador==2:
    if jogador==0:
        print('=|'*17)
        print('jogador vence')
        print('=|'*17)
    elif jogador==1:
        print('=|'*17)
        print('computador vence')
        print('=|'*17)
    elif jogador==2:
        print('=|'*17)
        print('empate')
        print('=|'*17)