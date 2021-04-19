from MySQLdb import _exceptions as MySQLExceptions
from MySQLdb import connect


class Banco:

    def __init__(self, db: str, host: str, port: int, user: str, passwd=''):
        # Informações para a conexão com o bando de dados:
        self.db = db
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd

    def conectar(self) -> tuple[bool, str]:
        # Retorna o resultado da operação e uma mensagem dentro de uma tupla
        try:
            # Cria a conexão com o bd:
            self.conn = connect(db=self.db, host=self.host, port=self.port, user=self.user, passwd=self.passwd)
            return True, "Conexão bem sucedida!"
        except MySQLExceptions.OperationalError:
            return False, "Erro ao tentar conectar com o banco de dados."


    def pegar_colunas_valores(self, **colsrows):
        # Monta a lista de colunas da tabela na query:
        cols = "("
        columns = tuple(colsrows.keys())
        for i in range(len(columns)):
            cols += f"{columns[i]}"
            cols += ")" if i + 1 == len(columns) else ', '

        # Monta a lista de valores:
        vals = "("
        values = tuple(colsrows.values())
        for i in range(len(values)):
            # Se for um campo numérico ele precisa ir sem as "
            if isinstance(values[i], int) or isinstance(values[i], float):
                vals += f"{values[i]}"
            else:
                vals += f"'{values[i]}'"
            vals += ")" if i + 1 == len(values) else ", "
        return cols, vals

    def insert(self, tabela: str, **colsrows):
        # Recebe o nome da tabela e as colunas com seus valores.
        # Exempo: insert("tabela", nome="Carlos", cpf="02340324802", ...)
        query = f"INSERT INTO {tabela} ("

        # Monta a lista de colunas da tabela no sql:
        columns = tuple(colsrows.keys())
        for i in range(len(columns)):
            query += f"{columns[i]}"
            query += ")" if i + 1 == len(columns) else ', '

        query += " VALUES ("
        # Concatena '?' para os valores: (isso evita SQL Injection)
        for i in range(len(colsrows.values())):
            # Se for um campo numérico ele precisa ir sem as "
            query += "%s"
            query += ");" if i + 1 == len(colsrows.values()) else ", "
        values = tuple(colsrows.values())

        cursor = self.conn.cursor()
        try:
            result = cursor.execute(query, values)
            self.conn.commit()
            return result
        except MySQLExceptions.OperationalError as error:
            print("Erro ao inserir dados!\nMensagem: " + error.args[1])
        except MySQLExceptions.IntegrityError as error:
            print("Erro ao inserir dados!\nMensagem: " + error.args[1])

    def get_all(self, tabela: str, *columns):
        # Monta o SQL:
        if len(columns) == 0:
            # Se o usuário informar as colunas ele busca todas as informações da tabela.
            query = f"SELECT * FROM {tabela}"
        else:
            # Monta o nome das colunas informadas no select:
            query = "SELECT "
            for i in range(len(columns)):
                query += f"{columns[i]}"
                query += " " if i+1 == len(columns) else ', '
            query += f"FROM {tabela};"

        # Faz a consulta e imprime o resultado:
        cursor = self.conn.cursor()
        cursor.execute(query)

        # Imprime o cabeçalho:
        coluna = [i[0].capitalize() for i in cursor.description]
        linha = ''
        for i in range(len(coluna)):
            linha += coluna[i] + ' '*(15-len(coluna[i]))
        print(linha)
        print('=' * len(linha))
        # Imprime os dados:
        for reg in cursor.fetchall():
            linha = ''
            for i in range(len(reg)):
                reg_str = str(reg[i])
                linha += reg_str + ' '*(15-len(str(reg[i])))
            print(linha)

    def delete(self, tabela: str, **where_condicoes):
        query = f"DELETE FROM {tabela} WHERE "

        # for campo, valor in where_condicoes.items():
        #     query += f"{campo} == {valor}"


bd = Banco("testes", "localhost", 3306, "root")
bd.conectar()

# bd.insert("tabela_teste", nome="Alek", cpf="98759875987")
# bd.insert("tabela_teste", nome="Fumaça", cpf="623456548978")
# bd.insert('tabela_teste', nome="Blablaba", cpf="045898784875")


bd.delete("testes", nome="Carlos")
bd.get_all("tabela_teste")
