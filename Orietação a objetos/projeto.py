from conta import Conta
def criar_conta(numero, titular, saldo, limite):
    conta = {'número': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

#def deposita(conta, valor):
 #   conta['saldo'] += valor
 #   return conta

#def saque(conta,valor):
    conta['saldo'] -= valor

#def extrado(conta):
#    print('O saldo da conta é: {}'.format(conta['saldo']))

conta = Conta(555,'Gio', 10000, 50000)

conta.limite

