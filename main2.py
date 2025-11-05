import sys
import json
import urllib.request
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Tp_Final import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- Conectar botones ---
        self.ui.btnSalir.clicked.connect(self.salir)
        self.ui.btnActualizar.clicked.connect(self.actualizar_datos)
        self.ui.btnActualizarClima.clicked.connect(self.actualizar_clima)

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

            # Pedimos los datos sin usar 'requests'
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
        """Convierte el código numérico del clima en una descripción legible."""
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


# === BLOQUE PRINCIPAL ===
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())