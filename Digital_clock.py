import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTime, QTimer

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self)
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(700,300,300,100)

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size:150px;"
                                      "font-family:Arial;"
                                      "color:#2bff00;")
        self.setStyleSheet("background-color:black;")
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
    def update_time(self):
        current_time=QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

def main():
    app=QApplication(sys.argv)
    clock=DigitalClock()
    clock.show()
    sys.exit(app.exec_())
main()