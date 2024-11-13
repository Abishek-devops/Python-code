import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
#QPixmap deals with Pictures
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super(). __init__()
        self.setWindowTitle("Varsha's Pic")
        self.setGeometry(700, 300, 500, 500)
        label=QLabel(self)
        self.setWindowIcon(QIcon("pic.jpg"))
        label.setGeometry(0, 0, 250, 250)
        #This import pic to Pixmap variable
        pixmap=QPixmap("pic.jpg")
        #this imports the pic into label
        label.setPixmap(pixmap)
        #This sets the picture sets in completely
        label.setScaledContents(True)
        #to set the picture in centre of the window
        label.setGeometry((self.width()-label.width())//2,
                          (self.height()-label.height())//2,
                          label.width(),
                          label.height())


def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
main()