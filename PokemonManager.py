"""
Módulo PokemonManager - Gestor de pokémones para el Sistema Solrock Battle Association.

Este módulo proporciona la funcionalidad CRUD (Crear, Leer, Actualizar, Eliminar)
para gestionar los pokémones de los participantes del torneo.
"""

import re
import csv
from Entidad import Entidad

class PokemonManager(Entidad):
    """
    Gestiona todas las operaciones relacionadas con pokémones del torneo.
    
    Hereda de la clase abstracta Entidad y implementa los métodos específicos
    para el manejo de pokémones con validaciones de datos y verificación de
    entrenadores existentes.
    
    Attributes:
        archivo (str): Nombre del archivo CSV ('pokemones.csv')
        campos (list): Lista de campos ['id_pokemon', 'id_entrenador', 'nombre','tipo', 'nivel', 'movimiento_principal']
        participante_manager (ParticipanteManager): Instancia para validar entrenadores
    """
    
    def __init__(self, participante_manager):
        """
        Inicializa el manager de pokémones con su archivo y estructura de datos.
        
        Args:
            participante_manager (ParticipanteManager): Instancia del manager de participantes
                para validar la existencia de entrenadores al crear/modificar pokémones.
        """
        super().__init__(
            "pokemones.csv", 
            ["id_pokemon", "id_entrenador", "nombre", "tipo", "nivel", "movimiento_principal"]
        )
        self.participante_manager = participante_manager
    
    def agregar(self) -> int:
        """
        Agrega un nuevo pokémon al sistema con validación de datos.
        
        Solicita al usuario los datos del pokémon, valida cada campo,
        verifica que el entrenador exista y guarda la información en el CSV.
        
        Returns:
            int: ID del pokémon creado si es exitoso, None si ocurre un error
        
        Raises:
            ValueError: Si algún campo no pasa las validaciones
        """
        print("\n--- AGREGAR POKÉMON ---")
        try:
            # Verificar que el entrenador (participante) existe
            id_entrenador = int(input("ID del entrenador (participante): "))
            participante = self.participante_manager.consultar(id_entrenador)
            
            if not participante:
                print("Error: El entrenador no existe.")
                return None
            
            with open(self.archivo, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                nuevo_id = self.obtener_ultimo_id()
                
                # Validación y captura de nombre del Pokémon
                nombre = input("Nombre del Pokémon: ")
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío.")
                
                # Validación y captura de tipo
                tipo = input("Tipo: ")
                if not tipo:
                    raise ValueError("El tipo no puede estar vacío.")
                
                # Validación y captura de nivel
                nivel = int(input("Nivel: "))
                if nivel < 1 or nivel > 100:
                    raise ValueError("El nivel debe estar entre 1 y 100.")
                
                # Validación y captura de movimiento principal
                movimiento_principal = input("Movimiento principal: ")
                if not movimiento_principal:
                    raise ValueError("El movimiento principal no puede estar vacío.")
                
                # Guardar el nuevo Pokémon
                writer.writerow([nuevo_id, id_entrenador, nombre, tipo, nivel, movimiento_principal])
                print(f"Pokémon agregado con éxito. ID: {nuevo_id}")
                return nuevo_id
                
        except ValueError as ve:
            print(f"Error de validación: {ve}")
            return None
        except Exception as e:
            print(f"Error al agregar pokémon: {e}")
            return None
    
    def consultar(self, id_pokemon: str) -> list:
        """
        Consulta un pokémon específico por su ID.
        
        Args:
            id_pokemon (str): ID del pokémon a consultar (puede ser string)
        
        Returns:
            list: Datos del pokémon [id, id_entrenador, nombre, tipo, nivel, movimiento] 
                si se encuentra, None si no existe
        
        Raises:
            ValueError: Si el ID no es un número entero válido
        """
        print("\n--- CONSULTAR POKÉMON ---")
        try:
            id_pokemon = int(id_pokemon)
            _, row = self.buscar_por_id(id_pokemon)
            
            if row:
                print(f"\nID Pokémon: {row[0]}")
                print(f"ID Entrenador: {row[1]}")
                print(f"Nombre: {row[2]}")
                print(f"Tipo: {row[3]}")
                print(f"Nivel: {row[4]}")
                print(f"Movimiento principal: {row[5]}")
                return row
            else:
                print("Pokémon no encontrado.")
                return None
                    
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return None
        except Exception as e:
            print(f"Error al consultar pokémon: {e}")
            return None
    
    def editar(self, id_pokemon: str) -> bool:
        """
        Edita los datos de un pokémon existente.
        
        Permite modificar todos los campos de un pokémon manteniendo
        validaciones consistentes y verificando que el nuevo entrenador exista.
        
        Args:
            id_pokemon (str): ID del pokémon a editar
        
        Returns:
            bool: True si la edición fue exitosa, False si ocurrió un error
        
        Raises:
            ValueError: Si algún campo no pasa las validaciones
        """
        print("\n--- EDITAR POKÉMON ---")
        try:
            id_pokemon = int(id_pokemon)
            indice, row = self.buscar_por_id(id_pokemon)
            
            if not row:
                print("Pokémon no encontrado.")
                return False
            
            # Verificar que el nuevo entrenador existe si se cambia
            nuevo_id_entrenador = input(f"Nuevo ID de entrenador ({row[1]}): ") or row[1]
            participante = self.participante_manager.consultar(nuevo_id_entrenador)
            
            if not participante:
                print("Error: El entrenador no existe.")
                return False
            
            # Leer todos los pokémones
            with open(self.archivo, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
            
            print(f"\nEditando pokémon: {row[2]}")
            
            # Editar nombre con validación
            nombre = input(f"Nuevo nombre ({row[2]}): ") or row[2]
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            
            # Editar tipo con validación
            tipo = input(f"Nuevo tipo ({row[3]}): ") or row[3]
            if not tipo:
                raise ValueError("El tipo no puede estar vacío.")
            
            # Editar nivel con validación
            try:
                nivel = input(f"Nuevo nivel ({row[4]}): ")
                nivel = int(nivel) if nivel else int(row[4])
                if nivel < 1 or nivel > 100:
                    raise ValueError("El nivel debe estar entre 1 y 100.")
            except ValueError:
                raise ValueError("El nivel debe ser un número entero.")
            
            # Editar movimiento principal con validación
            movimiento_principal = input(f"Nuevo movimiento principal ({row[5]}): ") or row[5]
            if not movimiento_principal:
                raise ValueError("El movimiento principal no puede estar vacío.")
            
            # Actualizar los datos
            rows[indice + 1] = [id_pokemon, nuevo_id_entrenador, nombre, tipo, nivel, movimiento_principal]
            
            # Escribir todos los datos de vuelta al archivo
            with open(self.archivo, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            
            print("Pokémon actualizado con éxito.")
            return True
                
        except ValueError as ve:
            print(f"Error de validación: {ve}")
            return False
        except Exception as e:
            print(f"Error al editar pokémon: {e}")
            return False
    
    def eliminar(self, id_pokemon: str) -> bool:
        """
        Elimina un pokémon del sistema después de confirmación.
        
        Args:
            id_pokemon (str): ID del pokémon a eliminar
        
        Returns:
            bool: True si la eliminación fue exitosa, False si ocurrió un error
        
        Raises:
            ValueError: Si el ID no es un número entero válido
        """
        print("\n--- ELIMINAR POKÉMON ---")
        try:
            id_pokemon = int(id_pokemon)
            _, row = self.buscar_por_id(id_pokemon)
            
            if not row:
                print("Pokémon no encontrado.")
                return False
            
            # Leer todos los pokémones
            with open(self.archivo, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
            
            # Filtrar el pokémon a eliminar
            nuevos_rows = [rows[0]]  # Mantener la cabecera
            
            for row_data in rows[1:]:  # Saltar la cabecera
                if row_data and row_data[0].isdigit() and int(row_data[0]) != id_pokemon:
                    nuevos_rows.append(row_data)
            
            # Confirmación de eliminación
            print(f"¿Está seguro de eliminar el pokémon: {row[2]}?")
            confirmacion = input("Escriba 'SI' para confirmar: ")
            
            if confirmacion.upper() != 'SI':
                print("Eliminación cancelada.")
                return False
            
            # Escribir todos los datos de vuelta al archivo
            with open(self.archivo, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(nuevos_rows)
            
            print("Pokémon eliminado con éxito.")
            return True
                
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return False
        except Exception as e:
            print(f"Error al eliminar pokémon: {e}")
            return False