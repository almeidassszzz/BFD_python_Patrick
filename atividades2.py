#1- Crie um programa que exiba a mensagem "Olá, Mundo!" na tela.
#print("Olá, Mundo!")


#2- Crie uma variável para armazenar seu nome e em seguida exiba uma mensagem de boas-vindas que inclua seu nome.
#nome = Patrick
#print("Seja bem-vindo," , nome,"!")


#3- Crie duas variáveis com números inteiros e exiba a soma delas.
#a = 2
#b = 3
#c = a + b
#print(c)


#4- Peça ao usuário para digitar seu nome e em seguida exiba uma mensagem de boas-vindas com o nome fornecido.
#nome = input("Digite o seu nome: ")
#print("Seja bem-vindo," , nome,"!")


#5- Peça ao usuário para digitar o ano em que nasceu, calcule e exiba sua idade aproximada.
#nasceu = int(input("Digite o seu ano de nascimento: "))
#ano = 2025
#idade = ano - nasceu
#print("A sua idade aproximada é:", idade)


#6- Peça ao usuário para inserir duas notas, calcule a média e exiba o resultado.
#nota_1 = float(input("Insira a primeira nota: "))
#nota_2 = float(input("Insira a segunda nota: "))
#media = (nota_1 + nota_2) / 2
#print("A sua média final foi:", media)


#7- Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais).
#idade = int(input("Insira a sua idade: "))
#if idade >= 18:
#    print("Você é maior de idade!")
#else:
#    print("Você é menor de idade!")


#8- Peça um número e verifique se ele é positivo, negativo ou zero.
#numero = int(input("Insira um número positivo, negativo ou o zero: "))
#if numero >= 1:
#    print("O seu número é positivo!")
#elif numero == 0:
#    print("O seu número é zero!")
#else:
#    print("O seu número é negativo!")


#9- Peça um número e informe se ele é par ou ímpar.
#numero = int(input("Insira um número: "))
#if numero % 2 == 0:
#    print("Seu número é par!")
#else:
#    print("Seu número é ímpar!")


#10- Crie uma senha (ex: "1234") e peça para o usuário digitá-la. Informe se a senha está correta ou incorreta.
#senha = 1824
#password = int(input("Insira a senha determinada: "))
#if senha == password:
#    print("A senha está correta!")
#else:
#    print("A senha está errada!")


#11- Peça o valor de uma compra e, se for maior que R$ 100,00, aplique um desconto de 10%. Exiba o valor final.
#valor_compra = float(input("Insira o valor da compra: "))
#if valor_compra > 100:
#    desconto = valor_compra * 0.10
#    print("O valor da sua compra é:", valor_compra - desconto)
#else:
#    print("O valor da sua compra é:", valor_compra)


#12- Peça uma letra ao usuário e verifique se é uma vogal ou uma consoante.
#letra = input("Digite uma letra: ")
#if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#    print("É uma vogal!")
#else:
#    print("É uma consoante!")


#13- Peça dois números e informe qual deles é o maior, ou se são iguais.
#numero_1 = int(input("Informe o primeiro número: "))
#numero_2 = int(input("Informe o segundo número: "))
#if numero_1 > numero_2:
#    print("O primeiro número informado é maior que o segundo número informado!")
#elif numero_1 == numero_2:
#    print("Os números informados são iguais!")
#else:
#    print("O segundo número informado é maior que o primeiro número informado!")


#14- Crie um programa que exiba os números de 1 a 10.
#i = 1
#for i in range(10):
#   i = i + 1
#   print(i)


#15- Peça um número ao usuário e exiba a tabuada de multiplicação desse número, de 1 a 10.
#numero = int(input("Insira um número para calcularmos a sua tabuada até 10: "))
#i = 1
#for i in range(11):
#    vezes = numero * i
#    i = i + i
#    print(vezes)


#16- Peça números ao usuário até que ele digite 0. Ao final, exiba a soma de todos os números digitados.
#numero = int(input("Insira um número para iniciarmos: "))
#soma = 0
#while numero != 0:
#    soma = soma + numero
#    numero = (int(input("Insira um novo número: ")))
#print(soma)


