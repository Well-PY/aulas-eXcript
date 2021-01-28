#Exercicios

#01 - Faça um algoritmo que apenas imprima o seu nome na tela e em seguida finalize a aplicação.
print("Wellington Rodrigues da Costa")

#02 - Faça um algoritmo que solicite ao usuário digitar o seu nome e em seguida envie a seguinte frase para a saída padrão: "O seu nome é: [nome do usuário]".
nome_1 = input("Digite o seu nome: ")

print("O seu nome é: ", nome_1)

#03 - Faça um algoritmo que solicite o nome e a idade do usuário e então, envie a seguinte frase para o Console: "O seu nome é <nome> e a sua idade é <idade>".
nome_2 = str(input("Digite o seu nome: "))
idade_1 = str(input("Digite a sua idade: "))

print("O seu nome é %s e a sua idade é %s" %(nome_2, idade_1))

#04 - Faça um algoritmo que solicite ao usuário informar um número. Em seguida, armazene este número numa variável. Por fim, envie esse número para a saída padrão.
num_1 = input("Digite um numero: ")

print("O numero digitado é: ", num_1)

#05 - Faça um algoritmo que solicite ao usuário informar um número. Em seguida, escreva a seguinte mensagem: "O número digitado foi: ".
num_2 = input("Digite um numero: ")

print("O número digitado foi: ", num_2)

#06 - Faça um algoritmo que solicite ao usuário informar 3 números. Em seguida, some-os e envie para a saída padrão a seguinte frase: "A soma total é: "
num_3 = float(input("Digite um número: "))
num_4 = float(input("Digite o segundo número: "))
num_5 = float(input("Digite o terceiro número: "))

soma = num_3 + num_4 + num_5

print("A soma total é: ", soma)

#07 - Faça um algoritmo que solicite ao usuário informar 2 números. Em seguida, some os valores e envie para a saída padrão a seguinte frase: "A soma entre <X> e <Y> é igual <total>".
num_6 = float(input("Digite um número: "))
num_7 = float(input("Digite outro número: "))

soma = num_6 + num_7

print("A soma entre %.2f e %.2f é igual %.2f" %(num_6, num_7, soma))

#08 - Faça um algoritmo que solicite a nota das 4 provas semestrais do usuário. Em seguida, calcule e envie para a saída padrão a média:
prova_1 = float(input("Digite a primeira nota: "))
prova_2 = float(input("Digite a segunda nota: "))
prova_3 = float(input("Digite a terceira nota: "))
prova_4 = float(input("Digite a quarta nota: "))

media = (prova_1 + prova_2 + prova_3 + prova_4) / 4

print("Sua média foi: ", media)

#09 - Faça um algoritmo em que o usuário informe uma medida em metros. Em seguida, converta essa medida para centímetros e envie para a saída padrão:
num_8 = float(input("Digite a quantidade de metros: "))

convert = num_8 * 100

print("O resultado da conversão foi: ", convert, "cm")

#10 - Faça um algoritmo que calcule o cubo e o quadrado de um determinado número:
num = float(input("Digite um numero: "))

print("O cubo do numero é", num**3)
print("O quadrado do numero é", num**4)

#11 - Faça um algoritmo que solicite ao usuário digitar 2 números. Em seguida, imprima o total decimal da divisão e o total inteiro (sem casas decimais):
num_1 = float(input("Digite um numero: "))
num_2 = float(input("Digite outro numero: "))

divisao = num_1 / num_2

resto = num_1 // num_2

print("O valor da divisão é: ", divisao)
print("Total inteiro: ", resto)

#12 - Faça um algoritmo que solicite a largura e a altura de um retângulo. Em seguida, imprima para o usuário quantos metros quadrados possui a área total.
altura = float(input("Digite a altura em centimetros: "))
largura = float(input("Digite a largura em centimetros: "))

print("A área do retângulo é: ", altura * largura,"cm²")

#13 - Faça um algoritmo que solicite ao usuário informar uma quantidade de dias, horas, minutos e segundos. Em seguida, converta tudo para segundos:
dia = float(input("Digite a quantidade de dias: "))
horas = float(input("Digite a quantidade de horas: "))
minutos = float(input("Digite quantos minutos: "))
segundos = float(input("Digite a quantidade de segundos: "))

dia = dia * 24 * 60 * 60
horas = horas * 60 * 60
minutos = minutos * 60

total = segundos + dia + horas + minutos

print("Total de segundos são: ", total)

#14 - Faça um algoritmo que solicite ao usuário informar o valor de uma compra. Em seguida, aplique 10% de desconto e imprima na tela tanto o valor total e também o valor com o desconto aplicado.
compra = float(input("Digite o valor da compra: "))

desconto = compra * 0.10

total = compra - desconto

print("Valor total: %.2f, desconto: %.2f, total: %.2f" %(compra, desconto, total))