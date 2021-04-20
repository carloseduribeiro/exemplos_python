class CadastroError(Exception):
    pass


class CpfNaoExistente(CadastroError):
    pass


class CpfNaoNumerico(CadastroError):
    pass


class CpfTamanhoInvalido(CadastroError):
    pass


class EmailInvalido(CadastroError):
    pass


def verifica_cpf(cpf: str):
    if not len(cpf) == 11:
        raise CpfTamanhoInvalido

    # if cpf not in banco_dados:
    #     raise CpfNaoExistente

    if not cpf.isdigit():
        raise CpfNaoNumerico


cpf = input("Cpf: ")
# email = input("Email: ")

verifica_cpf(cpf)
