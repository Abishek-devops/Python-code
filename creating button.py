import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        self.button=QPushButton("click here!", self)
        self.button.setGeometry(150,200,200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.button.setText("Clicked!!")
        #To disable once it was clicked
        self.button.setDisabled(True)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
main()