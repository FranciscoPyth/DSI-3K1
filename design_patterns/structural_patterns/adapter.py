"""
Este es un pequeño ejemplo del patrón aplicado, de igual manera buscar otro en donde 
el caso práctico sea más real y en donde solucione un problema actual.
"""


# Clase del enchufe europeo
class EuropeanPlug:
    def provide_electricity(self):
        return "Conectado a enchufe europeo de 220V."


# Clase de la toma americana
class AmericanSocket:
    def connect(self, plug):
        print(f"Conectando a toma americana: {plug}")


# Clase adaptador que permite conectar el enchufe europeo a la toma americana
class PlugAdapter:
    def __init__(self, european_plug):
        self.european_plug = european_plug

    def provide_electricity(self):
        # Adaptamos el enchufe europeo para que pueda conectarse a la toma americana
        return self.european_plug.provide_electricity()


# Programa principal
if __name__ == "__main__":
    # Tenemos un enchufe europeo
    european_plug = EuropeanPlug()

    # Tenemos una toma americana
    american_socket = AmericanSocket()

    # Creamos el adaptador
    adapter = PlugAdapter(european_plug)

    # Conectamos el enchufe europeo a la toma americana usando el adaptador
    american_socket.connect(adapter.provide_electricity())
