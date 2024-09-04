menu = """
================================================
    BEM-VINDO(A) AO MENU DO SISTEMA BANCÁRIO
================================================
Escolha uma das opções:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair do Menu

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

     opcao = input(menu)

     if opcao == "1":
          dinheiro = float(input("O quanto você deseja depositar? R$"))

          if dinheiro > 0:
             dinheiro += saldo # adiciona o valor no saldo
             extrato += f"Seus R${dinheiro:.f} foram depositados!"

          else:
               print("O valor informado é inválido.") # caso o valor seja negativo

     elif opcao == "2":
          dinheiro = float(input("O quanto você deseja sacar? R$"))

          exce_saldo = dinheiro > saldo # ver se eh maior q o saldo
          exce_limite = dinheiro > limite # ver se eh maior q o limite
          exce_saque = numero_saques >= LIMITE_SAQUES # se é maior que o limite, q é 3

          if exce_saldo:
               print("Você não tem saldo suficiente.")
          elif exce_limite:
               print("Você excedeu o limite de valor do saque.")
          elif exce_saque:
               print("Você excedeu o limite de saques diários.")
          elif dinheiro > 0: # verificando se o valor é maior que 0, ou seja se não é negativo
               saldo -= dinheiro # retirando o valor da conta
               extrato += f"Obteve o saque de: R${dinheiro:.f}"
               numero_saques += 1 # contabilizando os saques

          else:
               print("O valor informado é inválido.") # caso o valor seja negativo

     elif opcao == "3":

          print("\n================== EXTRATO =======================")
          print("Não houve nenhum registro de extratos." if not extrato else extrato)
          print(f"\nSaldo atual: R${saldo:.f} ")
          print("\n==================================================")

     elif opcao == "4":
          print("Você saiu do Menu do Sistema Bancário.")
          break

     else:
          print("Operação inválida. Escolha a opção desejada novamente.") # qnd n é nenhuma operação do menu