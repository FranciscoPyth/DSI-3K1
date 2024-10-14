import csv
import json

# Clase abstracta usando el módulo abc
from abc import ABC, abstractmethod

# Clase base que define el Template Method
class FileReader(ABC):
    
    # Método plantilla
    def read_file(self, file_path):
        data = self.open_file(file_path)
        return self.process_file(data)
    
    # Método concreto común para abrir el archivo
    def open_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()
    
    # Método abstracto que será implementado por las subclases
    @abstractmethod
    def process_file(self, data):
        pass


# Subclase para leer archivos CSV
class CSVFileReader(FileReader):
    
    def process_file(self, data):
        rows = []
        for row in csv.reader(data.splitlines()):
            rows.append(row)
        return rows


# Subclase para leer archivos TXT
class TXTFileReader(FileReader):
    
    def process_file(self, data):
        # Procesa el archivo txt dividiendo el contenido en líneas
        return data.splitlines()


# Subclase para leer archivos JSON
class JSONFileReader(FileReader):
    
    def process_file(self, data):
        # Procesa el archivo JSON convirtiéndolo en un diccionario o lista
        return json.loads(data)


# Uso del Template Method
def main():
    # Leer un archivo CSV
    csv_reader = CSVFileReader()
    csv_data = csv_reader.read_file('./behavioral_pattern/data/test_TM.csv')
    print("Datos CSV:", csv_data)
    
    # Leer un archivo TXT
    txt_reader = TXTFileReader()
    txt_data = txt_reader.read_file('./behavioral_pattern/data/test_TM.txt')
    print("Datos TXT:", txt_data)
    
    # Leer un archivo JSON
    json_reader = JSONFileReader()
    json_data = json_reader.read_file('./behavioral_pattern/data/test_TM.json')
    print("Datos JSON:", json_data)

if __name__ == "__main__":
    main()
