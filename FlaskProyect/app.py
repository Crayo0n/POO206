
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
        cursor.execute('select * from Albums where estatus = 1')
        consultaTodo=cursor.fetchall()
        return render_template('formulario.html',errores={},albums=consultaTodo)

    except Exception as e:
        print('Error en la consulta: '+e)
        return render_template('formulario.html',errores={},albums=[])

    finally:
        cursor.close()


@app.route('/detalles/<int:id>')
def detalle(id):
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from Albums where id= %s',((id),))
        consultaID=cursor.fetchone()
        return render_template ('consulta.html', errores={},album=consultaID)
    
    except Exception as e:
        print('Error al consultar por ID '+e)
        return redirect (url_for('home'))
    
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
        errores['txtAnio'] = 'Año del album obligatorio'
    elif not anio.isdigit() or int(anio) < 1800 or int(anio) > 2030:
        errores['txtAnio'] = 'En año solo ingresar un año valido'
        
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

@app.route('/actualizar/<int:id>', methods=['GET'])
def mostrar_actualizar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('select * from Albums where id = %s', (id,))
        album = cursor.fetchone()  # Obtener los datos del álbum
        if album:
            return render_template('formUpdate.html', album=album, errores={})
        else:
            flash('Álbum no encontrado')
            return redirect(url_for('home'))
    except Exception as e:
        flash(f'Error al cargar los datos del álbum: {e}')
        return redirect(url_for('home'))
    finally:
        cursor.close()


# ruta para actualizar
@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    errores = {}
    tituloA = request.form.get('txtTituloA', '').strip()
    artistaA = request.form.get('txtArtistaA', '').strip()
    anioA = request.form.get('txtAnioA', '').strip()

    if not tituloA:
        errores['txtTituloA'] = 'Nombre del album obligatorio'
    if not artistaA:
        errores['txtArtistaA'] = 'Nombre del artista obligatorio'
    if not anioA:
        errores['txtAnioA'] = 'Año del album obligatorio'
    elif not anioA.isdigit() or int(anioA) < 1800 or int(anioA) > 2030:
        errores['txtAnioA'] = 'En año solo ingresar un año valido'

    if not errores:
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('update Albums set Titulo=%s, Artista=%s, Año=%s where id=%s',(tituloA, artistaA, anioA, id))
            mysql.connection.commit()
            flash('Album se actualizó correctamente')
            return redirect(url_for('home'))
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Error: ' + str(e))
            return redirect(url_for('home'))
        
        finally:
            cursor.close()
            
    else:
        album = (id, tituloA, artistaA, anioA)
        return render_template('formUpdate.html', errores=errores, album=album)


#Ruta de eliminación
@app.route('/eliminar/<int:id>')
def mostrar_eliminar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('select * from Albums where id = %s', (id,))
        album = cursor.fetchone()
        if album:
            return render_template('confirmDel.html', album=album)
    except Exception as e:
        flash('Error al cargar el álbum: '+ str(e))
        return redirect(url_for('home'))
    finally:
        cursor.close()
        
@app.route('/eliminar/<int:id>', methods=['POST'])
def confirmarEliminar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('update Albums set estatus = 0 where id = %s', (id,))
        mysql.connection.commit()
        flash('Álbum eliminado en Base de datos')
    except Exception as e:
        mysql.connection.rollback()
        flash('Algo falló: ' + str(e))
    finally:
        cursor.close()
    return redirect(url_for('home'))
   
if __name__ == '__main__':
    app.run(port=3000, debug=True)