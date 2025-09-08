"""
Módulo ParticipanteManager - Gestor de participantes para el Sistema Solrock Battle Association.

Este módulo proporciona la funcionalidad CRUD (Crear, Leer, Actualizar, Eliminar)
para gestionar los participantes del torneo Pokémon.
"""

import csv
import re
from Entidad import Entidad

class ParticipanteManager(Entidad):
    """
    Gestiona todas las operaciones relacionadas con participantes del torneo.
    
    Hereda de la clase abstracta Entidad y implementa los métodos específicos
    para el manejo de participantes con validaciones de datos.
    
    Attributes:
        archivo (str): Nombre del archivo CSV ('participantes.csv')
        campos (list): Lista de campos ['id_participante', 'nombre', 'edad', 'ciudad', 'telefono']
    """
    
    def __init__(self):
        """
        Inicializa el manager de participantes con su archivo y estructura de datos.
        
        Llama al constructor de la clase base para configurar el archivo CSV
        con los campos específicos para participantes.
        """
        super().__init__(
            "participantes.csv", 
            ["id_participante", "nombre", "edad", "ciudad", "telefono"]
        )
    
    def agregar(self) -> int:
        """
        Agrega un nuevo participante al sistema con validación de datos.
        
        Solicita al usuario los datos del participante, valida cada campo
        y guarda la información en el archivo CSV.
        
        Returns:
            int: ID del participante creado si es exitoso, None si ocurre un error
        
        Raises:
            ValueError: Si algún campo no pasa las validaciones
        """
        print("\n--- AGREGAR PARTICIPANTE ---")
        try:
            with open(self.archivo, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                nuevo_id = self.obtener_ultimo_id()
                
                # Validación y captura de nombre
                nombre = input("Nombre: ")
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío.")
                
                # Validación y captura de edad
                edad = int(input("Edad: "))
                if edad < 1 or edad > 120:
                    raise ValueError("La edad debe estar entre 1 y 120 años.")
                
                # Validación y captura de ciudad
                ciudad = input("Ciudad: ")
                if not ciudad:
                    raise ValueError("La ciudad no puede estar vacía.")
                
                # Validación y captura de teléfono
                telefono = input("Teléfono: ")
                if not re.match(r'^[\d\s\-\+\(\)]+$', telefono):
                    raise ValueError("El formato del teléfono no es válido.")
                
                # Guardar el nuevo participante
                writer.writerow([nuevo_id, nombre, edad, ciudad, telefono])
                print(f"Participante agregado con éxito. ID: {nuevo_id}")
                return nuevo_id
                
        except ValueError as ve:
            print(f"Error de validación: {ve}")
            return None
        except Exception as e:
            print(f"Error al agregar participante: {e}")
            return None
    
    def consultar(self, id_participante: str) -> list:
        """
        Consulta un participante específico por su ID.
        
        Args:
            id_participante (str): ID del participante a consultar (puede ser string)
        
        Returns:
            list: Datos del participante [id, nombre, edad, ciudad, telefono] si se encuentra,
                None si no existe
        
        Raises:
            ValueError: Si el ID no es un número entero válido
            
        """
        print("\n--- CONSULTAR PARTICIPANTE ---")
        try:
            id_participante = int(id_participante)
            _, row = self.buscar_por_id(id_participante)
            
            if row:
                print(f"\nID: {row[0]}")
                print(f"Nombre: {row[1]}")
                print(f"Edad: {row[2]}")
                print(f"Ciudad: {row[3]}")
                print(f"Teléfono: {row[4]}")
                return row
            else:
                print("Participante no encontrado.")
                return None
                    
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return None
        except Exception as e:
            print(f"Error al consultar participante: {e}")
            return None
    
    def editar(self, id_participante: str) -> bool:
        """
        Edita los datos de un participante existente.
        
        Permite modificar todos los campos de un participante manteniendo
        validaciones consistentes con el método agregar.
        
        Args:
            id_participante (str): ID del participante a editar
        
        Returns:
            bool: True si la edición fue exitosa, False si ocurrió un error
        
        Raises:
            ValueError: Si algún campo no pasa las validaciones
            
        """
        print("\n--- EDITAR PARTICIPANTE ---")
        try:
            id_participante = int(id_participante)
            indice, row = self.buscar_por_id(id_participante)
            
            if not row:
                print("Participante no encontrado.")
                return False
            
            # Leer todos los participantes
            with open(self.archivo, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
            
            print(f"\nEditando participante: {row[1]}")
            
            # Editar nombre con validación
            nombre = input(f"Nuevo nombre ({row[1]}): ") or row[1]
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            
            # Editar edad con validación
            try:
                edad = input(f"Nueva edad ({row[2]}): ")
                edad = int(edad) if edad else int(row[2])
                if edad < 1 or edad > 120:
                    raise ValueError("La edad debe estar entre 1 y 120 años.")
            except ValueError:
                raise ValueError("La edad debe ser un número entero.")
            
            # Editar ciudad con validación
            ciudad = input(f"Nueva ciudad ({row[3]}): ") or row[3]
            if not ciudad:
                raise ValueError("La ciudad no puede estar vacía.")
            
            # Editar teléfono con validación
            telefono = input(f"Nuevo teléfono ({row[4]}): ") or row[4]
            if not re.match(r'^[\d\s\-\+\(\)]+$', telefono):
                raise ValueError("El formato del teléfono no es válido.")
            
            # Actualizar los datos (indice + 1 porque la primera fila es la cabecera)
            rows[indice + 1] = [id_participante, nombre, edad, ciudad, telefono]
            
            # Escribir todos los datos de vuelta al archivo
            with open(self.archivo, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            
            print("Participante actualizado con éxito.")
            return True
                
        except ValueError as ve:
            print(f"Error de validación: {ve}")
            return False
        except Exception as e:
            print(f"Error al editar participante: {e}")
            return False
    
    def eliminar(self, id_participante: str) -> bool:
        """
        Elimina un participante del sistema después de confirmación.
        
        Args:
            id_participante (str): ID del participante a eliminar
        
        Returns:
            bool: True si la eliminación fue exitosa, False si ocurrió un error
        
        Raises:
            ValueError: Si el ID no es un número entero válido
        """
        print("\n--- ELIMINAR PARTICIPANTE ---")
        try:
            id_participante = int(id_participante)
            _, row = self.buscar_por_id(id_participante)
            
            if not row:
                print("Participante no encontrado.")
                return False
            
            # Leer todos los participantes
            with open(self.archivo, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
            
            # Filtrar el participante a eliminar
            nuevos_rows = [rows[0]]  # Mantener la cabecera
            
            for row_data in rows[1:]:  # Saltar la cabecera
                if row_data and row_data[0].isdigit() and int(row_data[0]) != id_participante:
                    nuevos_rows.append(row_data)
            
            # Confirmación de eliminación
            print(f"¿Está seguro de eliminar al participante: {row[1]}?")
            confirmacion = input("Escriba 'SI' para confirmar: ")
            
            if confirmacion.upper() != 'SI':
                print("Eliminación cancelada.")
                return False
            
            # Escribir todos los datos de vuelta al archivo
            with open(self.archivo, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(nuevos_rows)
            
            print("Participante eliminado con éxito.")
            return True
                
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return False
        except Exception as e:
            print(f"Error al eliminar participante: {e}")
            return False