import re
import csv
from Entidad import Entidad

class PokemonManager(Entidad):
    def __init__(self, participante_manager):
        super().__init__(
            "pokemones.csv", 
            ["id_pokemon", "id_entrenador", "nombre", "tipo", "nivel", "movimiento_principal"]
        )
        self.participante_manager = participante_manager
    
    def agregar(self):
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
                
                nombre = input("Nombre del Pokémon: ")
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío.")
                
                tipo = input("Tipo: ")
                if not tipo:
                    raise ValueError("El tipo no puede estar vacío.")
                
                nivel = int(input("Nivel: "))
                if nivel < 1 or nivel > 100:
                    raise ValueError("El nivel debe estar entre 1 y 100.")
                
                movimiento_principal = input("Movimiento principal: ")
                if not movimiento_principal:
                    raise ValueError("El movimiento principal no puede estar vacío.")
                
                writer.writerow([nuevo_id, id_entrenador, nombre, tipo, nivel, movimiento_principal])
                print(f"Pokémon agregado con éxito. ID: {nuevo_id}")
                return nuevo_id
                
        except ValueError as ve:
            print(f"Error de validación: {ve}")
            return None
        except Exception as e:
            print(f"Error al agregar pokémon: {e}")
            return None
    
    def consultar(self, id_pokemon):
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
    
    def editar(self, id_pokemon):
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
            
            nombre = input(f"Nuevo nombre ({row[2]}): ") or row[2]
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            
            tipo = input(f"Nuevo tipo ({row[3]}): ") or row[3]
            if not tipo:
                raise ValueError("El tipo no puede estar vacío.")
            
            try:
                nivel = input(f"Nuevo nivel ({row[4]}): ")
                nivel = int(nivel) if nivel else int(row[4])
                if nivel < 1 or nivel > 100:
                    raise ValueError("El nivel debe estar entre 1 y 100.")
            except ValueError:
                raise ValueError("El nivel debe ser un número entero.")
            
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
    
    def eliminar(self, id_pokemon):
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
            
            for row in rows[1:]:  # Saltar la cabecera
                if row and row[0].isdigit() and int(row[0]) != id_pokemon:
                    nuevos_rows.append(row)
            
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