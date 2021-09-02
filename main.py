"""
Projeto simples para calcular os juros da venda na maquineta de cartão de crédito.
"""
import time
from colorama import init, Fore, Style

init()


def calc(valor):
    try:  # Tratamento de erro caso o usuario entre com letras.
        valor = float(num.replace(",", "."))  # Substituição de possiveis virgulas pelo ponto.
        if valor < 0:  # Condicional para não calcularmos valores negativos
            print(Fore.RED + "O valor informado é negativo, favor informar um valor positivo ou 'Sair' para fechar.")
            print(Style.RESET_ALL)
        else:
            rotativo = valor / 0.95  # Pagamento Rotativo
            print(f"O valor a ser cobrado no credito rotativo é:" + Fore.GREEN + f"R${rotativo:.2f}")
            print(Style.RESET_ALL)

            parceladox2 = valor / 0.9009  # Pagamento em 2x
            print(f"O valor a ser cobrado no credito em 2X é:" + Fore.GREEN + f"R${parceladox2:.2f}")
            print(Style.RESET_ALL)

            parceladox3 = valor / 0.8871  # Pagamento em 3x
            print(f"O valor a ser cobrado no credito em 3X é:" + Fore.GREEN + f"R${parceladox3:.2f}")
            print(Style.RESET_ALL)

    except ValueError:  # Tratamento de erro, caso seja digitado letras no lugar de números
        print(Fore.RED + "É necessário informar um número para continuar ou 'Sair' para fechar.")
        print(Style.RESET_ALL)


print(Fore.GREEN + 'Para começar digite o valor que você quer receber e o programa calculará quanto deverá\nser'
      ' cobrado para cada tipo de pagamento, digite "Sair" para fechar o programa.')
print(Style.RESET_ALL)

while 0 == 0:  # Laço infinito para que o usuario possa fazer diversas simulações seguidas
    num = input("Valor a ser recebido: R$ ")

    if num == "Sair" or num == "sair" or num == "SAIR":  # Digite Sair para encerrar o programa.
        print("Obrigado por usar nossa calculadora.")
        time.sleep(3)
        break
    else:
        calc(num)
