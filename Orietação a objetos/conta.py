class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo de {} do titular {} e limite para saque de {}'.format(self.__saldo, self.__titular, (self.__saldo + self.__limite)))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} para saque é maior que o seu limite para saque de {(self.__saldo + self.__limite)}.' )

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    #importante: o get sempre retorna um atributo enquanto o set sempre altera um a tributo
    #Exemplos
    #def get_saldo(self):
        #return self.__saldo

    #def get_titular(self):
        #return self.__titular

    #def get_limite(self):
        #return self.__limite

    #def set_limite(self, limite):
        #self.__limite = limite

    #Boas praticas sobre get/set é o uso do @property(pra get) e @atributo.setter(para get)

    @property
    def saldo(self):
        print(self.__saldo)
        return self.__saldo
    @property
    def titular(self):
        print(self.__titular)
        return self.__titular
    @property
    def limite(self):
        print(self.__limite)
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        print(self.__limite)

    @staticmethod
    def codigo_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}








# A convenção em pyhton para acessar valores utilizando sempre a classe é utilizar (__) seguindo o modelo self.__numero = numero
# O objetivo é deixar uma mensagem para todos os dessenvolvedores que esses objetdos não devem ser alterados diretamente usando conta.saldo = 60
# Mas sim utilizando as classe, alterando diretamente o saldo fazendo conta = Conta(numero, titular, saldo_alterando, limite).





