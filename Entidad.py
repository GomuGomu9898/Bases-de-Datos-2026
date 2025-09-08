import csv
import os
from abc import ABC, abstractmethod

class Entidad(ABC):
    """
    Clase abstracta que define la interfaz base para gestionar entidades en archivos CSV.
    
    Esta clase proporciona funcionalidades comunes para operaciones CRUD (Crear, Leer,
    Actualizar, Eliminar) y sirve como base para todas las entidades del sistema.
    
    Atributos:
        archivo (str): Ruta del archivo CSV donde se almacenan los datos
        campos (list): Lista de nombres de columnas para el archivo CSV
    """
    
    def __init__(self, archivo: str, campos: list):
        """
        Inicializa una nueva entidad con su archivo y estructura de datos.
        
        Args:
            archivo (str): Nombre o ruta del archivo CSV para esta entidad
            campos (list): Lista de strings con los nombres de las columnas
        """
        self.archivo = archivo
        self.campos = campos
        self.inicializar_archivo()
    
    def inicializar_archivo(self) -> None:
        """
        Crea el archivo CSV con las cabeceras si no existe.
        
        Verifica la existencia del archivo y lo crea con la estructura definida
        en `self.campos` si no está presente en el sistema de archivos.
        """
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(self.campos)
    
    def obtener_ultimo_id(self) -> int:
        """
        Obtiene el último ID utilizado en el archivo para generar uno nuevo.
        
        Returns:
            int: El último ID incrementado en 1, o 1 si el archivo está vacío
        """
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Saltar la cabecera
                ids = [int(row[0]) for row in reader if row and row[0].isdigit()]
                return max(ids) + 1 if ids else 1
        except (FileNotFoundError, ValueError, IndexError):
            return 1
    
    def buscar_por_id(self, id_buscar: int) -> tuple:
        """
        Busca un registro específico por su ID en el archivo CSV.
        
        Args:
            id_buscar (int): ID del registro a buscar
        
        Returns:
            tuple: (índice, fila) donde el índice es la posición y fila los datos,
                o (-1, None) si no se encuentra
        """
        try:
            with open(self.archivo, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Saltar la cabecera
                
                for i, row in enumerate(reader):
                    if row and row[0].isdigit() and int(row[0]) == id_buscar:
                        return i, row
                return -1, None
        except (FileNotFoundError, ValueError, IndexError):
            return -1, None
    
    def obtener_todos(self) -> list:
        """
        Obtiene todos los registros del archivo CSV excluyendo la cabecera.
        
        Returns:
            list: Lista de todos los registros encontrados, lista vacía si no hay datos
        """
        try:
            with open(self.archivo, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Saltar la cabecera
                return [row for row in reader if row]
        except FileNotFoundError:
            return []
    
    @abstractmethod
    def agregar(self):
        """
        Método abstracto para agregar una nueva entidad.
        
        Debe ser implementado por las clases hijas para definir la lógica específica
        de agregar un nuevo registro a la entidad correspondiente.
        
        Raises:
            NotImplementedError: Si no es implementado por la clase hija
        """
        pass
    
    @abstractmethod
    def consultar(self, id_entidad):
        """
        Método abstracto para consultar una entidad por su ID.
        
        Args:
            id_entidad: Identificador de la entidad a consultar
        
        Raises:
            NotImplementedError: Si no es implementado por la clase hija
        """
        pass
    
    @abstractmethod
    def editar(self, id_entidad):
        """
        Método abstracto para editar una entidad existente.
        
        Args:
            id_entidad: Identificador de la entidad a editar
        
        Raises:
            NotImplementedError: Si no es implementado por la clase hija
        """
        pass
    
    @abstractmethod
    def eliminar(self, id_entidad):
        """
        Método abstracto para eliminar una entidad.
        
        Args:
            id_entidad: Identificador de la entidad a eliminar
        
        Raises:
            NotImplementedError: Si no es implementado por la clase hija
        """
        pass