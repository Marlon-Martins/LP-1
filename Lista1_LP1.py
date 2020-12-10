1.Faça programas que:
    a.Leia um número e imprima o seu quadrado.
    b.Leia dois números e imprima a divisão do primeiro pelo segundo.
    c.Leia um número e imprima o resto da divisão desse número por 2.
    d.Leia dois número e imprima a média.
    e.Calcule   a   área   de   uma   circunferência   considerando   que   o   usuário   informe   o
    comprimento do raio. Para essa questão, declare uma variável “pi” com valor de 3,14 euse como valor de π. 
    Calcule também o comprimento e o diâmetro.
    
 1a)

n = input('Digite um número: ')
n = float(n)
print(n ** 2)

 1b)

a = input('Digite o primeiro número: ')
b = input('Digite o segundo número: ')
a = float(a)
b = float(b)
print(a + b)

 1c)

n = float(input('Digite um número: '))
print(n % 2)
 
 1d)

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
media = (a + b) / 2
print(media)

 1e)

pi = 3.14
raio = float(input('Digite o raio da circunferência: '))
area = pi * (raio ** 2)
diametro = raio * 2
comprimento = 2 * pi * raio
print('Diâmetro:', str(diametro))
print('Comprimento:', str(comprimento))
print('Área:', str(area))

2.Indique qual o resultado será obtido das seguintes expressões (lembre-se de usar “.” não“,” para casas decimais):
    a.4*4 + 1               = 9                         
    b.6 +20-23              = 3                          
    c.3,0* 5,0 +1           = 16.0          (".0" pois divisões retornam Float, não Integer)                
    d.1/4+2                 = 2.25          (".0" pois divisões retornam Float, não Integer)
    e.29,0/7+4              = 29    4.0     (O Python não aceita ',' para decimais)         
    f.3/6,0-7               = 0.5  -7       (O Python não aceita ',' para decimais)          
    g.2 / 2                 = 1.0           (" .0" pois divisões retornam Float, não Integer)
    h.2 // 2                = 1             (A divisão inteira '//' retorna a parte inteira)             
    i.4 % 2                 = 0             (O operador "%" retorna o resto da divisão)
    j.( 100 // 5 ) % 5      = 0             (A divisão inteira '//' retorna a parte inteira)

3.Indique o resultado lógico das seguintes expressões: 
    a.2 < 3                                           = Verdadeiro
    b.( 6 < 3 ) OU ( 10 > 11 )                        = Falso    
    c.((( 6 // 3 ) % 2 ) > 5 ) E ( 2 < ( 3 % 2 ) )    = Falso
    d.!( 2 < 3 )                                      = Falso         

4.Escreva   o   comando   de   atribuição   e   resolva   a   expressão   das   seguintes   fórmulas matemáticas:

    a)
a, b, c, d, e, f = 10, 3, 3, 4, 4, 2
x = 2 * ( ( a - ( b * 2 / c ) ) / ( d + ( e / f) ) )
print(x)
    ou
sup = ( a - ( b * 2 / c ) )
inf = ( d + ( e / f) )
x = (sup / inf) * 2
print(x)

    b)
x = 4
sup1 = (2 + x - ( 2 * (x ** (2 ** (x + 2) ) ) ) ) / 2
sup2 = ( (x + 1) ** 0.5 ) / x                           #{Poderia usar sqrt()}
sup = sup1 - sup2
y = sup / (3 ** x)                                      

print(y)

5.Faça   um   programa   para   ler   o   nome   do   usuário   e   escrever   na   tela   “Olá   [nomeinformando]”. 
Por exemplo, considere que eu use seu programa, vou escrever meu nome e oprograma deve imprimir “Olá Tiago”.

nome = input('Por favor, digite seu nome: ')
print('Olá,', nome)

6.Escreva   um   programa   para   ler   3   valores   inteiros   diferentes   e   escrevê-los   em   ordem crescente.

maior = int(input('Digite o primeiro valor: '))
b = int(input('Digite o próximo valor: '))
if b > maior:
    maior = b
c = int(input('Digite o próximo valor: '))
if c > maior:
    maior = c
print('O maior valor digitado foi:', str(maior))

7.Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

n = float(input('Digite um número: '))
if n >= 0:
    print('Esse número é positivo')
else:
    print('Este número é negativo')

8.Escreva um programa para ler uma temperatura em graus Celsius, calcular e escrever o valor correspondente em graus Fahrenheit e Kelvin.

c = float(input('Digite a temperatura em graus Celsius: '))
k = c + 273
f = (c * 1.8) + 32
print(str(c), 'Celcius é equivalente a', str(k), 'Kelvin e a', str(f), 'Fahrenheit')

9.Faça um programa que leia duas entradas de tipos numéricos. 
Verifique qual o maior dosdois ou se eles são iguais. Imprima uma mensagem informando.

x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
if x == y:
    print("Os números são iguais")
elif x > y:
    print(str(x), 'é maior que', str(y))
else:
    print(str(y), 'é maior que', str(x))

10.Escreva um programa que leia um número menor igual a 10 e informe se esse númeroé primo.

primos = [2, 3, 5, 7]
n = int(input('Digite um número natural menor ou igual a 10: '))
if n < 0:
    print('Número negativo')
elif n <= 10:
    if n in primos:
        print(str(n), 'é um número primo')
    else:
        print(str(n), 'não é um número primo')
else:
    print('Número maior que 10')

 11.Faça   um   programa   que   leia   três   entradas   de   inteiros.
Considere   que   cada   entrada corresponde   ao   comprimento   de   uma   aresta   de   um   triângulo.
Verifique   se   os   valores passados permitem que seja formado um triângulo 
considerando que elas devem se tocar nas extremidades

a = float(input('Digite o comprimento da primeira aresta: '))
b = float(input('Digite o comprimento da próxima aresta: '))
c = float(input('Digite o comprimento da próxima aresta: '))
if a < (b + c):
    if b < (a + c):
        if c < (a + b):
            print('Existe um triangulo com essas características')
        else:
            print('Não existe um triangulo com essas características')
    else:
        print('Não existe um triangulo com essas características')
else:
    print('Não existe um triangulo com essas características')

12.Faça um programa para calcular a área de um triângulo. O usuário deve fornecer os valores da base e da altura.

base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))
area = (base * altura) / 2
print('A área deste triângulo é', str(area))

