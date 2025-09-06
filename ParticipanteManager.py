import csv  # Faltaba este import
import re
from Entidad import Entidad

class ParticipanteManager(Entidad):
    def __init__(self):
        super().__init__(
            "participantes.csv", 
            ["id_participante", "nombre", "edad", "ciudad", "telefono"]
        )
    
    def agregar(self):
        print("\n--- AGREGAR PARTICIPANTE ---")
        try:
            with open(self.archivo, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                nuevo_id = self.obtener_ultimo_id()
                
                nombre = input("Nombre: ")
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío.")
                
                edad = int(input("Edad: "))
                if edad < 1 or edad > 120:
                    raise ValueError("La edad debe estar entre 1 y 120 años.")
                
                ciudad = input("Ciudad: ")
                if not ciudad:
                    raise ValueError("La ciudad no puede estar vacía.")
                
                telefono = input("Teléfono: ")
                if not re.match(r'^[\d\s\-\+\(\)]+$', telefono):
                    raise ValueError("El formato del teléfono no es válido.")
                
                writer.writerow([nuevo_id, nombre, edad, ciudad, telefono])
                print(f"Participante agregado con éxito. ID: {nuevo_id}")
                return nuevo_id
                
        except ValueError as ve:
            print(f"Error de validación: {ve}")
            return None
        except Exception as e:
            print(f"Error al agregar participante: {e}")
            return None
    
    def consultar(self, id_participante):
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
    
    def editar(self, id_participante):
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
            
            nombre = input(f"Nuevo nombre ({row[1]}): ") or row[1]
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            
            try:
                edad = input(f"Nueva edad ({row[2]}): ")
                edad = int(edad) if edad else int(row[2])
                if edad < 1 or edad > 120:
                    raise ValueError("La edad debe estar entre 1 y 120 años.")
            except ValueError:
                raise ValueError("La edad debe ser un número entero.")
            
            ciudad = input(f"Nueva ciudad ({row[3]}): ") or row[3]
            if not ciudad:
                raise ValueError("La ciudad no puede estar vacía.")
            
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
    
    def eliminar(self, id_participante):
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