#17- Crie um programa que peça uma senha ao usuário. Enquanto a senha não for "1234", continue pedindo.
#senha = 1234
#password = int(input("Insira a senha determinada: "))
#while senha != password:
#    password = int(input("Insira a senha determinada: "))


#18- Crie um programa que faça uma contagem regressiva de 10 até 0.
#n = 11
#while n != 0:
#    n = n - 1
#    print(n)


#19- Crie um número secreto e peça ao usuário para adivinhar. Dê dicas se o palpite foi maior ou menor, até ele acertar.
#segredo = 16
#tentativa = int(input("Arrisque um número: "))
#while tentativa != segredo:
#   if segredo > tentativa:
#      print("O número informado é menor que o número secreto!")
#      tentativa = int(input("Arrisque um número: "))
#   elif segredo < tentativa:
#       print("O número informado é maior do que o número secreto!")
#       tentativa = int(input("Arrisque um número: "))
#print("Você acertou o número secreto!")
    

#20- Crie um programa que itere de 1 a 20 e exiba apenas os números pares.
#i = 1
#par = []
#impar = []
#for i in range(21):
#    distribuir = i % 2
#    if distribuir == 0:
#        par.append(i)
#    else:
#        impar.append(i)
#print(par)


#21- Peça um número e calcule o seu fatorial (ex: 5! = 5 * 4 * 3 * 2 * 1).
#numero = int(input("Informe o número a ser calculado: "))
#resultado = 1
#for i in range(1, numero+1):
#    resultado *= i  
#print(resultado)


#22- Crie uma lista com 5 nomes de frutas e exiba cada fruta da lista.
#frutas = ["Banana", "Maçã", "Uva", "Abacaxi", "Goiaba"]
#print(frutas)


#23- Crie uma lista vazia e peça ao usuário para inserir 5 itens de uma lista de compras. Ao final, exiba a lista completa.
#lista = []
#for i in range(5):
#    inserir = input("Diga os itens que deseja ver na lista: ")
#    lista.append(inserir)
#print(lista)


#24- Dada uma lista de notas [7, 8, 5, 9, 6], calcule a média e exiba o resultado.
#notas = [7, 8, 5, 9, 6]
#soma = 0
#for i in notas:
#    soma = soma + i
#media = soma / 5
#print(media)


#25- Dada uma lista de números [10, 23, 4, 7, 15], encontre e exiba o maior e o menor número.
#numeros = [10, 23, 4, 7, 15]
#i = 0
#maior = 0
#menor = 50
#meio = 0
#for i in numeros:
#    if i > maior:
#        maior = i
#    elif i < menor:
#        menor = i
#    else:
#        meio = meio + 1
#print("O maior número é:", maior)
#print("O menor número é:", menor)


#26- Crie uma lista de nomes e peça um nome ao usuário. Verifique se o nome está na lista e exiba uma mensagem correspondente.
#nomes = ["Patrick", "Otávio", "Gabriel", "Amanda", "Letícia", "Julia"]
#for i in nomes:
#    teste = input("Insira um nome que está na lista:")
#    if teste == i:
#        print


#27- Crie uma função que exiba a mensagem "Bem-vindo ao programa!" e em seguida chame essa função.
#def oi():
#    return print("Bem-vindo ao programa!")
#teste = (oi())


#28- Crie uma função que receba um nome como parâmetro e exiba uma saudação personalizada.
#def personalizar():
#    nome = input("Digite o seu nome: ")
#    return print("Seja bem-vindo(a)", nome)
#teste = (personalizar())


#29- Crie uma função que receba dois números como parâmetros e retorne a soma deles.
#def soma(n1, n2):
#    return n1 + n2
#numero_1 = int(input("Insira o primeiro número de entrada: "))
#numero_2 = int(input("Insira o primeiro segundo de entrada: "))
#print(soma(numero_1, numero_2))


#30- Crie uma função que receba uma lista de números como parâmetro e retorne a média dos valores.
#def media(valores):
#    v = 0
#    for i in valores:
#        v = v + i
#    return v / len(valores)
#final = []
#inicial = int(input("Indique quantos valores você quer adicionar em uma lista: "))
#for i in range(inicial):
#    listando = int(input("Adicione o valor para adicionarmos na lista: "))
#    final.append(listando)
#print("O valor final é:", media(final))
