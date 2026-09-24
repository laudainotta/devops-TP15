import os
import psycopg2
from flask import Flask, request

app = Flask(__name__)


@app.route('/andon/eval')
def andon_eval():
    return str(eval(request.args.get('expr')))


@app.route('/andon/cmd')
def andon_cmd():
    os.system('ping -c 1 ' + request.args.get('host'))
    return 'ok'


@app.route('/andon/sql')
def andon_sql():
    conn = psycopg2.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes WHERE title = '" + request.args.get('t') + "'")
    return str(cur.fetchall())
