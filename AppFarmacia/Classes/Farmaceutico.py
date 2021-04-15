from Classes.Receita import Receita
from Classes.Paciente import Paciente
from datetime import date


class Farmaceutico:

    def __init__(self, nome: str):
        self.nome = nome

    def receber_receita(self, receita: Receita, cliente: Paciente):
        self.cliente = cliente
        self.receita = receita

    # Retorna True se a receita for válida:
    def validar_receita(self) -> bool:
        validade = self.receita.validade.split("/")

        # inverte a string de dd-mm-YYYY para YYYY-mm-dd
        if len(validade[0]) == 2:
            print(validade.reverse())
        ano = int(validade[0])
        mes = int(validade[1])
        dia = int(validade[2])

        validacoes = list()
        validacoes.append(self.cliente == self.receita.paciente)    # Verifica se o paciente é o dono da receita
        validacoes.append(date(ano, mes, dia) >= date.today())      # Verifica a validade
        validacoes.append(self.cliente.idade >= 18)                 # Verifica se ele é maior de idade
        return all(validacoes)

    # Verifica se a quantidade do medicamento existe no estoque:
    def verificar_estoque(self) -> bool:
        if not self.validar_receita():
            return False

        nome = ''
        quantidade = 0

        with open("../dados/estoque.txt") as estoque:
            for line in estoque:
                medicamento = line.split(';')
                # Verifica se
                if medicamento[1] == self.receita.medicamento:
                    nome = medicamento[1]
                    quantidade = int(medicamento[3].strip())
                    break

        if len(nome) > 0 and quantidade >= self.receita.quantidade:
            return True
        else:
            return False

    # Retira o medicamento
    def retirar_medicamento(self) -> bool:
        if not self.verificar_estoque():
            return False

        medicamento_entregue = False

        dados_modificados = []
        with open("../dados/estoque.txt") as estoque:
            for line in estoque:
                medicamento = line.split(';')
                # Verifica se o medicamento está na lista
                if medicamento[1] == self.receita.medicamento:
                    quantidade = int(medicamento[3].strip())
                    # Subtrai a quantidade escrita na receita do estoque:
                    medicamento[3] = str(quantidade - self.receita.quantidade) + '\n'
                    medicamento_entregue = True
                    self.receita.definir_como_entregue(self)
                dados_modificados.append(';'.join(medicamento))

        with open("../dados/estoque.txt", "w") as estoque:
            estoque.writelines(dados_modificados)

        return medicamento_entregue

    def entregar_medicamento(self):
        if self.receita.medicamento_entregue():
            print("Medicamento entregue!")
        else:
            print("medicamento não entregue!")
