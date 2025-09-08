"""
Módulo principal del Sistema de Gestión para Solrock Battle Association.

Este script inicia la aplicación y sirve como punto de entrada principal
para el sistema de gestión de participantes, cuentas y pokémones.
"""

from MenuManager import MenuManager

if __name__ == "__main__":
    """
    Punto de entrada principal de la aplicación.
    
    Esta condición verifica si el script está siendo ejecutado directamente
    (no importado como módulo) y en ese caso inicia el sistema.
    
    Steps:
        1. Crea una instancia de MenuManager
        2. Inicia el menú principal
        3. Maneja la ejecución hasta que el usuario decida salir
    """
    # Crear instancia del gestor de menús
    sistema = MenuManager()
    
    # Iniciar el sistema mostrando el menú principal
    sistema.mostrar_menu_principal()