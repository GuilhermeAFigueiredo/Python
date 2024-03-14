import sys
class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

def cadastrar_funcionario(funcionarios):
    nome = input("Nome do funcionário: ")
    idade = int(input("Idade do funcionário: "))

    while True:
        try:
            salario = int(input("Salário do funcionário: "))
            break
        except ValueError:
            print("Entrada inválida. Insira um número inteiro válido.")

    funcionario = Funcionario(nome, idade, salario)
    funcionarios.append(funcionario)

    print("Funcionário cadastrado com sucesso.")

def listar_funcionarios(funcionarios):
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return

    print("\nListagem de funcionários:\n")
    for i, funcionario in enumerate(funcionarios, 1):
        print(f"Funcionário {i}:\n")
        print(f"Nome: {funcionario.nome}\n")
        print(f"Idade: {funcionario.idade}\n")
        print(f"Salário: {funcionario.salario}\n")

def main():
    funcionarios = []

    while True:
        print("\nMenu:\n")
        print("1. Cadastrar funcionário\n")
        print("2. Listar funcionários\n")
        print("3. Sair\n")
