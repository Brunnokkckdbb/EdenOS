import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QImage, QPixmap, QPalette, QColor
from PyQt5.QtCore import Qt, QTimer

class SingleCameraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visor de Una Cámara")

        self.camera_index = 0  # Puedes cambiar esto al índice de la cámara que quieras mostrar
        self.camera_feed = cv2.VideoCapture(self.camera_index)

        if not self.camera_feed.isOpened():
            print(f"No se pudo abrir la cámara con índice {self.camera_index}")
            sys.exit()

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        palette = self.image_label.palette()
        palette.setColor(QPalette.Window, Qt.black)
        self.image_label.setAutoFillBackground(True)
        self.image_label.setPalette(palette)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Actualizar cada 30 ms

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

    def update_frame(self):
        """Actualiza el frame de la cámara en la etiqueta."""
        ret, frame = self.camera_feed.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            convert_to_qt_format = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
            p = convert_to_qt_format.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio)
            self.image_label.setPixmap(QPixmap.fromImage(p))

    def closeEvent(self, event):
        """Libera la cámara al cerrar la aplicación."""
        if self.camera_feed.isOpened():
            self.camera_feed.release()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SingleCameraApp()
    window.showMaximized() # Puedes iniciar la ventana maximizada
    sys.exit(app.exec_())