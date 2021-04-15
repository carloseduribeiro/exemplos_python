class Receita:

    # informacoes_receita = {"medicamento": str, "validade": date, "quantidade": int, "paciente": Paciente}
    def __init__(self, informacoes: dict):
        self.medicamento = informacoes["medicamento"]
        self.validade = informacoes["validade"]
        self.quantidade = informacoes["quantidade"]
        self.paciente = informacoes["paciente"]