13.Escreva um programa que leia três entradas numéricas correspondentes às arestas de um triângulos.
Caso os valores permitam que seja formado um triângulo, informe qual tipo de triângulo: 
(equilátero, isósceles ou escaleno).

x = float(input('Digite o comprimento da primeira aresta: '))
y = float(input('Digite o comprimento da próxima aresta: '))
z = float(input('Digite o comprimento da próxima aresta: '))

def triangulo(a, b, c):
    if a < (b + c):
        if b < (a + c):
            if c < (a + b):
                resp = True
            else:
                resp = False
        else:
            resp = False
    else:
        resp = False
    return resp

if triangulo(x, y, z):
    if x == y and y == z:
        print("Este triângulo é equilátero")
    elif x == y or y == z or z == x:
        print('Este triângulo é isósceles')
    else:
        print('Este triângulo é escaleno')
else:
    print('Não existe um triangulo com essas características')

14.Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o triângulo é 
Acutângulo, Retângulo ou Obtusângulo.
Sendo que:
- Triângulo Retângulo: possui um ângulo reto. (igual a 90º)
- Triângulo Obtusângulo: possui um ângulo obtuso. (maior que 90º)
- Triângulo Acutângulo: possui três ângulos agudos. (menor que 90º)

a = float(input("Digite o primeiro ângulo: "))
b = float(input("Digite o próximo ângulo: "))
c = 180 - (a + b)
print('O ângulo restante é', str(c))

if a == 90 or b == 90 or c == 90:
    print(str(a) + ',', str(b)+ 'e', str(c), ' formam um triângulo retângulo')
elif a > 90 or b > 90 or c > 90:
    print(str(a) + ',', str(b), 'e', str(c), ' formam um triângulo obtusângulo')
else:
    print(str(a) + ',', str(b)+ 'e', str(c), ' formam um triângulo acutângulo')  

15.Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar   um   determinado
cômodo   de   uma   residência. 
Dados   de   entrada:   a   potência   da lâmpada utilizada (em watts), 
as dimensões (largura e comprimento, em metros) do cômodo.
Considere que a potência necessária é de 18 watts por metro quadrado.

watts = float(input('Digite a potência da lâmpada: '))
x = float(input('Digite a largura do cômodo: '))
y = float(input('Digite o comprimento do cômodo: '))
potencia_necessaria = x * y * 18
lampadas = potencia_necessaria / watts
print('Serão necessárias', lampadas, 'lampadas para iluminar um cômodo de', str(x), "por", str(y))

