"""
Calculadora simples para estimar valores cobrados pela maquineta.
"""

print("Bem vindo(a) a Calculadora: Digite o valor que deseja receber ou -1 para SAIR.")
while 0 == 0: #Laço infinito para fazer varias simulações.

    num = input("Valor a ser recebido: ") #Entrada do número pelo usuário
    num2 = float(num.replace(",",".")) # Substituição da virgula pelo ponto para evitar erro de leitura.
    if num2 == -1: # Condição para encerrar o programa.
       print("Obrigado por usar nossa Caculadora! Volte Sempre.")
       break

    rot = (num2) / 0.95 # Pagamento Rotativo
    print(f"O valor a ser cobrado no credito rotativo é: R${rot:.2f}")

    x2 = (num2) / 0.9009 # Pagamento em 2x
    print(f"O valor a ser cobrado no credito em 2X é: R${x2:.2f}")

    x3 = (num2) / 0.8871 # Pagamento em 3x
    print(f"O valor a ser cobrado no credito em 3X é: R${x3:.2f}")
