
import random
import momofuncoes



output= " "
scores= [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 
34, 55, 51, 52,  44, 51, 69, 64, 66, 55,52, 61,46, 31, 57,52,44,18, 41, 53,55, 
61, 51, 44]
jade = "jade"
print ("olá mundo!") 
animal = "jade"
print (animal)
print ("animal")
print ("O animal é:"  + animal)
print (" O " + animal)
print (scores)
print (scores [2])
print (" O conteúdo da posição dois é"+ str(scores[2]))
print (" O tamanho da lista é:" + str ( len (scores)  ))
print (str(random.randint(0,len(scores))))
tamanho = len(scores)
valorAleatorio = random.randint (0, tamanho)

print (" Escolher numero aleatorio da lista " + momofuncoes.retornarNumeroAleatorioDaLista(scores) )
print (" Escolher numero aleatorio " + str(random.randint(0,10)))
lista = ["a","b","c"] 
print ("Escolher letra aleatoria da lista scores" + momofuncoes.retornarNumeroAleatorioDaLista(lista) )

i = 0 
while (i < len(lista)):
 
 print (" o elemento #"+str(i) + " " + lista[i])
 i = i + 1


