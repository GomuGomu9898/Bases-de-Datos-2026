import csv
import os
from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, archivo, campos):
        self.archivo = archivo
        self.campos = campos
        self.inicializar_archivo()
    
    def inicializar_archivo(self):
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(self.campos)
    
    def obtener_ultimo_id(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Saltar la cabecera
                ids = [int(row[0]) for row in reader if row and row[0].isdigit()]
                return max(ids) + 1 if ids else 1
        except:
            return 1
    
    def buscar_por_id(self, id_buscar):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Saltar la cabecera
                
                for i, row in enumerate(reader):
                    if row and row[0].isdigit() and int(row[0]) == id_buscar:
                        return i, row
                return -1, None
        except:
            return -1, None
    
    def obtener_todos(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Saltar la cabecera
                return [row for row in reader if row]
        except:
            return []
    
    @abstractmethod
    def agregar(self):
        pass
    
    @abstractmethod
    def consultar(self, id_entidad):
        pass
    
    @abstractmethod
    def editar(self, id_entidad):
        pass
    
    @abstractmethod
    def eliminar(self, id_entidad):
        pass