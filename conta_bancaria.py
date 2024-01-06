menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
aux = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
     opcao = input(menu)

     if opcao == "d":
         aux = float(input("Digite o valor a ser depositado: "))

         if aux <= 0:
             print("Valor inválido, digite um um número maior que zero!")
         else:
             saldo += aux
             extrato += f"Depósito: R$ {aux:.2f}\n"

     elif opcao == "s":

         if numero_saques < LIMITE_SAQUES:  
             aux1 = float(input("Digite o valor a ser sacado: ")) 
             if aux1 <= limite:
                 if aux1 <= saldo:
                     saldo -= aux1
                     print("Sacado com sucesso!")
                     numero_saques += 1
                     extrato += f"Saque: R$ {aux1:.2f}\n" 
                 else:
                    print("Saldo insuficiente!") 
             else:
                 print("Seu limite é insuficiente!")
         else:
             print("Limite de saques atingido no dia!")   
            

 
     elif opcao == "e":
           
            print("\n================================== EXTRATO ==================================")
            print("\nNão foram realizaados movimentações na conta!" if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}" )
            print("================================================================================")

     elif opcao == "q":
        break
     else:
        print("Opção inválida! Por favor escolha novamente a operação desejada.")
     