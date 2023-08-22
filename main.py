from banco import*
from operacoes.transferencia import transferir
from operacoes.saque import sacar
from operacoes.consulta import consultarSaldo
from operacoes.consulta import obterConta
from operacoes.deposito import depositar

def menu():
 while True:
    print("____BEM VINDO AO BANCO INFINITY -------")
    print("1 - Adicionar conta")
    print("2 - Alterar nome")
    print("3 - Consultar contas")
    print("4 - Remover conta")
    print("5 - listar contas")
    print("6 - Realizar saque")
    print("7 - Realizar deposito")
    print("8 - Consultar saldo")
    print("9 - realizar transferencia")
    print("10 - Sair")
    opcao = int(input('Selecione uma opção:'))

    if opcao == 1:
        nome = input ('Digite o nome do cliente:')
        saldo = float(input('Digite o saldo do cliente:'))
        adicionarConta(nome, saldo)

    elif opcao == 2:
        conta = int(input('Digite o numero da conta:'))
        nome = input('Digite o novo nome:')
        atualizarNome(conta, nome)
    elif opcao ==3:
        conta = int(input('Digite o numero da conta'))
        print(obterConta(conta))

    elif opcao == 4:
        conta = int(input('Digite o numero da conta'))
        print(deletarConta(conta))

    elif opcao == 5:
        listarContas()

    elif opcao == 6:
        conta = int(input('Digite o numero da conta'))
        valor = float(input('Digite o valor que deseja sacar'))
        sacar(conta,valor)

    elif opcao == 7:
        conta = int(input('Digite o numero da conta'))
        valor = float(input('Digite o valor que deseja depositar'))
        depositar(conta, valor)

    elif opcao == 8:
        conta = int(input('Digite o numero da conta'))
        consultarSaldo(conta)

    elif opcao == 9:
        contaOrigem = int(input('Inforte a conta de origem:'))
        contaDestino = int(input('Inforte a conta de destino:'))
        valor = float(input('Informe o valor:'))
        transferir(contaOrigem,contaDestino,valor)

    elif opcao == 10:
        print('Você saiu do sistema!')
        break
    else:
        print('Opção inválda')

menu()