class Paciente:

    def __init__(self, nome: str, cpf: str, idade: int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        # self.receita = receita

    def __eq__(self, other) -> bool:
        if self.cpf == other.cpf and self.nome == other.nome:
            return True
        else:
            return False
