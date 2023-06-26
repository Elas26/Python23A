import mysql.connector
opcionBaseDeDatos = 2
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

try:
    conexion = mysql.connector.connect(
        host= host,
        user= user,
        password= passwd,
        port= port,
        database = database )
    cursor = conexion.cursor()
    cursor.execute("Select * From Maestro ") #limit para solo traer algunos
    registros = cursor.fetchall()
    for registro in registros:
        print(f'Id {registro[0]} valor {registro[1]}')
except mysql.connector.Error as err:
    print("Ocurrio un error al conectar: ",err)
finally:
    print("Conexion closed")
    conexion.close()