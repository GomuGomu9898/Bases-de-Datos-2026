from ParticipanteManager import ParticipanteManager
from CuentaManager import CuentaManager
from PokemonManager import PokemonManager

class MenuManager:
    def __init__(self):
        self.participante_manager = ParticipanteManager()
        self.cuenta_manager = CuentaManager(self.participante_manager)
        self.pokemon_manager = PokemonManager(self.participante_manager)
    
    def mostrar_menu_principal(self):
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
    
    def mostrar_menu_participantes(self):
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
    
    def listar_participantes(self):
        print("\n--- LISTA DE PARTICIPANTES ---")
        participantes = self.participante_manager.obtener_todos()
        
        if not participantes:
            print("No hay participantes registrados.")
            return
        
        for participante in participantes:
            print(f"ID: {participante[0]}, Nombre: {participante[1]}, Edad: {participante[2]}, Ciudad: {participante[3]}")
    
    def mostrar_menu_cuentas(self):
        while True:
            print("\n--- GESTIÓN DE CUENTAS ---")
            print("1. Agregar cuenta")
            print("2. Consultar cuenta")
            print("3. Editar cuenta")
            print("4. Eliminar cuenta")
            print("5. Listar todas las cuentas")
            print("6. Volver al menú principal")
            
            try:
                opcion = int(input("Seleccione una opción: "))  # Aquí faltaba cerrar el paréntesis
                
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
    
    def listar_cuentas(self):
        print("\n--- LISTA DE CUENTAS ---")
        cuentas = self.cuenta_manager.obtener_todos()
        
        if not cuentas:
            print("No hay cuentas registradas.")
            return
        
        for cuenta in cuentas:
            print(f"ID: {cuenta[0]}, ID Participante: {cuenta[1]}, Usuario: {cuenta[2]}")
    
    def mostrar_menu_pokemones(self):
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
    
    def listar_pokemones(self):
        print("\n--- LISTA DE POKÉMONES ---")
        pokemones = self.pokemon_manager.obtener_todos()
        
        if not pokemones:
            print("No hay pokémones registrados.")
            return
        
        for pokemon in pokemones:
            print(f"ID: {pokemon[0]}, Entrenador: {pokemon[1]}, Nombre: {pokemon[2]}, Tipo: {pokemon[3]}, Nivel: {pokemon[4]}")