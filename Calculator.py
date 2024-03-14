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

print("Olá, bem vindo a minha calculadora, selecione a operação que deseja realizar:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite = (1/2/3/4) para selecionar: ")

num1 = float(input("Digite o operador 1: "))
num2 = float(input("Digite o operador 2: "))

if escolha == '1':
    print(num1, "+", num2, "=", adição(num1, num2))
    print("Obrigado por usar a calculadora")
elif escolha == '2':
    print(num1, "-", num2, "=", subtração(num1, num2))
    print("Obrigado por usar a calculadora")
elif escolha == '3':
    print(num1, "*", num2, "=", multiplicação(num1, num2))
    print("Obrigado por usar a calculadora")
elif escolha == '4':
    print(num1, "/", num2, "=", divisão(num1, num2))
    print("Obrigado por usar a calculadora")
else:
    print("Opção inválida")
    
