from conta import Conta
from tipo_transferencia import Tipo
import util

def transferencia(emissor, receptor, tipo, valor):

    if emissor.get_numero() == receptor.get_numero() and emissor.get_agencia() == receptor.get_agencia():
        print('Sua transferência não foi completada pois não são permitidas transferências para a mesma conta.')
        return
    if tipo == Tipo.PIX and valor > 5000.00:
        print('Sua transferência não foi completada pois o limite de uma tranferência PIX é de $ 5 mil.')
        return
    elif tipo == Tipo.DOC and valor <= 10000.00:
        print('Sua transferência não foi completada pois o limite de transferência via DOC é acima $ 10 mil.')
        return
    elif tipo == Tipo.TED and not (valor > 5000 and valor <= 10000.00):
        print('Sua transferências via TED não foi completada pois são para valores acima de R$ 5 mil e até R$ 10 mil.')
        return

    emissor.set_valor_em_conta(emissor.get_valor_em_conta() - valor)
    receptor.set_valor_em_conta(receptor.get_valor_em_conta() + valor)

    print('Sua transferência foi realizada com sucesso!')
    print(f'Saldo do emissor: R$ {emissor.get_valor_em_conta():.2f}')
    print(f'Saldo do receptor: R$ {receptor.get_valor_em_conta():.2f}')

if __name__=="__main__":
    values = util.carregarVariaveis()

    emissor = Conta(agencia=values['agencia_emissor'], numero=values['conta_emissor'], cpf_titular=values['cpf_emissor'], nome_titular=values['nome_emissor'])
    receptor = Conta(agencia=values['agencia_receptor'], numero=values['conta_receptor'], cpf_titular=values['cpf_receptor'], nome_titular=values['nome_receptor'])

    transferencia(emissor, receptor, Tipo[values['tipo_transferencia']],  float(values['valor_transferencia']))


