
class Conta:
    def __init__(self, agencia, numero, cpf_titular, nome_titular, valor_em_conta=0):
        self._agencia = agencia
        self._numero = numero
        self._cpf_titular = cpf_titular
        self._nome_titular = nome_titular
        self._valor_em_conta = valor_em_conta

    def get_agencia(self):
        return self._agencia

    def get_numero(self):
        return self._numero

    def get_cpf_titular(self):
        return self._cpf_titular

    def get_nome_titular(self):
        return self._nome_titular

    def get_valor_em_conta(self):
        return self._valor_em_conta

    def set_valor_em_conta(self, novo_valor):
        self._valor_em_conta = novo_valor
