import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from chiffrement import *


def window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(200,200,500,250)
    w.setWindowTitle('Chiffrement de Message')
    
    L1 = QLabel("Entrez le massage à chiffrer")
    L2 = QLabel("Choisissez le décallage")
    L3 = QLabel()
    L4 = QLabel('Message chiffré')
    
    msg = QLineEdit()
    decal = QSpinBox()
    btncrypte = QPushButton("Chiffrer")
    reset = QPushButton("Reset")
    
    v1 = QVBoxLayout()
    v1.addWidget(L1)
    v1.addWidget(msg)
    
    v2 = QVBoxLayout()
    v2.addWidget(L2)
    v2.addWidget(decal)
    
    v3 = QHBoxLayout()
    v3.addWidget(btncrypte)
    v3.addWidget(reset)
    
    v4 = QVBoxLayout()
    v4.addWidget(L4)
    v4.addWidget(L3)
    
    fbox = QFormLayout()
    fbox.addRow(v1)
    fbox.addRow(v2)
    fbox.addRow(v3)
    fbox.addRow(v4)
    
    L5 = QLabel("Entrez le massage à déchiffrer")
    L6 = QLabel("Choisissez le décallage")
    L7 = QLabel()
    L8 = QLabel('Message déchiffré')
    
    msgdecrypte = QLineEdit()
    decal2 = QSpinBox()
    btndecrypte = QPushButton("Déchiffer")
    decryptreset = QPushButton("Reset")
    
    v5 = QVBoxLayout()
    v5.addWidget(L5)
    v5.addWidget(msgdecrypte)
    
    v6 = QVBoxLayout()
    v6.addWidget(L6)
    v6.addWidget(decal2)
    
    v7 = QHBoxLayout()
    v7.addWidget(btndecrypte)
    v7.addWidget(decryptreset)
    
    v8 = QVBoxLayout()
    v8.addWidget(L8)
    v8.addWidget(L7)
    
    fbox2 = QFormLayout()
    fbox2.addRow(v5)
    fbox2.addRow(v6)
    fbox2.addRow(v7)
    fbox2.addRow(v8)
    
    stack1 = QWidget()
    stack2 = QWidget()
    
    stack1.setLayout(fbox)
    stack2.setLayout(fbox2)
    
    stackwidget = QStackedWidget()
    stackwidget.addWidget(stack1)
    stackwidget.addWidget(stack2)
    
    page1 = QPushButton("Chiffer un message ")
    page1.clicked.connect(lambda: showpage1(stackwidget))
    page2 = QPushButton("Déchiffer un message ")
    page2.clicked.connect(lambda: showpage2(stackwidget))
    
    layout = QVBoxLayout()
    layout.addWidget(stackwidget)
    layout.addSpacing(50)
    layout.addWidget(page1)
    layout.addWidget(page2)
    
    reset.clicked.connect(lambda: reset_func(L3,msg)) 
    btncrypte.clicked.connect(lambda: cryptographie(msg.text(),L3,decal.value()))
    btndecrypte.clicked.connect(lambda:decryptographie(msgdecrypte.text(),L7,decal2.value()))
    decryptreset.clicked.connect(lambda: reset_func(L7,msgdecrypte))
    
    w.setLayout(layout)
    w.show()
    
    sys.exit(app.exec_())
   
 
def cryptographie(message,l,d):
   msgc = crypte(message,d)
   l.setText(msgc)
   
def decryptographie(message,l,d):
   msgc = decrypte(message,d)
   l.setText(msgc)
     
def reset_func(label,inputl):
    clin(label)
    clin(inputl)
    
def showpage1(stack):
    stack.setCurrentIndex(0)
    
def showpage2(stack):
    stack.setCurrentIndex(1)

if __name__ == '__main__':
    window()