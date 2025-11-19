import sys
import json
import os
import urllib.request
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QTimer   # ★★★ AGREGADO QTimer
from ui_main import Ui_MainWindow as uiMain
from ui_datos import Ui_MainWindow as uiDatos
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# ★★★ Arduino
import serial


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



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uiMain()
        self.ui.setupUi(self)

    def iniciar_sesion(self):
        print("iniciar sesion")
        correo = self.ui.txtMail.text().strip()
        password = self.ui.txtPass.text().strip()

        usuarios = get_database()

        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                self.mostrar_mensaje(f"Bienvenido, {usuario['nombre']} 👋", "exito")
                self.abrir_ventana_principal(usuario["nombre"], usuario["correo"])
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
        
    def abrir_ventana_principal(self, nombre_usuario, correo_usuario):
        self.ventana_principal = VentanaPrincipal(nombre_usuario, correo_usuario)
        self.ventana_principal.show()
        self.close()



# =======================================================================
# ========================== VENTANA PRINCIPAL ===========================
# =======================================================================

class VentanaPrincipal(QMainWindow):
    def __init__(self, nombre_usuario, correo_usuario):
        super().__init__()
        self.ui = uiDatos()
        self.ui.setupUi(self)

        self.nombre_usuario = nombre_usuario
        self.correo_usuario = correo_usuario

        if hasattr(self.ui, "lblBienvenida"):
            self.ui.lblBienvenida.setText(f"¡Bienvenido, {nombre_usuario}! ")

        self.ui.btnSalir.clicked.connect(self.salir)

        # -------------------------
        # MOSTRAR DATOS INICIALES
        # -------------------------
        self.actualizar_datos()
        self.actualizar_clima()

        # ★★★ TIMER PARA ACTUALIZAR HORA AUTOMÁTICA
        self.timer_hora = QTimer()
        self.timer_hora.timeout.connect(self.actualizar_datos)
        self.timer_hora.start(1000)   # cada 1 segundo

        # ★★★ CONECTAR A ARDUINO
        try:
            self.arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
        except:
            self.arduino = None
            QMessageBox.warning(self, "Arduino", "No se pudo conectar al Arduino.")

        # ★★★ TIMER PARA LEER ARDUINO
        self.timer_arduino = QTimer()
        self.timer_arduino.timeout.connect(self.leer_arduino)
        self.timer_arduino.start(1000)


    # === SALIR ===
    def salir(self):
        if hasattr(self, "arduino") and self.arduino:
            self.arduino.close()   # ★★★ cerrar puerto
        self.close()


    # === ACTUALIZAR CLIMA ===
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

    # === ACTUALIZAR HORA ===
    def actualizar_datos(self):
        ahora = datetime.now()
        self.ui.lblHora.setText(ahora.strftime("%H:%M:%S"))
        self.ui.lblFecha.setText(ahora.strftime("%d/%m/%Y"))


    # ★★★ LEER ARDUINO
    def leer_arduino(self):
        if not self.arduino:
            return

        try:
            linea = self.arduino.readline().decode().strip()

            if linea == "":
                return

            partes = linea.split("|")
            datos = {}

            for p in partes:
                k, v = p.split(":")
                datos[k] = v

            self.ui.lblTempArduino.setText(datos.get("TEMP", "--") + " °C")
            self.ui.lblLuz.setText(datos.get("LUZ", "--"))
            self.ui.lblEstado.setText(datos.get("ESTADO", "--"))
            self.ui.label_9.setText(datos.get("SUEÑO", "--") + " Hs")

        except Exception as e:
            print("Error leyendo Arduino:", e)


    # === ENVIAR RESUMEN ===
    def enviar_resumen(self):
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
            remitente = "t.buttazzoni.solis@itsv.edu.ar"
            contraseña = "ewyoglgcdjsykzgp"
            destinatario = self.correo_usuario

            msg = MIMEMultipart()
            msg["From"] = remitente
            msg["To"] = destinatario
            msg["Subject"] = "Resumen diario - Asistente de Rutina"
            msg.attach(MIMEText(resumen, "plain"))

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(remitente, contraseña)
                server.send_message(msg)

            QMessageBox.information(self, "Éxito", "Resumen enviado correctamente por mail.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo enviar el correo:\n{e}")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
