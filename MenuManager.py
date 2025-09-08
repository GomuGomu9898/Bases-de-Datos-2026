"""
Módulo MenuManager - Gestor de menús para el Sistema Solrock Battle Association.

Este módulo proporciona la interfaz de usuario por menús para interactuar con
el sistema de gestión de participantes, cuentas y pokémones.
"""

from ParticipanteManager import ParticipanteManager
from CuentaManager import CuentaManager
from PokemonManager import PokemonManager

class MenuManager:
    """
    Gestiona la navegación por menús y coordina las operaciones del sistema.
    
    Esta clase actúa como el controlador principal que orquesta la interacción
    entre el usuario y los diferentes managers de entidades.
    
    Attributes:
        participante_manager (ParticipanteManager): Instancia para gestionar participantes
        cuenta_manager (CuentaManager): Instancia para gestionar cuentas
        pokemon_manager (PokemonManager): Instancia para gestionar pokémones
    """
    
    def __init__(self):
        """
        Inicializa el MenuManager y todas las dependencias.
        
        Crea las instancias de los managers necesarios y establece las relaciones
        entre ellos para el correcto funcionamiento del sistema.
        """
        self.participante_manager = ParticipanteManager()
        self.cuenta_manager = CuentaManager(self.participante_manager)
        self.pokemon_manager = PokemonManager(self.participante_manager)
    
    def mostrar_menu_principal(self) -> None:
        """
        Muestra el menú principal y maneja la navegación del usuario.
        
        Este método presenta las opciones principales del sistema y redirige
        a los submenús correspondientes según la selección del usuario.
        
        Features:
            - Interfaz interactiva con manejo de errores
            - Navegación cíclica hasta que el usuario elige salir
            - Validación de entradas numéricas
        
        Menu Options:
            1. Gestionar Participantes
            2. Gestionar Cuentas
            3. Gestionar Pokémones
            4. Salir del sistema
        """
        while True:
            print("\n=== SISTEMA SOLROCK BATTLE ASSOCIATION ===")
            print("1. Gestionar Participantes")
            print("2. Gestionar Cuentas")
            print("3. Gestionar Pokémones")
            print("4. Salir")
            
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    self.mostrar_menu_participantes()
                elif opcion == 2:
                    self.mostrar_menu_cuentas()
                elif opcion == 3:
                    self.mostrar_menu_pokemones()
                elif opcion == 4:
                    print("¡Hasta pronto!")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
            except Exception as e:
                print(f"Error inesperado: {e}")
    
    def mostrar_menu_participantes(self) -> None:
        """
        Muestra el submenú para la gestión de participantes.
        
        Permite realizar todas las operaciones CRUD sobre los participantes
        del sistema Solrock Battle Association.
        
        Menu Options:
            1. Agregar participante
            2. Consultar participante
            3. Editar participante
            4. Eliminar participante
            5. Listar todos los participantes
            6. Volver al menú principal
        """
        while True:
            print("\n--- GESTIÓN DE PARTICIPANTES ---")
            print("1. Agregar participante")
            print("2. Consultar participante")
            print("3. Editar participante")
            print("4. Eliminar participante")
            print("5. Listar todos los participantes")
            print("6. Volver al menú principal")
            
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    self.participante_manager.agregar()
                elif opcion == 2:
                    id_participante = input("ID del participante a consultar: ")
                    self.participante_manager.consultar(id_participante)
                elif opcion == 3:
                    id_participante = input("ID del participante a editar: ")
                    self.participante_manager.editar(id_participante)
                elif opcion == 4:
                    id_participante = input("ID del participante a eliminar: ")
                    self.participante_manager.eliminar(id_participante)
                elif opcion == 5:
                    self.listar_participantes()
                elif opcion == 6:
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
            except Exception as e:
                print(f"Error inesperado: {e}")
    
    def listar_participantes(self) -> None:
        """
        Lista todos los participantes registrados en el sistema.
        
        Muestra una vista tabular de todos los participantes con sus
        datos principales en formato legible.
        
        Output Format:
            ID: [id], Nombre: [nombre], Edad: [edad], Ciudad: [ciudad]
        
        Example:
            ID: 1, Nombre: Ash Ketchum, Edad: 10, Ciudad: Pueblo Paleta
        """
        print("\n--- LISTA DE PARTICIPANTES ---")
        participantes = self.participante_manager.obtener_todos()
        
        if not participantes:
            print("No hay participantes registrados.")
            return
        
        for participante in participantes:
            print(f"ID: {participante[0]}, Nombre: {participante[1]}, Edad: {participante[2]}, Ciudad: {participante[3]}")
    
    def mostrar_menu_cuentas(self) -> None:
        """
        Muestra el submenú para la gestión de cuentas de usuario.
        
        Permite realizar operaciones CRUD sobre las cuentas del sistema,
        siempre validando la existencia del participante asociado.
        
        Menu Options:
            1. Agregar cuenta
            2. Consultar cuenta
            3. Editar cuenta
            4. Eliminar cuenta
            5. Listar todas las cuentas
            6. Volver al menú principal
        """
        while True:
            print("\n--- GESTIÓN DE CUENTAS ---")
            print("1. Agregar cuenta")
            print("2. Consultar cuenta")
            print("3. Editar cuenta")
            print("4. Eliminar cuenta")
            print("5. Listar todas las cuentas")
            print("6. Volver al menú principal")
            
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    self.cuenta_manager.agregar()
                elif opcion == 2:
                    id_cuenta = input("ID de la cuenta a consultar: ")
                    self.cuenta_manager.consultar(id_cuenta)
                elif opcion == 3:
                    id_cuenta = input("ID de la cuenta a editar: ")
                    self.cuenta_manager.editar(id_cuenta)
                elif opcion == 4:
                    id_cuenta = input("ID de la cuenta a eliminar: ")
                    self.cuenta_manager.eliminar(id_cuenta)
                elif opcion == 5:
                    self.listar_cuentas()
                elif opcion == 6:
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
            except Exception as e:
                print(f"Error inesperado: {e}")
    
    def listar_cuentas(self) -> None:
        """
        Lista todas las cuentas registradas en el sistema.
        
        Muestra información resumida de todas las cuentas existentes
        con sus datos principales.
        
        Output Format:
            ID: [id], ID Participante: [id_participante], Usuario: [usuario]
        """
        print("\n--- LISTA DE CUENTAS ---")
        cuentas = self.cuenta_manager.obtener_todos()
        
        if not cuentas:
            print("No hay cuentas registradas.")
            return
        
        for cuenta in cuentas:
            print(f"ID: {cuenta[0]}, ID Participante: {cuenta[1]}, Usuario: {cuenta[2]}")
    
    def mostrar_menu_pokemones(self) -> None:
        """
        Muestra el submenú para la gestión de pokémones.
        
        Permite realizar operaciones CRUD sobre los pokémones del sistema,
        validando siempre la existencia del entrenador asociado.
        
        Menu Options:
            1. Agregar pokémon
            2. Consultar pokémon
            3. Editar pokémon
            4. Eliminar pokémon
            5. Listar todos los pokémones
            6. Volver al menú principal
        """
        while True:
            print("\n--- GESTIÓN DE POKÉMONES ---")
            print("1. Agregar pokémon")
            print("2. Consultar pokémon")
            print("3. Editar pokémon")
            print("4. Eliminar pokémon")
            print("5. Listar todos los pokémones")
            print("6. Volver al menú principal")
            
            try:
                opcion = int(input("Seleccione una opción: "))
                
                if opcion == 1:
                    self.pokemon_manager.agregar()
                elif opcion == 2:
                    id_pokemon = input("ID del pokémon a consultar: ")
                    self.pokemon_manager.consultar(id_pokemon)
                elif opcion == 3:
                    id_pokemon = input("ID del pokémon a editar: ")
                    self.pokemon_manager.editar(id_pokemon)
                elif opcion == 4:
                    id_pokemon = input("ID del pokémon a eliminar: ")
                    self.pokemon_manager.eliminar(id_pokemon)
                elif opcion == 5:
                    self.listar_pokemones()
                elif opcion == 6:
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
            except Exception as e:
                print(f"Error inesperado: {e}")
    
    def listar_pokemones(self) -> None:
        """
        Lista todos los pokémones registrados en el sistema.
        
        Muestra información detallada de todos los pokémones con sus
        características principales en formato legible.
        
        Output Format:
            ID: [id], Entrenador: [id_entrenador], Nombre: [nombre], 
            Tipo: [tipo], Nivel: [nivel]
        """
        print("\n--- LISTA DE POKÉMONES ---")
        pokemones = self.pokemon_manager.obtener_todos()
        
        if not pokemones:
            print("No hay pokémones registrados.")
            return
        
        for pokemon in pokemones:
            print(f"ID: {pokemon[0]}, Entrenador: {pokemon[1]}, Nombre: {pokemon[2]}, Tipo: {pokemon[3]}, Nivel: {pokemon[4]}")