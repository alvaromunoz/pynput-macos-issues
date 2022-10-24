import sys

from PySide6 import (
    QtWidgets,
)

from pynput import keyboard

class MyListener():

    def __init__(self, label: QtWidgets.QLabel):

        def on_press(key):
            label.setText("You pressed {0}".format(key))

        def on_release(key):
            label.setText("You released {0}".format(key))

        self.listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
        
    def start(self):
        self.listener.start()
        self.listener.wait()
        print("listener has started? {0}".format(self.listener.running))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Listener Demo 2")

        central_widget = QtWidgets.QWidget()

        layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(layout)

        label_description = QtWidgets.QLabel("Press the button to crash")
        layout.addWidget(label_description)

        label = QtWidgets.QLabel("Press any key")
        label.setEnabled(False)
        layout.addWidget(label)

        button = QtWidgets.QPushButton("Start listener!")
        button.pressed.connect(self.start_listener)
        layout.addWidget(button)
        
        self.listener = MyListener(label)

        self.setCentralWidget(central_widget)

    def start_listener(self):
        print("beep")
        self.listener.start()
        print("boop")

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()