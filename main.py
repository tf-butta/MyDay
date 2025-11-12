import sys
import json
import os
import urllib.request
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from ui_main import Ui_MainWindow as uiMain
from ui_datos import Ui_MainWindow as uiDatos
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random



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
        self.ui = uiMain() #crea una instancia de Ui_MainWindow class, la cual es la definición de la interfaz del usuario para la ventana principal.
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
        self.mostrar_mensaje(" Cuenta creada con éxito", "exito")
        
    def mostrar_mensaje(self, texto, tipo):
        self.ui.lblError.setText(texto)
        color = "red" if tipo == "error" else "green"
        self.ui.lblError.setStyleSheet(f"color: {color}; font-weight: bold;")
        
    def abrir_ventana_principal(self, nombre_usuario):
        self.ventana_principal = VentanaPrincipal(nombre_usuario)
        self.ventana_principal.show()
        self.close()  # cierra la ventana de login
        

class VentanaPrincipal(QMainWindow):
    def __init__(self, nombre_usuario):
        super().__init__()
        self.ui = uiDatos()
        self.ui.setupUi(self)

        self.nombre_usuario = nombre_usuario

        # Mostrar mensaje de bienvenida
        if hasattr(self.ui, "lblBienvenida"):
            self.ui.lblBienvenida.setText(f"¡Bienvenido, {nombre_usuario}! ")

        # Conectar botones
        
        self.ui.btnSalir.clicked.connect(self.salir)

        # Mostrar datos iniciales
        self.actualizar_datos()
        self.actualizar_clima()

    # === BOTÓN SALIR ===
    def salir(self):
        self.close()
    
    def actualizar_clima(self):
        try:
            url = (
                "https://api.open-meteo.com/v1/forecast?"
                "latitude=-31.4167&longitude=-64.1833&current=temperature_2m,weather_code"
            )

            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode())

            temperatura = data["current"]["temperature_2m"]
            codigo_clima = data["current"]["weather_code"]

            descripcion = self.descripcion_clima(codigo_clima)

            self.ui.lblTemperaturaClima.setText(f"{temperatura} °C")
            self.ui.lblIconoClima.setText(descripcion)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo actualizar el clima:\n{e}")

    
    def descripcion_clima(self, codigo):
        condiciones = {
            0: "Despejado ☀️",
            1: "Mayormente despejado 🌤️",
            2: "Parcialmente nublado ⛅",
            3: "Nublado ☁️",
            45: "Niebla 🌫️",
            51: "Llovizna 🌧️",
            61: "Lluvia ligera 🌧️",
            63: "Lluvia moderada 🌦️",
            65: "Lluvia intensa 🌧️",
            80: "Tormentas ⛈️",
        }
        return condiciones.get(codigo, "Desconocido")

    # === BOTÓN ACTUALIZAR DATOS ===
    def actualizar_datos(self):
        ahora = datetime.now()
        self.ui.lblHora.setText(ahora.strftime("%H:%M:%S"))
        self.ui.lblFecha.setText(ahora.strftime("%d/%m/%Y"))

        # Simulamos los datos de Arduino
        temp = 23.5
        luz = "Alta"
        estado = "Activo"
        horas_dormidas = 7

        # Mostrar los valores en la interfaz
        self.ui.lblTempArduino.setText(f"{temp} °C")
        self.ui.lblLuz.setText(luz)
        self.ui.lblEstado.setText(estado)
        self.ui.label_9.setText(str(horas_dormidas))

    # === BOTÓN ENVIAR RESUMEN ===
    def enviar_resumen(self):
        # Obtiene datos de la interfaz
        resumen = (
            f"Resumen del día para {self.nombre_usuario}:\n\n"
            f"Hora actual: {self.ui.lblHora.text()}\n"
            f"Fecha: {self.ui.lblFecha.text()}\n"
            f"Temperatura: {self.ui.lblTempArduino.text()}\n"
            f"Luz: {self.ui.lblLuz.text()}\n"
            f"Estado: {self.ui.lblEstado.text()}\n"
            f"Horas dormidas: {self.ui.label_9.text()}\n"
            f"Clima: {self.ui.lblIconoClima.text()} ({self.ui.lblTemperaturaClima.text()})\n"
        )

        try:
            # Configuración del correo
            remitente = "tu_correo@gmail.com"   # <-- Cambiá esto
            contraseña = "tu_contraseña"        # <-- Y esto (o usá un token)
            destinatario = "destinatario@gmail.com"  # <-- o el mail del usuario logueado

            msg = MIMEMultipart()
            msg["From"] = remitente
            msg["To"] = destinatario
            msg["Subject"] = "Resumen diario - Asistente de Rutina"

            msg.attach(MIMEText(resumen, "plain"))

            # Enviar correo por SMTP
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(remitente, contraseña)
                server.send_message(msg)

            QMessageBox.information(self, "Éxito", "Resumen enviado correctamente por mail.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo enviar el correo:\n{e}")


if __name__ == "__main__": #checkea si el script está siendo ejecutado como el prog principal (no importado como un modulo).
    app = QApplication(sys.argv)    # Crea un Qt widget, la cual va ser nuestra ventana.
    window = MainWindow() #crea una intancia de MainWindow 
    window.show()   # IMPORTANT!!!!! la ventanas estan ocultas por defecto.
    sys.exit(app.exec_()) # Start the event loop.