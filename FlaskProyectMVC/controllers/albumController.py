from flask import Blueprint, render_template, request,redirect,url_for,flash
from models.albumModel import *
 
albumsBP= Blueprint('albums',__name__)

#ruta de inicio
@albumsBP.route('/')
def home(): 
    try:
        consultaTodo=getAll()
        return render_template('formulario.html',errores={},albums=consultaTodo)

    except Exception as e:
        print('Error en la consulta: '+ str(e))
        return render_template('formulario.html',errores={},albums=[])



#ruta de agregar
@albumsBP.route('/guardarAlbum', methods=['POST'])
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
            insertAlbum(titulo,artista,anio)
            flash('Album se guardo en la BD')
            return redirect(url_for('albums.home'))
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Error: '+ str(e))
            return redirect(url_for('albums.home'))
    
    
    return render_template('formulario.html', errores = errores)


#ruta de consulta un solo Album
@albumsBP.route('/detalles/<int:id>')
def detalle(id):
    try:
        consultaID=getByID(id)
        return render_template ('consulta.html', errores={},album=consultaID)
    
    except Exception as e:
        print('Error al consultar por ID '+e)
        return redirect (url_for('albums.home'))
    
#ruta para mostrar actualizacion
@albumsBP.route('/actualizar/<int:id>', methods=['GET'])
def mostrar_actualizar(id):
    try:
        album=getByID(id)
        if album:
            return render_template('formUpdate.html', album=album, errores={})
        else:
            flash('Álbum no encontrado')
            return redirect(url_for('albums.home'))
    except Exception as e:
        flash('Error: ' + str(e))
        return redirect(url_for('albums.home'))

    
#ruta para actualizar album
@albumsBP.route('/actualizar/<int:id>', methods=['POST'])
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
            actuAlbum(id,tituloA,artistaA,anioA)
            flash('Album se actualizó correctamente')
            return redirect(url_for('albums.home'))
        
        except Exception as e:
            mysql.connection.rollback()
            flash('Error: ' + str(e))
            return redirect(url_for('albums.home'))
            
    else:
        album = (id, tituloA, artistaA, anioA)
        return render_template('formUpdate.html', errores=errores, album=album)
    
    
#ruta para mostrar eliminar Album
@albumsBP.route('/eliminar/<int:id>')
def mostrar_eliminar(id):
    try:
        album=getByID(id)
        if album:
            return render_template('confirmDel.html', album=album)
    except Exception as e:
        flash('Error al cargar el álbum: '+ str(e))
        return redirect(url_for('albums.home'))


#ruta para eliminar Album
@albumsBP.route('/eliminar/<int:id>', methods=['POST'])
def confirmarEliminar(id):
    try:
        eliminarAlbum(id)
        flash('Álbum eliminado en Base de datos')
    except Exception as e:
        mysql.connection.rollback()
        flash('Algo falló: ' + str(e))
    return redirect(url_for('albums.home'))
