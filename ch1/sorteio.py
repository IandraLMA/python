import random


clientes = ['Jimmy', 'Kim', 'John', 'Stacie']
sabor = ' baunilha '
pedido = ' sundae de ' + sabor 
vencedor = random.choice(clientes)

print (' parabéns '+ vencedor +' você ganhou um sundae!')
prompt = 'Você quer uma cereja em cima? '
quer_cereja = input (prompt)
if ( quer_cereja == 'sim'):
    pedido = pedido + ' com uma cereja em cima'
prompt = 'Você quer banana em cima ? '
quer_banana = input (prompt)
if (quer_banana == 'sim'): 
    pedido = pedido + ' e uma banana em cima '
print (' Um ' + pedido + ' para ' + vencedor + ' saindo...')
