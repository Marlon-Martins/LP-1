3.Escreva um programa para ler valores inteiros fornecidos pelo usuário e escrevê-los em ordem crescente.

inteiros = list()
while True:
    n = int(input('Digite um número inteiro: '))
    resp = input('Continuar? [S]/[N]')
    resp = resp.upper()
    inteiros.append(n)
    inteiros.sort()
    if resp != 'S':
        break
print(inteiros) 

4.Escreva um programa que leia um número e informe se esse número é primo.

def primo(n):
    c = 1
    div = 0
    while c <= n:
        if (n % c == 0):
            div += 1
        c += 1
    if n <= 1:
        resp = False
    elif div > 2:
        resp = False
    else:
        resp = True
    return resp

11.Crie um programa para ler uma string fornecida pelo usuário. Informe se essa stringforma um palíndromo.

def inverso(a):
    mensagem = ""
    for letra in a:
        mensagem = letra + mensagem
    return mensagem

def palindromo(a):
    texto = ""
    for letra in a:
        if letra != " " and letra != "-" and letra != ",":
            texto += letra
    m = texto.lower()
    if inverso(m) == m:
        return True
    else:
        return False

12.Crie um programa para ler duas strings fornecidas pelo usuário. Verifique se elas foram um anagrama.

def anagrama(m1, m2):
    resp = True
    lista1 = list()
    lista2 = list()
    for letra in m1:
        lista1.append(letra.lower)
    for letra in m2:
        lista2.append(letra.lower)
    for letra in lista1:
        if letra not in lista2:
            resp = False
            break
        else:
            continue
    for letra in lista2:
        if letra not in lista1:
            resp = False
            break
        else:
            continue
    return resp

a = input('Escreva sua mensagem: ')
b = input('Escreva outra mensagem: ')
print(anagrama(a, b))

13.Faça um programa para multiplicar matrizes 3x3

def produto_matriz(matriz1, matriz2):    
    linha, coluna, line = 0, 0, 0
    matriz_final = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while linha < len(matriz1):
        while coluna < len(matriz2):
            while line < len(matriz2):
                matriz_final[linha][coluna] += matriz1[linha][line] * matriz2[line][coluna]
                line += 1
            line = 0
            coluna += 1
        coluna = 0
        linha += 1
    return matriz_final

        # Podemos verificar os resultados usando a biblioteca Numpy
        #import numpy
        #produto = numpy.dot(A, B) 
        #print(produto)



14.Faça um programa para calcular a soma, a subtração e a multiplicação de matrizes.
Você pode fornecer a matriz no código, em vez de ler o que o usuário digitar, 
mas suas funções que fazem os cálculos devem ser úteis para qualquer tamanho de matriz desde que as
propriedades matemáticas sejam respeitadas.

def operar_matrizez(matriz1, matriz2):
    resp = False
    linha = 0
    if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
        for linha in matriz1:
            for line in matriz2:
                if len(linha) == len(line):
                    resp = True
                else:
                    resp = False
                    break
    return resp

def soma_matriz(matriz1, matriz2):    
    if operar_matrizez(matriz1, matriz2):   
        matriz_final = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        linha, coluna = 0, 0
        while linha < len(matriz1):
            while coluna < len(matriz1):
                matriz_final[linha][coluna] = matriz1[linha][coluna] + matriz2[linha][coluna]
                coluna += 1
            linha += 1
            coluna = 0
    else:
        matriz_final = False
    return matriz_final

def sub_matriz(matriz1, matriz2):
    if operar_matrizez(matriz1, matriz2):
        matriz_final = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        linha, coluna = 0, 0
        while linha < len(matriz1):
            while coluna < len(matriz1):
                matriz_final[linha][coluna] = matriz1[linha][coluna] - matriz2[linha][coluna]
                coluna += 1
            linha += 1
            coluna = 0
    else:
        matriz_final = False
    return matriz_final

def multi_matriz(matriz1, matriz2):
    linha_1 = len(matriz1)
    coluna_1 = len(matriz1[0])
    linha_2 = len(matriz2)
    coluna_2 = len(matriz2[0])
    linha_final = list()
    matriz_final = list()
    if coluna_1 != linha_2: 
        matriz_final = "Não foi possível efetuar a multiplicação"
    else:
        for i in range(linha_1):
            for j in range(coluna_2):
                soma = 0
                for k in range(coluna_1):
                    soma += matriz1[i][k] * matriz2 [k][j]
                linha_final.append(soma)
            matriz_final.append(linha_final)
            linha_final = []
    return matriz_final


A = [[1, 1, 1], [2, 2, 2], [3, 1, 2]]   
B = [[8, 7, 6], [5, 4, 3], [2, 1, 0]]
C = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 1, 2, 3], [9, 0, 3, 2]]   
D = [[8, 7], [5, 4], [2, 1], [2, 9]]

print(soma_matriz(A, B))
print('')
print(sub_matriz(A, B))
print('')
print(multi_matriz(C, D))

