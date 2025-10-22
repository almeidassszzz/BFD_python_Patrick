#1 - Construa uma classe para armazenar informações de carros, cada objeto instanciado por essa classe deve ter os seguintes atributos:
#A - Modelo, marca, ano de lançamento, potência (1.0,1.6,etc), tipo de câmbio (manual ou automático), preço no lançamento.
#B - Crie um método para retornar cada atributo.
#Crie ao menos 3 instâncias de objeto, e execute todos os métodos para teste.

# forma de iniciar padrão, definindo as instâncias da atividade
#class Carro:
#    def __init__(self, modelo, marca, ano, potencia, cambio, preco):
#        self.modelo = modelo
#        self.marca = marca
#        self.ano = ano
#        self.potencia = potencia
#        self.cambio = cambio
#        self.preco = preco
#    
#    # metodos requisitado em que segui um padrao de construçao e tentei refinar algumas coisas; tipo o format de preço, mas nao deu muito certo
#    def verificar_modelo(self):
#        return f"O seu veículo é conhecido pelo nome de {self.modelo}!"
#    
#    def verificar_marca(self):
#        return f"O seu veículo foi fabricado pela marca {self.marca}!"
#    
#    def verificar_ano(self):
#        return f"O seu veículo foi fabricado no ano de {self.ano}!"
#    
#    def verificar_potencia(self):
#        return f"O seu veículo possui {self.marca} de potência em CV!"
#    
#    def verificar_cambio(self):
#        return f"O câmbio do seu veículo é {self.cambio}!"
#    
#    def verificar_preco(self):
#        return f"A atual cotação do mercado para o seu veículo é de R${self.preco}!"
#    
#
## questao estetica pra facilitar leitura
#print("=="*40)
#
## nomeando de forma generica e criando padrao de colocar. como ja tinha dito, queria deixar o format de preço no formato brasileiro, mas a unica forma era com replace e acho que nao valia estender o codigo assim
#i1 = Carro(modelo = "Corolla GR-Sport", marca = "Toyota", ano = 2025, potencia = 175, cambio = "automático", preco = "199.790,00")
#print(i1.verificar_modelo())
#print(i1.verificar_marca())
#print(i1.verificar_ano())
#print(i1.verificar_marca())
#print(i1.verificar_cambio())
#print(i1.verificar_preco())
#
#print("=="*40)
#
#i2 = Carro(modelo = "Mustang", marca = "Ford", ano = 1967, potencia = 120, cambio = "manual", preco = "199.790,00")
#print(i2.verificar_modelo())
#print(i2.verificar_marca())
#print(i2.verificar_ano())
#print(i2.verificar_marca())
#print(i2.verificar_cambio())
#print(i2.verificar_preco())
#
#print("=="*40)
#
#i3 = Carro(modelo = "Camaro Concept", marca = "Chevrolet", ano = 2006, potencia = 400, cambio = "manual", preco = "200.000,00")
#print(i3.verificar_modelo())
#print(i3.verificar_marca())
#print(i3.verificar_ano())
#print(i3.verificar_marca())
#print(i3.verificar_cambio())
#print(i3.verificar_preco())