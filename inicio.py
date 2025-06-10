matriz1= []  
for i in range(2):
    linha = []
    for j in range (3):
        var1 = (input('escreva o nome do candidato(e tecle enter) :'))
        linha.append(var1)
    matriz1.append(linha)
matriz2 = []
for i in range(2):
    linha = []
    for j in range (3):
        var2 = int(input('escreva o número do candidato( e tecle enter):'))
        linha.append(var2)
    matriz2.append(linha)  
cand_1 = 0
cand_2 = 0
cand_3 = 0
cand_4 = 0
cand_5 = 0
cand_6 = 0
while True: 
    print('a votação irá começar, escolha o número do candidato que deseja votar')
    var3= int(input('número do candidato:'))
    if var3== matriz2[0][0]:
         print(f"você votou no candidato {matriz1[0][0]}")  
         cand_1 += 1
    if var3 == matriz2[0][1]:
         print(f"você votou no candidato {matriz1[0][1]}")
         cand_2 += 1
    if var3 == matriz2[0][2]:
         print(f"você votou no candidato {matriz1[0][2]}")
         cand_3 += 1
    if var3 == matriz2[1][0]:
         print(f"você votou no candidato {matriz1[1][0]}")
         cand_4 += 1
    if var3 == matriz2[1][1]:
         print(f"você votou no candidato {matriz1[1][1]}")
         cand_5 += 1
    if var3 == matriz2[1][2]:
         print(f"você votou no candidato {matriz1[1][2]}")
         cand_6 += 1
    if var3 not in matriz2[0] and var3 not in matriz2[1]:
        print('Nenhum voto computado.')
    numero = int(input("Digite um número (0 para sair/ 1 para continuar): "))
    if numero < 0:
        print("Número negativo ignorado.")
        continue  
    if numero == 0:
        break  
        
total_votos = cand_1 + cand_2 + cand_3 + cand_4 + cand_5 + cand_6 

if total_votos > 0:
    print('\nPorcentagem de votos:') 
    print(f'{matriz1[0][0]}: {cand_1/total_votos*100:.2f}%') 
    print(f'{matriz1[0][1]}: {cand_2/total_votos*100:.2f}%')
    print(f'{matriz1[0][2]}: {cand_3/total_votos*100:.2f}%')
    print(f'{matriz1[1][0]}: {cand_4/total_votos*100:.2f}%')
    print(f'{matriz1[1][1]}: {cand_5/total_votos*100:.2f}%')
    print(f'{matriz1[1][2]}: {cand_6/total_votos*100:.2f}%')
else:
    print('\nNenhum voto computado.')