15.Crie um programa que verifica todos os números perfeitos em um intervalo fornecido pelo usuário.
Ou seja, o usuário fornece dois valores (inicial e final) e o programa verifica se existe e quais são os
números perfeitos nesse intervalo. Para saber o que são números perfeitos, busque na wikipedia.

inicio = int(input('Onde o intervalo começa? '))
fim = int(input('Onde ele termina? '))

if inicio > fim:                #caso o usuário troque a ordem das variáveis 
    inicio, fim = fim, inicio

perfeitos = list()
n = inicio + 1
while n < fim:
    divisores = 0
    c = n - 1
    while c > 0:
        if (n % c) == 0:
            divisores += c
        c -= 1
    if divisores == n and n != 0:
            perfeitos.append(n)
    n += 1
print(perfeitos)    #[6, 28, 496, 8121, 33550336, 859869064...]

# Podemos economizar processamento pela formula 2^n−1(2^n - 1) 
primos = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73) #Uma tupla com os 20 primeiros primos
perfeitos = list()
perf_no_intervalo = list()
for primo in primos:
    perfeitos.append(2**(primo-1) * (2**primo - 1))
inicio = int(input('Onde o intervalo começa? '))
fim = int(input('Onde ele termina? '))
if inicio > fim:
    inicio, fim = fim, inicio
while inicio <= fim:
    if inicio in perfeitos:
        perf_no_intervalo.append(inicio)
    inicio += 1
print(perf_no_intervalo)

16 Jogo da Velha interativo

def ja_venceu(tabela): #Temos 8 casos possíveis para verificar
    vitoria = False
    if tabela[0][0] == tabela[0][1]:  # 3 casos horizontais 
        if tabela[0][0] == tabela[0][2]:
            vitoria = True
    if tabela[1][0] == tabela[1][1]:  # A lógica foi dividida em dois IF Statments por questões de legibilidade.
        if tabela[1][0] == tabela[1][2]:
            vitoria = True
    if tabela[2][0] == tabela[2][1]:
        if tabela[2][0] == tabela[2][2]:
            vitoria = True
    
    if tabela[0][0] == tabela[1][0]:  # 3 casos verticais 
        if tabela[0][0] == tabela[2][0]:
            vitoria = True
    if tabela[0][1] == tabela[1][1]:
        if tabela[0][1] == tabela[2][1]:
            vitoria = True
    if tabela[0][2] == tabela[1][2]:
        if tabela[0][2] == tabela[2][2]:
            vitoria = True
    
    if tabela[0][0] == tabela[1][1]:  # 2 casos diagonais
        if tabela[0][0] == tabela[2][2]:
            vitoria = True
    if tabela[0][2] == tabela[1][1]:
        if tabela[0][2] == tabela[2][0]:
            vitoria == False
    
    return vitoria


while True:  # O jogo começa aqui  
    vitoria = False
    n = 1
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('O jogador X começa\n')
    
    while True:
        if (n % 2) == 0:
            marca = 'O'
        else:
            marca = 'X'
        for linha in matriz:
            print(linha)
        try: 
            escolha = int(input('Para desistir/sair, digite qualquer valor não tabelado.\nDigite aonde jogar: '))
        except:   # Caso o jogador não digite um número, isso impede que o programa trave
            if marca == 'X':
                print('Tudo bem desistir às vezes...\nO jogador "O" foi declarado vencedor')
            else:
                print('Tudo bem desistir às vezes...\nO vencedor foi "X"')
            break
        
        if 0 < escolha <= 3:
            if matriz[0][escolha - 1] != 'X' and matriz[0][escolha - 1] != 'O':
                matriz[0][escolha - 1] = marca
                n += 1
            else:
                print('Jogada inválida')
        elif 3 < escolha <= 6:
            if matriz[1][escolha - 4] != 'X' and matriz[1][escolha - 4] != 'O':
                matriz[1][escolha - 4] = marca
                n += 1
            else:
                print('Jogada inválida')
        elif 6 < escolha <= 9:
            if matriz[2][escolha - 7] != 'X' and matriz[2][escolha - 7] != 'O':
                matriz[2][escolha - 7] = marca
                n += 1
            else:
                print('Jogada inválida')
        else:
            if marca == 'X':
                print('\nTudo bem desistir às vezes...\nO jogador "O" foi declarado vencedor')
            else:
                print('\nTudo bem desistir às vezes...\nO vencedor foi "X"')
            break
        
        if ja_venceu(matriz) == True:
            for linha in matriz:
                print(linha)
            print('\nTemos um ganhador! \nParabéns jogador', str(marca))
            break
        if n == 10:
            for linha in matriz:
                print(linha)
            print('\nTemos um empate')
            break
    resp = input('\nJogar novamente? [S]/[N] ')
    if resp == 'n' or resp == 'N':
        break

print('Tchau, até logo!')
