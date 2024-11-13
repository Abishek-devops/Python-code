import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
#to import a icon to the prompt
from PyQt5.QtGui import QIcon, QFont
#to import the alignment
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #.setWindowTitle sets a Title for the prompt
        self.setWindowTitle("My First code")
        #self.setGeometry(x, y, width, height)
        self.setGeometry(700, 300, 500, 500)
        # the below code import the icon for the prompt if it is added
        #self.setWindowIcon(QIcon("profile_pic.jpg"))
        label=QLabel("Hello", self)
        #Below line sets the font style and size
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0, 0, 500, 100)
        #below line set a font color we can also give RGB values for unique color
        label.setStyleSheet("color:Black;"
                            "background-color:Red;"
                            "font-weight:bold;"
                            "font-style:italic;"
                            "text-decoration:underline;")
        #label.setAlignment(Qt.AlignTop) #this aligns the text vertically to top
        #label.setAlignment(Qt.AlignBottom) #this aligns the text vertically to Bottom
        #label.setAlignment(Qt.AlignVCenter) #this aligns the text vertically to centre

        #label.setAlignment(Qt.AlignRight) #this aligns the text horizontally to Right
        #label.setAlignment(Qt.AlignHCenter)  # this aligns the text horizontally to centre
        #label.setAlignment(Qt.AlignLeft)  # this aligns the text horizontally to Left

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #this aligns text Horiz centre nd vertically top

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
main()