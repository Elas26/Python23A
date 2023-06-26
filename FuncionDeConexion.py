import mysql.connector
opcionBaseDeDatos = 2
def conexionBD(opcionBaseDeDatos):
    if opcionBaseDeDatos == 1 :
    #FORMA LOCAL
        host = "142.44.163.242"
        user = "Alumno3" #root
        passwd = "AlumnoPython1@." #""
        port = 4000
        database= "mini-siiau-liz"
       
    elif opcionBaseDeDatos == 2:
    #FORMA REMOTO
        host = "142.44.163.242"
        user = "Alumno3"
        passwd = "AlumnoPython1@."
        port = 4000
        database = "mini-siiau-liz"
        conexion = mysql.connector.connect(
        host= host,
        user= user,
        password= passwd,
        port= port,
        database = database )
    return conexion
