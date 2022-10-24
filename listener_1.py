import sys


from PySide6 import (
    QtWidgets,
)

from pynput import keyboard

# Subclass QMainWindow to customize your application's main window
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pynput Keyboard Listener Demo")

        label = QtWidgets.QLabel("Press any key!")

        def on_press(key):
            label.setText("You pressed {0}".format(key))

        def on_release(key):
            label.setText("You released {0}".format(key))
        
        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
        listener.start()


        # Set the central widget of the Window.
        self.setCentralWidget(label)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()