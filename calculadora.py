print("=== Calculadora Teste ===")

num_operacoes = int(input("Quantas operações você quer realizar? "))

for i in range(num_operacoes):
    print(f"\nOperação {i+1} de {num_operacoes}")
    num1 = float(input("Digite o 1 número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o 2 número: "))
  
   if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro!"
    else:
        resultado = "Digite novamente!!!"
    
    print(f"Resultado: {resultado}")
