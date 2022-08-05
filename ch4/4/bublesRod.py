from re import I
scores = [ 60 , 50 , 60 , 58 , 54 , 54 , 
           58 , 50 , 52 , 54 , 48 , 69 ,
           34 , 55 , 51 , 52 , 44 , 51 , 
           69 , 64 , 66 , 55 , 52 , 61 ,
           46 , 31 , 57 , 52 , 44 , 18 ,
           41 , 53 , 55 , 61 , 51 , 44]

maiorBubble = 0
i = 0 
tamanho  = len(scores)
while ( i < tamanho):
    if( maiorBubble < scores[i]):
        maiorBubble = scores[i]
    print ("Bubble solution #"+str(i) + " score: "+str(scores[i]))
    i = i + 1
print ("Bubbles tests: "+ str(tamanho))
print ("Highest bubble score: "+ str(maiorBubble))


output = " ["
i = 0
while (i < tamanho):
    if(maiorBubble == scores[i]):
        output = + ", " + output + str(i) 
    i = i + 1
output = output + "]"
print ("Solutions with highest score: " + output) 


