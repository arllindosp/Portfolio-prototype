especie = input('Informe a espécie do animal')
distancia = int(input('Informea distancia a ser percorrida no processo de migração')) # distancia em cm 
tamanho_passo = int(input('Informe o tamanho do passo do animal em cm'))

num_passo = 0
for i in range(0,distancia,tamanho_passo):
    num_passo += 1
print(f' O {especie} precisrá dar {num_passo} passos ate chegar ao seu destino')