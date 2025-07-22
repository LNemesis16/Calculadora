import os
import time

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Função de calculadora que realiza operações com dois números.
    Retorna 'nan' se a operação não for válida.
    """
    result = float("nan")

    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        if num2 != 0:
            result = num1 / num2
    elif operador == '**':
        result = num1 ** num2

    return result


if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print('Calculadora')
        print('----------------------------------\n')

        try:
            # Pedir os dois números
            num1 = float(input("Digite o primeiro número: "))
            operador = input("Escolha a operação (+, -, *, /, **): ")
            num2 = float(input("Digite o segundo número: "))

            # Calcular e apresentar resultado
            resultado = calculadora(num1, num2, operador)

            if str(resultado) == 'nan':
                print("\nOperação inválida ou divisão por zero!")
            else:
                print(f"\nResultado: {num1} {operador} {num2} = {resultado}")

        except ValueError:
            print('\nDados inválidos! -> Tente novamente.')
        except ZeroDivisionError:
            print('\nImpossível dividir por zero! -> Tente novamente.')

        # Perguntar se o utilizador quer continuar
        continuar = input("\nDeseja fazer outra operação? (s/n): ").lower()
        if continuar != 's':
            print('\nVolte sempre!\n')
            break

        time.sleep(2)