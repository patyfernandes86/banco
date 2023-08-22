from banco import obterConta,banco

def transferir(contaori: int, contaDes: int, valor: float) -> None:
    contaOrigem = obterConta(contaori)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
           contaOrigem['saldo'] -= valor
           contaOrigem['saldo'] += valor
           print ('Transferencia realizada com sucesso!')
        else:
         print('Saldo insuficiente na conta de origem' )
    else:
        print('Uma ou mais contas não existem')

if __name__=="__main__":
    transferir(1,2,1500)
    print(banco)