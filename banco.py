def depositar(valor):
  
  if valor <= 0:
    print("O valor do depósito deve ser maior que zero.")
    print(f'Saldo: R$ ${saldo}')
    return saldo
  else:
    novoSaldo = valor + saldo
    valor = str(valor)
    extrato.append(f"Depósito: R$ {valor}")
    print(f'Saldo: R$ ${novoSaldo}')
    return novoSaldo
  

menu =  """

    [d] Depositar
    [s] Sacar 
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Digite o valor do depósito: "))
        saldo = depositar(valor)
    
    elif opcao == 's':
        valor = float(input("Digite o valor que deseja sacar: "))
        if valor <= 0:
            print("O valor do depósito deve ser maior que zero.")
            print(f'Saldo: R$ ${saldo}')
        if valor > 500:
            print("O valor do saque ultrapassa o limite de R$ 500,00 reais .")
            print(f'Saldo: R$ ${saldo}')
        elif valor > saldo:
            print("Saldo insuficiente.")
            print(f'Saldo: R$ ${saldo}')
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários atingido.")
            print(f'Saldo: R$ ${saldo}')
        else:
            saldo = saldo - valor
            valor = str(valor)
            extrato.append("Saque: " + "R$" + valor)
            print(f'Saldo: R$ ${saldo}')
            numero_saques += 1
                
    elif opcao == 'e':
        print('Não foram realizadas movimentações') if not extrato else [print(i) for i in extrato]
        print(f'Saldo Final: R$ ${saldo}')
    
    elif opcao == 'q':
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")