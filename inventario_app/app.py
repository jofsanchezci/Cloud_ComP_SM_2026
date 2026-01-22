from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, emit
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

DB_PATH = 'inventario.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS inventario (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        cantidad_actual INTEGER NOT NULL,
                        precio REAL NOT NULL,
                        cantidad_futura INTEGER DEFAULT 0
                    )''')
        conn.commit()

def obtener_productos():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, nombre, cantidad_actual, precio, cantidad_futura, precio*1.19 as precio_iva FROM inventario")
    productos = c.fetchall()
    conn.close()
    return productos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventario')
def inventario():
    return jsonify(obtener_productos())

@app.route('/agregar', methods=['POST'])
def agregar():
    data = request.form
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''INSERT INTO inventario (nombre, cantidad_actual, precio, cantidad_futura) 
                     VALUES (?, ?, ?, ?)''',
                  (data['nombre'], data['cantidad_actual'], data['precio'], data['cantidad_futura']))
        conn.commit()
    socketio.emit('actualizar_inventario')
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        data = request.form
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute('''UPDATE inventario 
                         SET nombre=?, cantidad_actual=?, precio=?, cantidad_futura=?
                         WHERE id=?''',
                      (data['nombre'], data['cantidad_actual'], data['precio'], data['cantidad_futura'], id))
            conn.commit()
        socketio.emit('actualizar_inventario')
        return redirect(url_for('index'))
    else:
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM inventario WHERE id=?', (id,))
            producto = c.fetchone()
        return render_template('editar.html', producto=producto)

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('DELETE FROM inventario WHERE id=?', (id,))
        conn.commit()
    socketio.emit('actualizar_inventario')
    return redirect(url_for('index'))

@app.route('/cargar_masiva', methods=['POST'])
def cargar_masiva():
    archivo = request.files['archivo']
    if archivo and archivo.filename.endswith('.txt'):
        contenido = archivo.read().decode('utf-8').splitlines()
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            for linea in contenido:
                if linea.strip() == '' or linea.startswith("ID"):
                    continue
                id_, nombre, cant_act, precio, cant_fut = linea.split(',')
                c.execute('''INSERT OR REPLACE INTO inventario (id, nombre, cantidad_actual, precio, cantidad_futura)
                             VALUES (?, ?, ?, ?, ?)''',
                          (int(id_), nombre, int(cant_act), float(precio), int(cant_fut)))
            conn.commit()
        socketio.emit('actualizar_inventario')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    socketio.run(app, debug=True)
