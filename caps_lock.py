import sys

from PySide6 import (
    QtWidgets,
)

from pynput import keyboard

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Listener Demo 1")

        central_widget = QtWidgets.QWidget()

        layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(layout)

        label_description = QtWidgets.QLabel("Press Caps lock to crash.")
        layout.addWidget(label_description)

        label = QtWidgets.QLabel("Press any key")
        layout.addWidget(label)

        def on_press(key):
            label.setText("You pressed {0}".format(key))

        def on_release(key):
            label.setText("You released {0}".format(key))
        
        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
        listener.start()

        self.setCentralWidget(central_widget)

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()