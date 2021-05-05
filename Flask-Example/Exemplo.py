from flask import Flask, request, render_template
import MySQLdb
import json
import pandas as pd

app = Flask(__name__)

conn = MySQLdb.connect(host="localhost", user="root", passwd="1996", db="llamaaqu_master")
conn.autocommit(True)
cursor = conn.cursor()


@app.route("/read", methods=["GET"])
@app.route("/read/<int:id_reg>", methods=["GET"])
def read(id_reg=None):
    sql = "SELECT * FROM teste"
    if id_reg:
        sql += f" where id = {id_reg}"

    try:
        result_rows = cursor.execute(sql)
        if result_rows > 0:
            columns = [i[0] for i in cursor.description]
            df = pd.DataFrame(cursor.fetchall(), columns=columns)
            result = df.to_json(orient="records")
            # result = json.dumps(dict(cursor.fetchall()))
            return result
    except Exception as error:
        return str(error.args)

    return "Algo deu errado!", 400


@app.route("/update", methods=["PUT"])
@app.route("/update/<int:id_reg>", methods=["PUT"])
def update(id_reg=None):
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    sql = f"UPDATE FROM teste WHERE id = "
    sql += f"{id_reg}" if isinstance(id_reg, int) else f"{dict_values['id']}"

    try:
        affected_rows = cursor.execute(sql)
        if affected_rows > 0:
            return "Deu tudo certo", 200
    except Exception as error:
        return str(error.args)

    return "Algo deu errado!", 400


@app.route("/save", methods=["POST"])
def save():
    raw_request = request.data.decode("utf-8")
    dict_values = json.loads(raw_request)

    # Monta o SQL de inserção:
    sql = f"INSERT INTO teste VALUES (default, '{dict_values['nome']}', " \
          f"'{dict_values['idade']}', '{dict_values['animal']}')"

    try:
        # Executa o comando SQL e armazena o número de registros inseridos:
        affected_rows = cursor.execute(sql)
        if affected_rows > 0:
            return "Deu tudo certo!", 200
    except Exception as error:
        return str(error.args)

    return "Algo deu errado!", 400


@app.route("/delete/<int:id_reg>", methods=["DELETE"])
def delete(id_reg: int):
    sql = f"DELETE FROM teste WHERE id = {id_reg}"
    try:
        affected_rows = cursor.execute(sql)
        if affected_rows > 0:
            return "Apagou show!", 200
    except Exception as error:
        return str(error.args)

    return "Algo deu errado!", 400


if __name__ == "__main__":
    app.run(debug=True)
