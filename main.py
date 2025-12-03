import sys
import json
import os
import urllib.request
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QTimer 
from ui_main import Ui_MainWindow as uiMain
from ui_datos import Ui_MainWindow as uiDatos
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLineEdit
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
        self.ui.label.setPixmap(QPixmap("Mydaylogo.png"))
        self.ui.txtPass.setEchoMode(QLineEdit.EchoMode.Password)

    def iniciar_sesion(self):
        print("iniciar sesion")
        correo = self.ui.txtMail.text().strip()
        password = self.ui.txtPass.text().strip()

        if not correo or not password:
            self.mostrar_mensaje("Por favor complete los campos de ingreso" , "error")
            return

        usuarios = get_database()
        encontrado = False

        for usuario in usuarios:
            if usuario["correo"] == correo:
                encontrado = True

        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                self.mostrar_mensaje(f"Bienvenido, {usuario['nombre']} 👋", "exito")
                self.abrir_ventana_principal(usuario["nombre"], usuario["correo"])
                return
            
        if encontrado == False:
            self.mostrar_mensaje("Error, el correo no esta registrado en MyDay", "error")
        else:
            self.mostrar_mensaje("Error: Contraseña incorrecta", "error")


    def crear_cuenta(self):
        print("Crear cuenta")
        nombre = self.ui.txtNombre.text().strip()
        correo = self.ui.txtMail.text().strip()
        password = self.ui.txtPass.text().strip()

        if not nombre or not correo or not password:
            self.mostrar_mensaje("Por favor complete todos los campos", "error")
            return
        
        if ("@gmail.com" not in correo and 
            "@hotmail.com" not in correo and 
            "@itsv.edu.ar" not in correo):
            self.mostrar_mensaje("Error el mail es inválido", "error")
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


# VENTANA PRINCIPAL 


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

        self.actualizar_datos()
        self.actualizar_clima()

        self.timer_hora = QTimer()
        self.timer_hora.timeout.connect(self.actualizar_datos)
        self.timer_hora.start(1000)   # cada 1 segundo

        try:
            self.arduino = serial.Serial("COM4", 9600, timeout=1)
        except:
            self.arduino = None
            QMessageBox.warning(self, "Arduino", "No se pudo conectar al Arduino.")

        self.timer_arduino = QTimer()
        self.timer_arduino.timeout.connect(self.leer_arduino)
        self.timer_arduino.start(1000)


    def salir(self):
        if hasattr(self, "arduino") and self.arduino:
            self.arduino.close()  
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

    def actualizar_datos(self):
        ahora = datetime.now()
        self.ui.lblHora.setText(ahora.strftime("%H:%M:%S"))
        self.ui.lblFecha.setText(ahora.strftime("%d/%m/%Y"))


    def leer_arduino(self):
        if not self.arduino:
            return

        ultima_linea_valida = None
        while self.arduino.in_waiting > 0:
            try:
                linea = self.arduino.readline().decode('utf-8', errors='ignore').strip()
                if linea: ultima_linea_valida = linea
            except: pass

        if not ultima_linea_valida: return

        if "|" not in ultima_linea_valida: return

        try:
            partes = ultima_linea_valida.split("|")
            datos = {}
            for p in partes:
                if ":" in p:
                    k, v = p.split(":")
                    datos[k] = v

            if "TEMP" in datos:
                self.ui.lblTempArduino.setText(datos["TEMP"] + " °C")

            if "LDR" in datos:
                try:
                    val = int(datos["LDR"])
                    self.ui.lblLuz.setText("Noche 🌑" if val < 100 else "Día ☀️")
                except: pass

            if "ESTADO" in datos:
                self.ui.lblEstado.setText(datos["ESTADO"])

            if "SUEÑO" in datos:
                try:
                    total_segundos = float(datos["SUEÑO"])
                    total_segundos = int(total_segundos)
                    
                    horas = total_segundos // 3600
                    minutos = (total_segundos % 3600) // 60
                    segundos = total_segundos % 60
                    
                    if horas > 0:
                        texto_tiempo = f"{horas} h {minutos} m {segundos} s"
                    elif minutos > 0:
                        texto_tiempo = f"{minutos} m {segundos} s"
                    else:
                        texto_tiempo = f"{segundos} s"
                        
                    self.ui.label_9.setText(texto_tiempo)
                    
                except: 
                    self.ui.label_9.setText("0 s")

        except Exception as e:
            print("Error:", e)


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
