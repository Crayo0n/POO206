
from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="U41578780o"
app.config['MYSQL_DB']="dbflask"
app.secret_key='mysecretkey'

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
        

#ruta de inicio
@app.route('/')
def home(): 
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from Albums')
        consultaTodo=cursor.fetchall()
        return render_template('formulario.html',errores={},albums=consultaTodo)

    except Exception as e:
        print('Error en la consulta: '+e)
        return render_template('formulario.html',errores={},albums=[])

    finally:
        cursor.close()
        
#ruta de consulta
@app.route('/consulta')
def consulta(): 
    return render_template('consulta.html')

#ruta Try-Catch
@app.errorhandler(404)
def paginaNoE(e):
    return 'Cuidado: Error de capa 8 !!!', 404

#ruta Try-Catch
@app.errorhandler(405)
def errorPost(e):
    return 'Cuidado: Revisa el metodo utilizado !!!', 405

#ruta para el insert
@app.route('/guardarAlbum', methods=['POST'])
def guardar(): 
    errores={}
    #Obtener los datos a insestrar
    titulo= request.form.get('txtTitulo','').strip()
    artista= request.form.get('txtArtista','').strip()
    anio= request.form.get('txtAnio','').strip()


    if not titulo:
        errores['txtTitulo'] = 'Nombre del album obligatorio'
    if not artista:
        errores['txtArtista'] = 'Nombre del artista obligatorio'
    if not anio:
        errores['txtAno'] = 'Año del album obligatorio'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2030:
        errores['txtAno'] = 'En año solo ingresar un año valido'
        
    if not errores:
        #Intentamos Ejecutar el Insert
        try:
            cursor=mysql.connection.cursor()
            cursor.execute('insert into Albums (Titulo, Artista, Año) values (%s,%s,%s)',(titulo,artista,anio))
            mysql.connection.commit()
            flash('Album se guardo en la BD')
            return redirect(url_for('home'))
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Error: '+ str(e))
            return redirect(url_for('home'))
    
        finally:    
            cursor.close()
    
    return render_template('formulario.html', errores = errores)
    

if __name__ == '__main__':
    app.run(port=3000, debug=True)