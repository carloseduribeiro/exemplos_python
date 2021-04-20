class Error(Exception):
    pass


class SalarioAbaixoDoEsperado(Error):

    def __init__(self, salario):
        if salario < 2000:
            restante = 2000 - salario
            mensagem = "Seu salário está diferente do esperado!\n" \
                       f"Ainda faltam R${salario}"
            super().__init__(mensagem, salario)


try:
    raise SalarioAbaixoDoEsperado(1000)
except Exception as error:
    print(error.args)
