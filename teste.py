use=input('digite seu nome de usuario').upper().strip()
senha=input('digite sua senha')
print('conta criada com sucesso!')
print('usario:{}'.format(use))
usee=input('digite seu nome de usuario,novamente').upper().strip()
senha=input('digite sua senha,novamente')

if use==usee and senha==senha:
    print('login realizado com sucesso!! seja bem vindo {}'.format(use))
else:
    print('usuario ou senha incorreto,ainda estão 1 tentativa')

    print('='*30)
    print('seja bem vindo a loja andrade')
    print('='*30)
    print('''oq vc deseja fazer?
    [ 1 ] ver produtos
    [ 2 ] fazer uma compra
    [ 3 ] ver meu saldo
    [ 4 ] sair''')
    opção=int(input('qual a opção?'))

if (opção==1):
    produtos=camieta=short=tenis=valor=quantidade=total=0
    print('vc escolheu opção 1')
    print('short,camiseta,tenis')
    print('vc escolheu a opção 2')
    print('vc escolheu fazer uma compra')


elif opção==2:
    print('vc escolheu fazer uma compra')
    produtos=input('qual o produto,deseja comprar')
elif produtos == 'camiseta':
     valor=79.99
     print('o valor da camiseta é R$ 79.99')
elif produtos=='short':
     valor=89.99
     print('o valor do short é R$ 89.99')
elif produtos=='tenis':
     valor=199.99
     print('o valor do tenis é R$ 199.99')
     quantidade=int(input('qual a quantidade de produtos?'))
     total=valor*quantidade
     print(f'o valor total da compra foi R$ {total:.2f }')

if   opção==3:
     print('vc escolheu a opção 3')
     saldo=int(input('seu saldo é de 2000'))

elif opção==4:
     print('vc escolheu a opção 4')

else:
     print('opção invalida')