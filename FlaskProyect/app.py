
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="U41578780o"
app.config['MYSQL_DB']="dbflask"

mysql= MySQL(app)
#ruta para probar la conexion a la BD
@app.route('/DBcheck')
def DB_check(): 
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify({'status':'ok','message':'Conectado con exito'}), 200
    except MySQLdb.MySQLError as e:
        return jsonify({'status':'error','message': str(e)}), 500
        


#ruta simple
@app.route('/')
def home(): 
    return 'Hola mundo FLASK'

#ruta con parametros
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola ,'+nombre+'!!!' 

#ruta Try-Catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8 !!!', 404


#ruta doble
@app.route('/usuario')
@app.route('/usuaria')
def dobleroute():
    return 'Soy el mismo recurso del servidor'

#ruta POST
@app.route('/formulario', methods=['POST'])
def formulario():
    return 'Soy un formulario'

if __name__ == '__main__':
    app.run(port=3000, debug=True)