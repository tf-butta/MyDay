import sys
import json
import os
import urllib.request
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from ui_main import Ui_MainWindow


BASE_DE_DATOS = "./usuarios.json"

def get_database():
    if not os.path.exists(BASE_DE_DATOS):
        with open(BASE_DE_DATOS, "w") as db_file:
            json.dump([], db_file, indent=4)
            
    with open(BASE_DE_DATOS, "r") as db_file:
        return json.load(db_file)


def save_database(db):
    with open(BASE_DE_DATOS, "w") as db_file:
        json.dump(db, db_file, indent=4)
    


class MainWindow(QMainWindow):  #Clase MainWindow heredada de QMainWindow, que es una clase de PyQt para crear la ventana principal de la app.
    def __init__(self): #constructor method. Se ejuecuta cuando la instancia de la clase es creada.
        super().__init__() #llama al constructor de la clase QMainWindow, para inicializar las funcionalidades básicas de la ventana principal de la app.
        self.ui = Ui_MainWindow() #crea una instancia de Ui_MainWindow class, la cual es la definición de la interfaz del usuario para la ventana principal.
        self.ui.setupUi(self) #llama al método setupUi() de la instancia Ui_MainWindow, para setear los componenetes de la interfaz del usuario dentro de main window.

    def iniciar_sesion(self):
        print("iniciar sesion")
        correo = self.ui.txtMail.text().strip()
        password = self.ui.txtPass.text().strip()

        usuarios = get_database()

        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                self.mostrar_mensaje(f"Bienvenido, {usuario['nombre']} 👋", "exito")
                
                self.abrir_ventana_principal(usuario["nombre"])
                return


    def crear_cuenta(self):
        print("Crear cuenta")
        nombre = self.ui.txtNombre.text().strip()
        correo = self.ui.txtMail.text().strip()
        password = self.ui.txtPass.text().strip()

        if not nombre or not correo or not password:
            self.mostrar_mensaje("Por favor complete todos los campos", "error")
            return

        usuarios = get_database()

        for usuario in usuarios:
            if usuario["correo"] == correo:
                self.mostrar_mensaje("Error: el correo ya está registrado", "error")
                return

        usuarios.append({
            "nombre": nombre,
            "correo": correo,
            "password": password
        })

        save_database(usuarios)
        
    def mostrar_mensaje(self, texto, tipo):
        self.ui.lblError.setText(texto)
        color = "red" if tipo == "error" else "green"
        self.ui.lblError.setStyleSheet(f"color: {color}; font-weight: bold;")
        
    def abrir_ventana_principal(self, nombre_usuario):
        self.ventana_principal = VentanaPrincipal(nombre_usuario)
        self.ventana_principal.show()
        self.close()  # cierra la ventana de login
        




if __name__ == "__main__": #checkea si el script está siendo ejecutado como el prog principal (no importado como un modulo).
    app = QApplication(sys.argv)    # Crea un Qt widget, la cual va ser nuestra ventana.
    window = MainWindow() #crea una intancia de MainWindow 
    window.show()   # IMPORTANT!!!!! la ventanas estan ocultas por defecto.
    sys.exit(app.exec_()) # Start the event loop.