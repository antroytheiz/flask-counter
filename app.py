from flask import Flask, render_template, request, redirect, session, url_for
from flask_ipinfo import IPInfo
from datetime import datetime
import mysql.connector
import os

app = Flask(__name__)
ipinfo = IPInfo()


# app = Flask(__name__)
# app.config['DB_USER'] = 'theis'
# app.config['DB_PASSWORD'] = 'salupa'
# app.config['DB_DATABASE'] = 'flaskcounter'
# app.config['DB_HOST'] = 'localhost'

# conn = cursor = None

# def open():
#     global conn, cursor
#     conn = mysql.connector.connect(
#         user = app.config['DB_USER'],
#         password = app.config['DB_PASSWORD'],
#         database = app.config['DB_DATABASE'],
#         host = app.config['DB_HOST']
#     )
#     cursor = conn.cursor()

# def close():
#     global conn, cursor
#     cursor.close()
#     conn.close()


@app.route('/')
def index():
    if not session.get('count'):
        session['count'] = 0
    session['count'] += 1
    date = datetime.now()
    ipadd = ipinfo.ipaddress
    return render_template('index.html',date=date, ipadd=ipadd)

@app.route('/add2', methods=['POST'])
def add_two():
    session['count'] += 0
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

# @app.route('/')
# def table():
#     global data
#     open()
#     cursor.execute('SELECT * FROM userCounter')
#     data = []
#     for id,ipadd in cursor.fetchall():
#         data.append((id,ipadd))
#     close()
#     return render_template('index.html')

# @app.route('/tambah', methods=['GET','POST'])
# def tambah():
#     if request.method == 'POST':
#         # id = request.form['id']
#         nama = request.form['nama']
#         jurusan = request.form['jurusan']
#         open()
#         cursor.execute("INSERT INTO userCounter (nama,jurusan) VALUES(%s,%s)", (nama,jurusan))
#         conn.commit()
#         close()
#         return redirect(url_for('index'))
#     else:
#         close()
#         return render_template('tambah_data.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True) # run our server