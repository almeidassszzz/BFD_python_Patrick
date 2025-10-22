#2 - Suponha que estamos desenvolvendo um sistema para um banco. Este sistema deve obedecer as seguintes restrições:
#A - Uma classe pai chamada Cliente, com os atributos: nome, cpf, endereço.
#B - Uma classe filha chamada Conta_Corrente que deve herdar os atributos da classe pai mais o atributo "saldo". Este atributo deve ser privado.
#C - O sistema precisa ser capaz de: depositar, sacar, consultar saldo, consultar informações dos clientes e alterar informações dos clientes. Não deve ser possível ter saldo negativo, nem sacar além do saldo.
#Crie ao menos 1 instância de Conta_Corrente, execute todos os métodos para teste.



##classe inicial normal
#class Cliente:
#  def __init__(self, nome, cpf, endereco):
#    self.nome = nome
#    self.cpf = cpf
#    self.endereco = endereco
#
#
##puxando a classe padrao
#class Conta_Corrente(Cliente):
#    def __init__(self, nome, cpf, endereco, saldo):
#        super().__init__(nome, cpf, endereco)
#        self.__saldo = saldo
#
#    #replicando o metodo nada muito elaborado
#    def depositar(self):
#        self.__saldo += float(input("Insira o valor que você deseja depositar: "))
#        return f"Este é o seu saldo atual R${self.__saldo:.2f} após o depósito."
#
#    # tentando trazer "realismo"
#    def sacar(self): 
#        valor = float(input("Quanto você deseja sacar? \n Insira: "))
#        if valor <= self.__saldo:
#            self.__saldo -= valor
#            return f"Este é o seu saldo atual após o saque: R${self.__saldo:.2f}"
#        else:
#            return f"Operação inválida! Insira um valor compatível com o seu saldo atual. Para mais informações utilize a opção 'consultar_saldo'! Sistema reiniciando..."
#    
#    #metodo intuitivo
#    def consultar_saldo(self):
#        return f"Este é o seu saldo atual R${self.__saldo:.2f}"
#
#    # bem padrao, mas tentando trazer esse "realismo"
#    def consultar_info(self):
#        return f"Consultando os nossos sistemas... \n O cliente de nome {self.nome}, do CPF de número {self.cpf} e que atualmente residente no endereço {self.endereco} é um cliente com conta ativa em nossos sistemas."
#
#    #metodo pedido, mas fiz como se fosse um menu para facilitar o "entedimento" dos clientes.
#    def alterar_info(self):
#        escolha = input("Você deseja alterar qual dado da sua conta? \n Escolha: \n A)- Nome \n B)- CPF \n C)- Endereço \n Insira: " )
#        if escolha == "a" or escolha == "A":
#            self.nome = input("Atualize o seu nome: ")
#            return f"O seu novo nome em nossos sistemas é {self.nome}!"
#        elif escolha == "b" or escolha == "B":
#            self.cpf = input("Atualize o seu CPF: ")
#            return f"CPF atualizado! O seu novo CPF em nossos sistemas é:{self.cpf}"
#        elif escolha == "c" or escolha == "C":
#            self.endereco = input("Atualize o seu endereço: ")
#            return f"Novo endereço {self.endereco} inserido no sistema!"
#        else:
#            return f"Opção inválida! Sistema reiniciando..."
#
#
##vasco da gama
##Nuno = Conta_Corrente(nome = "Nuno Moreira", cpf = 180076543, endereco = "Avenida Vasco da Gama", saldo = 17000)
#
##prints com espaçamento para facilitar leitura – inclusive a minha que tava dificil
#print(Nuno.depositar())
#print("=="*40)
#print(Nuno.sacar())
#print("=="*40)
#print(Nuno.consultar_saldo())
#print("=="*40)
#print(Nuno.consultar_info())
#print("=="*40)
## aplico o metodo 3x para que possa explorar as 3 opçoes logo de cara sem necessidade reiniciar ou aplicar um while 
#print(Nuno.alterar_info())
#print("=="*40)
#print(Nuno.alterar_info())
#print("=="*40)
#print(Nuno.alterar_info())