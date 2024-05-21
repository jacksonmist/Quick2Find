from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

app = QApplication([])
window = QWidget()

def main():
    window_config()
    
    
    window.show()
    app.exec_()

def display_text(word, type, definition):
    text = QLabel(window)
    text.setText(f'{word} - {type}\n{definition}')
    text.setFont(QFont("Arial", 16))
    window.show()
    app.exec()
    

def window_config(): 
    window.setWindowOpacity(.7)
    window.setGeometry(0, 0, 0, 0)
    window.setWindowTitle("Quick-To-Find")
    window.setMinimumSize(400, 200)
    return window
    

main()