import sys
import json
import os
import urllib.request
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from sub_prueba import Ui_MainWindow
from Tp_Final import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Archivo de usuarios
        self.archivo_usuarios = "usuarios.json"
        if not os.path.exists(self.archivo_usuarios):
            with open(self.archivo_usuarios, "w") as f:
                json.dump([], f)

    def crear_cuenta(self):
        print("Crear cuenta")
        nombre = self.ui.txtNombre.text().strip()
        correo = self.ui.txtMail.text().strip()
        password = self.ui.txtPass.text().strip()

        if not nombre or not correo or not password:
            self.mostrar_mensaje("Por favor complete todos los campos", "error")
            return

        with open(self.archivo_usuarios, "r") as f:
            usuarios = json.load(f)

        for usuario in usuarios:
            if usuario["correo"] == correo:
                self.mostrar_mensaje("Error: el correo ya está registrado", "error")
                return

        usuarios.append({
            "nombre": nombre,
            "correo": correo,
            "password": password
        })

        with open(self.archivo_usuarios, "w") as f:
            json.dump(usuarios, f, indent=4)

        self.mostrar_mensaje(" Cuenta creada con éxito", "exito")

    def iniciar_sesion(self):
        print("iniciar sesion")
        correo = self.ui.txtMail.text().strip()
        password = self.ui.txtPass.text().strip()

        with open(self.archivo_usuarios, "r") as f:
            usuarios = json.load(f)

        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                self.mostrar_mensaje(f"Bienvenido, {usuario['nombre']} 👋", "exito")
                self.abrir_ventana_principal(usuario["nombre"])
                return

        self.mostrar_mensaje("Correo o contraseña incorrectos", "error")

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
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Mostrar mensaje de bienvenida si existe el label
        if hasattr(self.ui, "lblBienvenida"):
            self.ui.lblBienvenida.setText(f"¡Bienvenido, {nombre_usuario}! ")


        # --- Mostrar hora y clima iniciales ---
        self.actualizar_datos()
        self.actualizar_clima()

    # === BOTÓN SALIR ===
    def salir(self):
        self.close()

    # === BOTÓN ACTUALIZAR DATOS ===
    def actualizar_datos(self):
        ahora = datetime.now()
        self.ui.lblHora.setText(ahora.strftime("%H:%M:%S"))
        self.ui.lblFecha.setText(ahora.strftime("%d/%m/%Y"))

    # === BOTÓN ACTUALIZAR CLIMA ===
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


# ========== BLOQUE PRINCIPAL ==========
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
