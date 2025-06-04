cand_1 = 0
cand_2 = 0
cand_3 = 0
cand_4 = 0
cand_5 = 0
cand_6 = 0

matriz1= []
for i in range(2):
    linha = []
    for j in range (3):
        var1 = (input('escreva o nome dos candidatos em ordem :'))
        linha.append(var1)
    matriz1.append(linha)
matriz2 = []
for i in range(2):
    linha = []
    for j in range (3):
        var2 = int(input('escreva o número dos candidatos em ordem :'))
        linha.append(var2)
    matriz2.append(linha)
soma = 0

while True:
    var3= int(input('número do candidato votado  :'))
    
    numero = int(input("Digite um número (0|sair,1|continuar: "))
    
    if numero < 0:
        print("Número negativo ignorado.")
        continue  # Volta para o início do laço, sem executar o restante
    if numero == 0:
        break  # Sai do laço
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


print(f'{cand_1,cand_2,cand_3,cand_4,cand_5,cand_6}')