16.Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,largura e altura), 
calcular e escrever a quantidade de caixas de azulejos para se colocar em todas   as   suas   paredes   
(considere   que   não   será   descontada   a   área   ocupada   por   portas   e janelas). 
Cada caixa de azulejos possui 1,5 m2.

x = float(input('Digite a largura do cômodo: '))
z = float(input('Digite o comprimento do cômodo: '))
y = float(input('Digite a altura do cômodo: '))
chao = x * z
paredes_maior = x * y * 2
paredes_menor = z * y * 2
total_area = chao + paredes_maior + paredes_menor 
caixas = total_area / 1.5
print('Área total =', str(total_area))
print('O total de caixas é:', str(caixas))

17.Um motorista de táxi deseja calcular o rendimento de seu carro na praça. 
Sabendo-se que o preço do combustível é de R$ 1,90, escreva um programa para ler: 
a marcação do odômetro (Km) no início do dia, 
a marcação (Km) no final do dia, 
o número de litros de combustível gasto e
o valor total (R$) recebido dos passageiros. 
Calcular e escrever: a média do consumo em Km/L e o lucro (líquido) do dia.

inicio = float(input('Quantos quilómetros marcavam o odômetro no início do dia? '))
fim = float(input('Quantos quilómetros marcam agora? '))
litros = float(input('Quantos litros foram gastos? '))
receita = float(input('Valor total recebido: R$'))
km = fim - inicio
consumo_medio = km / litros
custo = litros * 1.9
lucro = receita - custo
print('Seu carro consume uma média de', str(consumo_medio), 'litros')
print('Seu lucro foi de', str(lucro))

18.Escreva   um   programa   que   leia   as   notas   das   duas   avaliações   normais
e   a   nota   da avaliação optativa. 
Caso o aluno não tenha feito a optativa deve ser fornecido o valor –1.
Calcular a média do semestre considerando que a nota mais baixa será excluída do calculo.
Escrever a média e mensagens que indiquem se o aluno foi aprovado, reprovado ou está em exame, 
de acordo com as informações abaixo:
    Aprovado : media >= 6.0
    Reprovado: media < 3.0
    Exame : media >= 3.0 e < 6.0

nota1 = float(input('Digite o valor da primeira nota: '))
menor = nota1
nota2 = float(input('Digite o valor da segunda nota: '))
if nota2 < menor:
    menor = nota2
optativa = float(input('Digite o valor da optativa, caso não tenha feito, digite -1'))
if optativa < menor:
    media = (nota1 + nota2) / 2
elif nota2 == menor:
    media = (nota1 + optativa) / 2
elif nota1 == menor:
    media = (nota2 + optativa) / 2
if media >= 6:
    print('Aluno aprovado com media', str(media))
elif media >= 3 and media < 6:
    print('Aluno de exame. Sua média foi', str(media))
else:
    print('Aluno reprovado. Sua média', str(media), 'foi insuficiente')

19.Escreva um programa que leia a idade de 2 homens e 2 mulheres 
(considere que aidade dos homens será sempre diferente, assim como as idades das mulheres). 
Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e
o produto das idades do homem mais novo com a mulher mais velha.

homem1 = int(input('Digite a idade do primeiro homem: '))
homem2 = int(input('Digite a idade do segundo homem: '))
mulher1 = int(input('Digite a idade da primeira mulher: '))
mulher2 = int(input('Digite a idade da segunda mulher: '))

if homem1 >= homem2:
    h_mais_velho = homem1
    h_mais_novo = homem2
else:
    h_mais_velho = homem2
    h_mais_novo = homem1
if mulher1 >= mulher2:
    m_mais_velha = mulher1
    m_mais_nova = mulher2
else:
    m_mais_velha = mulher2
    m_mais_nova = mulher1

soma = h_mais_velho + m_mais_nova
produto = (h_mais_novo) * (m_mais_velha)
print('A soma das idades do homem mais velho e da mulher mais nova é', str(soma))
print('O produto das idades do homem mais novo com a mulher mais velha é', str(produto))

20.Crie um programa para ler duas entradas de Strings fornecidas pelo usuário. 
Verifique se as Strings são iguais ou diferentes. 
Imprima uma mensagem na saída padrão indicando o resultado da verificação.

a = input('Digite algo: ')
b = input('Mais uma vez: ')
if a == b:
    print('As duas Strings são iguais')
else:
    print('As Strings são diferentes')
