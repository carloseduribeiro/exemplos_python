from Classes.Farmaceutico import Farmaceutico

class Receita:

    # informacoes_receita = {"medicamento": str, "validade": date, "quantidade": int, "paciente": Paciente}
    def __init__(self, informacoes: dict):
        self.medicamento = informacoes["medicamento"]
        self.validade = informacoes["validade"]
        self.quantidade = informacoes["quantidade"]
        self.paciente = informacoes["paciente"]
        self.__medicamento_entregue = False
        self.farmaceutico = Farmaceutico

    def medicamento_entregue(self) -> bool:
        return self.__medicamento_entregue

    def definir_como_entregue(self, farmaceutico: Farmaceutico):
        self.__medicamento_entregue = True
        self.farmaceutico = farmaceutico
