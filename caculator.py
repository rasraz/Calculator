from PyQt5 import QtWidgets,QtCore,QtGui
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.UiApp()
        self.show()

    def UiApp(self):
        self.setGeometry(100,100,235,340)
        self.setMinimumWidth(235)
        self.setMaximumWidth(235)
        self.setMinimumHeight(340)
        self.setMaximumHeight(340)

        self.monitor=QtWidgets.QLabel("hello world",self)
        self.monitor.setGeometry(10,10,215,45)
        self.monitor.setFont(QtGui.QFont('Arial', 20))
        self.monitor.setAlignment(QtCore.Qt.AlignRight)
        self.monitor.setStyleSheet('background-color:red;border-radius:10px;padding:3px;')

        buttonClear=QtWidgets.QPushButton('C',self)
        buttonClear.setGeometry(10,60,50,50)
        buttonClear.clicked.connect(lambda:self.calculable(buttonClear.text()))

        buttonDivision=QtWidgets.QPushButton('/',self)
        buttonDivision.setGeometry(175,60,50,50)
        buttonDivision.clicked.connect(lambda:self.calculable(buttonDivision.text()))
        button1=QtWidgets.QPushButton('1',self)
        button1.setGeometry(10,115,50,50)
        button1.clicked.connect(lambda:self.calculable(button1.text()))
        button2=QtWidgets.QPushButton('2',self)
        button2.setGeometry(65,115,50,50)
        button2.clicked.connect(lambda:self.calculable(button2.text()))
        button3=QtWidgets.QPushButton('3',self)
        button3.setGeometry(120,115,50,50)
        button3.clicked.connect(lambda:self.calculable(button3.text()))
        buttonMul=QtWidgets.QPushButton('*',self)
        buttonMul.setGeometry(175,115,50,50)
        buttonMul.clicked.connect(lambda:self.calculable(buttonMul.text()))
        button4=QtWidgets.QPushButton('4',self)
        button4.setGeometry(10,170,50,50)
        button4.clicked.connect(lambda:self.calculable(button4.text()))
        button5=QtWidgets.QPushButton('5',self)
        button5.setGeometry(65,170,50,50)
        button5.clicked.connect(lambda:self.calculable(button5.text()))
        button6=QtWidgets.QPushButton('6',self)
        button6.setGeometry(120,170,50,50)
        button6.clicked.connect(lambda:self.calculable(button6.text()))
        buttonSub=QtWidgets.QPushButton('-',self)
        buttonSub.setGeometry(175,170,50,50)
        buttonSub.clicked.connect(lambda:self.calculable(buttonSub.text()))
        button7=QtWidgets.QPushButton('7',self)
        button7.setGeometry(10,225,50,50)
        button7.clicked.connect(lambda:self.calculable(button7.text()))
        button8=QtWidgets.QPushButton('8',self)
        button8.setGeometry(65,225,50,50)
        button8.clicked.connect(lambda:self.calculable(button8.text()))
        button9=QtWidgets.QPushButton('9',self)
        button9.setGeometry(120,225,50,50)
        button9.clicked.connect(lambda:self.calculable(button9.text()))
        buttonAdd=QtWidgets.QPushButton('+',self)
        buttonAdd.setGeometry(175,225,50,50)
        buttonAdd.clicked.connect(lambda:self.calculable(buttonAdd.text()))
        buttonDelete=QtWidgets.QPushButton('D',self)
        buttonDelete.setGeometry(10,280,50,50)
        buttonDelete.clicked.connect(lambda:self.calculable(buttonDelete.text()))
        button0=QtWidgets.QPushButton('0',self)
        button0.setGeometry(65,280,50,50)
        button0.clicked.connect(lambda:self.calculable(button0.text()))
        buttonDot=QtWidgets.QPushButton('.',self)
        buttonDot.setGeometry(120,280,50,50)
        buttonDot.clicked.connect(lambda:self.calculable(buttonDot.text()))
        buttonEqual=QtWidgets.QPushButton('=',self)
        buttonEqual.setGeometry(175,280,50,50)
        buttonEqual.clicked.connect(self.equally)

    def calculable(self,text):
        textMonitor=self.monitor.text()
        if textMonitor=='hello world':textMonitor=''
        if text=='D':textMonitor=textMonitor[:len(textMonitor)-1]
        elif text=='C':textMonitor=''
        else:textMonitor+=text
        self.monitor.setText(textMonitor)

    def equally(self):
        textMonitor=eval(self.monitor.text())
        self.monitor.setText(str(textMonitor))

app=QtWidgets.QApplication(sys.argv)
win=Window()
sys.exit(app.exec_())
