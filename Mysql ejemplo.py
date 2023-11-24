from mysql.connector import connect, Error

try:
    dbConexion = connect(host="localhost", user="root", password="123459", database = "olimpiadas")
    cursor = dbConexion.cursor()
    sql = "select * from Genero"
    #sql = "UPDATE GENERO SET NOMBRE = %s WHERE ID = %s"
    val = [("FEMENINO", 1), ("Masculino",)]
    lista_datos = cursor.fetchall()
    for item in lista_datos:
        print(item)
    #sql = "INSERT INTO GENERO (nombre) VALUES (%s)"
    #val = [("Femenino",), ("Masculino",)]
    cursor.execute(sql, val[0])
    dbConexion.commit()
    print(cursor.lastrowid)

    """
    sql = "show databases"
    cursor.execute(sql)
    lista_datos = cursor.fetchall()

    for item in lista_datos:
        print(item)
    """

except Error as e:
    print(e)


