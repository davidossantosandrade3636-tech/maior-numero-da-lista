lista=[]
while True:
     while True:
         try:
            num=int(input('digite um numero:'))
            lista.append(num)
            break
         except ValueError:
          print('Digite apenas numeros')
     while True:
         resp=str(input('Deseja continuar?[S/N]')).strip().upper()
         if resp in ['S','N']:
             break
         print('digite apenas S ou N')

     if resp=='N':
      break
print(f'O maior numero da lista foi {max(lista)}')