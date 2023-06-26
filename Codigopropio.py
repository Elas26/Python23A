import FuncionDeConexion
import mysql.connector
def interfazSql(sql):
    try:
        conexion = FuncionDeConexion.conexionBD(2)#PONER NUMERO DE CONEXION
        cursor = conexion.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
    except mysql.connector.Error as err:
        print("Ocurrio un error al conectar: ",err)
    finally:
        print("Conexion closed")
        conexion.close()
        
interfazSql("Select name from Maestro where name like 'd%'")