import re
import csv
from Entidad import Entidad

class CuentaManager(Entidad):
    """
    Gestiona las operaciones CRUD para las cuentas de usuarios en el sistema.
    
    Hereda de la clase abstracta Entidad y se encarga de manejar todas las
    operaciones relacionadas con cuentas: creación, consulta, edición y eliminación.
    
    Attributes:
        archivo (str): Nombre del archivo CSV donde se almacenan las cuentas
        campos (list): Lista de nombres de columnas para el archivo CSV
        participante_manager (ParticipanteManager): Instancia para gestionar participantes
    """
    
    def __init__(self, participante_manager):
        """
        Inicializa el manager de cuentas.
        
        Args:
            participante_manager (ParticipanteManager): Instancia del manager de participantes
                para validar la existencia de participantes al crear cuentas.
        """
        super().__init__(
            "cuentas.csv", 
            ["id_cuenta", "id_participante", "usuario", "contrasena", "fecha_creacion"]
        )
        self.participante_manager = participante_manager
    
    def agregar(self):
        """
        Agrega una nueva cuenta al sistema.
        
        Solicita al usuario los datos necesarios para crear una cuenta, valida
        que el participante exista y guarda la información en el archivo CSV.
        
        Returns:
            int or None: ID de la cuenta creada si es exitoso, None si ocurre un error
        
        Raises:
            ValueError: Si los datos ingresados no pasan las validaciones
        """
        print("\n--- AGREGAR CUENTA ---")
        try:
            # Verificar que el participante existe
            id_participante = int(input("ID del participante: "))
            participante = self.participante_manager.consultar(id_participante)
            
            if not participante:
                print("Error: El participante no existe.")
                return None
            
            with open(self.archivo, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                nuevo_id = self.obtener_ultimo_id()
                
                usuario = input("Usuario: ")
                if not usuario:
                    raise ValueError("El usuario no puede estar vacío.")
                
                contrasena = input("Contraseña: ")
                if not contrasena:
                    raise ValueError("La contraseña no puede estar vacía.")
                
                fecha_creacion = input("Fecha de creación (YYYY-MM-DD): ")
                if not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_creacion):
                    raise ValueError("El formato de fecha debe ser YYYY-MM-DD.")
                
                writer.writerow([nuevo_id, id_participante, usuario, contrasena, fecha_creacion])
                print(f"Cuenta agregada con éxito. ID: {nuevo_id}")
                return nuevo_id
                
        except ValueError as ve:
            print(f"Error de validación: {ve}")
            return None
        except Exception as e:
            print(f"Error al agregar cuenta: {e}")
            return None
    
    def consultar(self, id_cuenta):
        """
        Consulta una cuenta específica por su ID.
        
        Args:
            id_cuenta (str or int): ID de la cuenta a consultar
        
        Returns:
            list or None: Datos de la cuenta si se encuentra, None si no existe
        
        """
        print("\n--- CONSULTAR CUENTA ---")
        try:
            id_cuenta = int(id_cuenta)
            _, row = self.buscar_por_id(id_cuenta)
            
            if row:
                print(f"\nID Cuenta: {row[0]}")
                print(f"ID Participante: {row[1]}")
                print(f"Usuario: {row[2]}")
                print(f"Contraseña: {row[3]}")
                print(f"Fecha de creación: {row[4]}")
                return row
            else:
                print("Cuenta no encontrada.")
                return None
                    
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return None
        except Exception as e:
            print(f"Error al consultar cuenta: {e}")
            return None
    
    def editar(self, id_cuenta):
        """
        Edita los datos de una cuenta existente.
        
        Permite modificar el usuario, contraseña, fecha de creación y participante
        asociado a una cuenta. Valida que el nuevo participante exista.
        
        Args:
            id_cuenta (str or int): ID de la cuenta a editar
        
        Returns:
            bool: True si la edición fue exitosa, False si ocurrió un error
        """
        print("\n--- EDITAR CUENTA ---")
        try:
            id_cuenta = int(id_cuenta)
            indice, row = self.buscar_por_id(id_cuenta)
            
            if not row:
                print("Cuenta no encontrada.")
                return False
            
            # Verificar que el nuevo participante existe si se cambia
            nuevo_id_participante = input(f"Nuevo ID de participante ({row[1]}): ") or row[1]
            participante = self.participante_manager.consultar(nuevo_id_participante)
            
            if not participante:
                print("Error: El participante no existe.")
                return False
            
            # Leer todas las cuentas
            with open(self.archivo, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
            
            print(f"\nEditando cuenta: {row[2]}")
            
            usuario = input(f"Nuevo usuario ({row[2]}): ") or row[2]
            if not usuario:
                raise ValueError("El usuario no puede estar vacío.")
            
            contrasena = input("Nueva contraseña (dejar vacío para mantener la actual): ")
            if not contrasena:
                contrasena = row[3]
            
            fecha_creacion = input(f"Nueva fecha ({row[4]}): ") or row[4]
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', fecha_creacion):
                raise ValueError("El formato de fecha debe ser YYYY-MM-DD.")
            
            # Actualizar los datos
            rows[indice + 1] = [id_cuenta, nuevo_id_participante, usuario, contrasena, fecha_creacion]
            
            # Escribir todos los datos de vuelta al archivo
            with open(self.archivo, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            
            print("Cuenta actualizada con éxito.")
            return True
                
        except ValueError as ve:
            print(f"Error de validación: {ve}")
            return False
        except Exception as e:
            print(f"Error al editar cuenta: {e}")
            return False
    
    def eliminar(self, id_cuenta):
        """
        Elimina una cuenta del sistema después de confirmación.
        
        Args:
            id_cuenta (str or int): ID de la cuenta a eliminar
        
        Returns:
            bool: True si la eliminación fue exitosa, False si ocurrió un error
        """
        print("\n--- ELIMINAR CUENTA ---")
        try:
            id_cuenta = int(id_cuenta)
            _, row = self.buscar_por_id(id_cuenta)
            
            if not row:
                print("Cuenta no encontrada.")
                return False
            
            # Leer todas las cuentas
            with open(self.archivo, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                rows = list(reader)
            
            # Filtrar la cuenta a eliminar
            nuevos_rows = [rows[0]]  # Mantener la cabecera
            
            for row_data in rows[1:]:  # Saltar la cabecera
                if row_data and row_data[0].isdigit() and int(row_data[0]) != id_cuenta:
                    nuevos_rows.append(row_data)
            
            print(f"¿Está seguro de eliminar la cuenta: {row[2]}?")
            confirmacion = input("Escriba 'SI' para confirmar: ")
            
            if confirmacion.upper() != 'SI':
                print("Eliminación cancelada.")
                return False
            
            # Escribir todos los datos de vuelta al archivo
            with open(self.archivo, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(nuevos_rows)
            
            print("Cuenta eliminada con éxito.")
            return True
                
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return False
        except Exception as e:
            print(f"Error al eliminar cuenta: {e}")
            return False