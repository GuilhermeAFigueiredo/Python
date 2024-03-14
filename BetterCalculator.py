def adição(x, y):
    return x + y

def subtração(x, y):
    return x - y

def multiplicação(x, y):
    return x * y

def divisão(x, y):
    if y == 0:
        return "Não se pode dividir por 0."
    else:
        return x / y

def obter_input():
    while True:
        escolha = input("Digite = (1/2/3/4) para selecionar: ")
        if escolha.isdigit() and int(escolha) in [1, 2, 3, 4]:
            return int(escolha)
        else:
            print("Opção inválida")

def calcular(operacao, x, y):
    operacoes = {
        1: adição,
        2: subtração,
        3: multiplicação,
        4: divisão
    }
    return operacoes[operacao](x, y)

if __name__ == "__main__":
    print("Olá, bem vindo a minha calculadora, selecione a operação que deseja realizar:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    operacao = obter_input()

    x = float(input("Digite o operador 1: "))
    y = float(input("Digite o operador 2: "))

    resultado = calcular(operacao, x, y)
    print(resultado)
    print("Obrigado por usar a calculadora")
