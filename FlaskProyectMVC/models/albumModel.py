from app import mysql

#metodo para obtener albums activos
def getAll():
    cursor=mysql.connection.cursor()
    cursor.execute('select * from Albums where estatus = 1')
    consultaTodo=cursor.fetchall()
    cursor.close()
    return consultaTodo

#metodo para obtener album por ID
def getByID(id):
    cursor=mysql.connection.cursor()
    cursor.execute('select * from Albums where id= %s',((id),))
    consultaID=cursor.fetchone()
    cursor.close()
    return consultaID

#metodo para insert album 
def insertAlbum(titulo,artista,anio):
    cursor=mysql.connection.cursor()
    cursor.execute('insert into Albums (Titulo, Artista, Año) values (%s,%s,%s)',(titulo,artista,anio))
    mysql.connection.commit()
    cursor.close()
    

#metodo para actualizar album 
def actuAlbum(id,tituloA,artistaA,anioA):
    cursor = mysql.connection.cursor()
    cursor.execute('update Albums set Titulo=%s, Artista=%s, Año=%s where id=%s',(tituloA, artistaA, anioA, id))
    mysql.connection.commit()
    cursor.close()
    
    
#metodo para eliminar album
def eliminarAlbum(id):
    cursor = mysql.connection.cursor()
    cursor.execute('update Albums set estatus = 0 where id = %s', (id,))
    mysql.connection.commit()
    cursor.close()


