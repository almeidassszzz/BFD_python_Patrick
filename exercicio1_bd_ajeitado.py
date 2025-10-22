import sqlite3

con = sqlite3.connect("teste.db")

cursor = con.cursor()

print("=="*72)
print("Banco de dados sendo sendo conectado... \n Banco de dados online!")
print("=="*72)

cursor.execute(""" CREATE TABLE IF NOT EXISTS clientes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade TEXT NOT NULL,
               cpf TEXT NOT NULL, 
               email TEXT NOT NULL,
               endereco TEXT NOT NULL,
               sexo TEXT NOT NULL,
               salario TEXT NOT NUll); """)

print("Finalizando o processo...\n Banco de dados criado com sucesso!")
print("=="*72)

cursor.execute("INSERT INTO clientes (nome, idade, cpf, email, endereco, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Patrick", "21", "184.585.684-99", "trick@gmail.com", "Trav. São José, 650", "Masculino", "2.300"))

cursor.execute("INSERT INTO clientes (nome, idade, cpf, email, endereco, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Gabriel", "21", "745.856.096-00", "sosa@gmail.com", "Noronha Torrezão, 104", "Masculino", "2.500"))

cursor.execute("INSERT INTO clientes (nome, idade, cpf, email, endereco, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Larissa", "24", "111.687.757-00", "lilissa@gmail.com", "Largo do Marrom, 22", "Feminino", "6.500"))

print("Dados sendo inseridos... \n Dados inseridos com sucesso! Tabela atualizada!")
print("=="*72)

cursor.execute("SELECT * FROM clientes;")

resultado = cursor.fetchall()

print("Carregando a lista de clientes do nosso banco... \n Lista ilustrada:")
print("=="*72)

for i in resultado:
    print(f"Buscando por dados de clientes... \n ID: {i[0]}, Nome: {i[1]}, Idade: {i[2]}, CPF: {i[3]}, E-mail: {i[4]}, Endereço: {i[5]}, Sexo: {i[6]}, Salário: {i[7]}.")

print("=="*72)

cursor.execute("SELECT * FROM clientes WHERE sexo = 'Feminino';")
sexo = cursor.fetchall()

for a in sexo:
    print(f"Buscando por dados de clientes conforme os requisitos... \n ID: {i[0]}, Nome: {i[1]}, Idade: {i[2]}, CPF: {i[3]}, E-mail: {i[4]}, Endereço: {i[5]}, Sexo: {i[6]}, Salário: {i[7]}.")

print("=="*72)

con.commit()

con.close()