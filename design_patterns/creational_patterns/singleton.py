"""
Este patrón es sencillo y pertenece a los patrones creacionales, 
se encarga de crear una instancia única de una clase particular, proporciona un punto de 
acceso global a dicha instancia, se suele implementar para conexiones con bases de datos u otros 
recursos compartidos, para no tener que crear muchas conexiones y utilizar siempre una conexión única. 
A continuación mostramos un pequeño ejemplo:
"""

# Cabe aclarar utilizamos estas librerias en forma de ejemplo
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()


class MySQLConnectionSingleton:
    _instance = None

    def __new__(cls):
        """El método constructor __new__ se dispara automáticamente al crear una instancia/objeto de
        la clase.
        :cls: Objeto que se está creando
        :return: Devuelve un nuevo objeto
        """
        if cls._instance is None:
            # Pedimos al padre (super), que cree un objeto cls y lo asigne a _instance
            cls._instance = super(MySQLConnectionSingleton, cls).__new__(cls)
            cls._instance._connection = None
        # Se retorna _instance, ya sea que estaba asigando o si se acaba de crear
        return cls._instance

    def connect(self):
        if self._connection is None:
            try:
                # Obtener las credenciales desde las variables de entorno
                host = os.getenv("DB_HOST")
                user = os.getenv("DB_USER")
                password = os.getenv("DB_PASSWORD")
                database = os.getenv("DB_NAME")

                self._connection = mysql.connector.connect(
                    host=host, user=user, password=password, database=database
                )
                if self._connection.is_connected():
                    print("Conexión exitosa a la base de datos")
            except Error as e:
                print(f"Error al conectar a la base de datos: {e}")
        return self._connection

    def disconnect(self):
        if self._connection is not None and self._connection.is_connected():
            self._connection.close()
            self._connection = None
            print("Conexión cerrada")


# Ejemplo de uso
if __name__ == "__main__":
    db_singleton = MySQLConnectionSingleton()

    # Conectar a la base de datos
    connection = db_singleton.connect()

    # Realizar consultas a la base de datos
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("Conectado a la base de datos:", record)

    # Cerrar la conexión
    db_singleton.disconnect()
