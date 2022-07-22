def pescar_peixe ():
    print ('pesquei um peixe!')

def esperar ():
    print ('esperando...')
print ('eu amo você')
print ('pegar minhoca')
print ('colocar minhoca no anzol')
print ('arremessar a isca')
aindaNaoPescou = True
while aindaNaoPescou:
    response = input (' A boia afundou?')
    if response =='sim':
        aindaNaoPescou = False
        print ('Fisguei!')
        pescar_peixe()
    else:
        esperar ()
