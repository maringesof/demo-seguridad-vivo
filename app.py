from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/usuario")
def usuario():
    nombre = request.args.get("nombre")
    conn = sqlite3.connect("db.sqlite")
    consulta = f"SELECT * FROM usuarios WHERE nombre = '{nombre}'"
    return str(conn.execute(consulta).fetchall())
