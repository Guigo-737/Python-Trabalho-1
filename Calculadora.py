def exibir_menu():
    print("\n=== CALCULADORA SIMPLES ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")


while True:
    exibir_menu()
    escolha = input("Escolha uma opção (1-5): ").strip()

    if not escolha:
        print("inválido: Digite um número entre 1 e 5.")
        continue
    if escolha not in ["1", "2", "3", "4", "5"]:
        print("Inválido: Tente novamente.")
        continue

    if escolha == "5":
        print("Saindo")
        break  
    try:
        num1 = float(input("Digite um número: ").strip())
        num2 = float(input("Digite outro número: ").strip())
    except ValueError:
        print("Números inválidos")
        continue

    if escolha == "1":
        resultado = num1 + num2
        print(f" Resultado: {num1} + {num2} = {resultado}")
    elif escolha == "2":
        resultado = num1 - num2
        print(f" Resultado: {num1} - {num2} = {resultado}")
    elif escolha == "3":
        resultado = num1 * num2
        print(f" Resultado: {num1} × {num2} = {resultado}")
    elif escolha == "4":
        if num2 == 0:
            print(" Erro: divisão por zero não é permitida!")
            continue
        resultado = num1 / num2
        print(f" Resultado: {num1} ÷ {num2} = {resultado}")