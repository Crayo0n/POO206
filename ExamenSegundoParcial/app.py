from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="U41578780o"
app.config['MYSQL_DB']="ContactosBD"
app.secret_key='mysecretkey'

mysql=MySQL(app)

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
        cursor.execute('select * from contactos where estatus = 1')
        consultaTodo=cursor.fetchall()
        return render_template('inicio.html',errores={},contactos=consultaTodo)

    except Exception as e:
        print('Error en la consulta: '+e)
        return render_template('inicio.html',errores={},contactos=[])

    finally:
        cursor.close()





#ruta para el insert
@app.route('/guardarContacto', methods=['POST'])
def guardar(): 
    errores={}
    #Obtener los datos a insestrar
    nombre= request.form.get('txtNombre','').strip()
    correo= request.form.get('txtCorreo','').strip()
    telefono= request.form.get('txtTelefono','').strip()
    edad= request.form.get('txtEdad','').strip()


    if not nombre:
        errores['txtNombre'] = 'Nombre del contacto obligatorio'
    if not correo:
        errores['txtCorreo'] = 'Correo obligatorio'
    if not len(telefono)==10:
        errores['txtTelefono'] = 'Telefono incorrecto'
    elif not edad.isdigit() or int(edad) < 1 or int(edad) > 105:
        errores['txtEdad'] = 'Ingresa una edad valida'
        
    if not errores:
        #Intentamos Ejecutar el Insert
        try:
            cursor=mysql.connection.cursor()
            cursor.execute('insert into contactos (nombre, correo, telefono, edad) values (%s,%s,%s,%s)',(nombre,correo,telefono, edad))
            
            mysql.connection.commit()
            flash('Contacto se guardo en la BD')
            return redirect(url_for('home'))
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Error: '+ str(e))
            return redirect(url_for('home'))
    
        finally:    
            cursor.close()
    
    return render_template('inicio.html', errores = errores)




#Ruta de detalles       
@app.route('/detalles/<int:id>')
def detalle(id):
    try:
        cursor=mysql.connection.cursor()
        cursor.execute('select * from contactos where id= %s',((id),))
        
        consultaID=cursor.fetchone()
        return render_template ('DetallesContacto.html', errores={},contacto=consultaID)
    
    except Exception as e:
        print('Error al consultar por ID '+str(e))
        return redirect (url_for('home'))
    
    finally:
        cursor.close()


@app.route('/actualizar/<int:id>', methods=['GET'])
def mostrar_actualizar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('select * from contactos where id = %s', (id,))
        contacto = cursor.fetchone()  # Obtener los datos del álbum
        if contacto:
            return render_template('ActualizarContacto.html', contacto=contacto, errores={})
        else:
            flash('Contacto no encontrado')
            return redirect(url_for('home'))
    except Exception as e:
        flash(f'Error al cargar los datos del contacto: {e}')
        return redirect(url_for('home'))
    finally:
        cursor.close()


# ruta para actualizar
@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    errores = {}
    nombreA = request.form.get('txtNombreA', '').strip()
    correoA = request.form.get('txtCorreoA', '').strip()
    telefonoA = request.form.get('txtTelefonoA', '').strip()
    edadA = request.form.get('txtEdadA', '').strip()

    if not nombreA:
        errores['txtNombreA'] = 'Nombre del contacto obligatorio'
    if not correoA:
        errores['txtCorreoA'] = 'Correo obligatorio'
    if not len(telefonoA)==10:
        errores['txtTelefonoA'] = 'Telefono incorrecto'
    elif not edadA.isdigit() or int(edadA) < 1 or int(edadA) > 105:
        errores['txtEdadA'] = 'Ingresa una edad valida'

    if not errores:
        try:
            cursor = mysql.connection.cursor()
            cursor.execute('update contactos set nombre=%s, correo=%s, telefono=%s,edad=%s where id=%s',(nombreA, correoA, telefonoA, edadA , id))
            mysql.connection.commit()
            flash('Contacto se actualizó correctamente')
            return redirect(url_for('home'))
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Error: ' + str(e))
            return redirect(url_for('home'))
        
        finally:
            cursor.close()
            
    else:
        contacto = (id, nombreA, correoA, telefonoA, edadA)
        return render_template('ActualizarContacto.html', errores=errores, contacto=contacto)


#Ruta de eliminación
@app.route('/eliminar/<int:id>')
def mostrar_eliminar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('select * from contactos where id = %s', (id,))
        contacto = cursor.fetchone()
        if contacto:
            return render_template('EliminarContacto.html', contacto=contacto)
    except Exception as e:
        flash('Error al cargar el contacto: '+ str(e))
        return redirect(url_for('home'))
    finally:
        cursor.close()
        
@app.route('/eliminar/<int:id>', methods=['POST'])
def confirmarEliminar(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('update contactos set estatus = 0 where id = %s', (id,))
        mysql.connection.commit()
        flash('Contacto eliminado en Base de datos')
    except Exception as e:
        mysql.connection.rollback()
        flash('Algo falló: ' + str(e))
    finally:
        cursor.close()
    return redirect(url_for('home'))
   
if __name__ == '__main__':
    app.run(port=3000, debug=True)