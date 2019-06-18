#Author - Min Thet Naung
#License - Open Source
#Language - Python, PyQT5
#If you want to use this code, please kindly give me some credits. Thanks
#Program is implemented on 18/June/2019


import sys
from PyQt5.QtWidgets import* 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title  = "BMI Program"
        self.left   = 200
        self.top    = 200
        self.width  = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('bmi_logo.ico'))
        #create a menu bar
        mainMenu    = self.menuBar()
        fileMenu    = mainMenu.addMenu("File")

        #add category button to the menu bar File
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        #Calculation and GUI part

        label0 = QLabel(self)
        label0.setText("Body Mass Index (BMI) Calculation Program Written in Python") #You can try putting your name as the one to implement this system
        label0.setGeometry(0,80,1000,100)
        label0.move(50,0)
        
        label1 = QLabel(self)
        label1.setText("Enter height:")
        label1.move(30,95)
        
        label2 = QLabel(self)
        label2.setText("Enter weight:")
        label2.move(30,145)

        #create a textbox for input
        self.height_input = QLineEdit(self)
        self.height_input.move(100, 100)
        self.height_input.resize(50, 20)

        self.weight_input = QLineEdit(self)
        self.weight_input.move(100, 150)
        self.weight_input.resize(50, 20)

        #creat a Calculate Button in the window
        self.cal_button = QPushButton("Calculate", self)
        self.cal_button.setToolTip("This is to calculate the result.") #this info will pop-up when a user put mouse censor on the button
        self.cal_button.move(100, 180)

        label3 = QLabel(self)
        label3.setText("Developed by Min Thet Naung.")
        label3.move(30,230)
        label3.setFixedWidth(200)
        label3.show()

        label4 = QLabel(self)
        label4.setText("lbs (Pound(s))")
        label4.move(160,145)

        label5 = QLabel(self)
        label5.setText("inches")
        label5.move(160,95)
        
        #connect button to function on_click
        self.cal_button.clicked.connect(self.on_click)
        
        self.show()

   
    def on_click(self):    
        
        if str(self.weight_input.text()) =="" and str(self.height_input.text()) =="":
            QMessageBox.warning(self, 'Oops...No Data to calculate!', "You didn't key in any data at all. Please fill in again! ", QMessageBox.Ok)

        elif str(self.weight_input.text()) =="" and str(self.height_input.text()) !="":            
            QMessageBox.warning(self, 'Oops...No Weight value!', "You didn't key in your weight value into the textbox! ", QMessageBox.Ok)

        elif str(self.height_input.text()) =="" and str(self.weight_input.text()) !="":            
            QMessageBox.warning(self, 'Oops...No Height value!', "You didn't key in your height value into the textbox! ", QMessageBox.Ok)
       
        else:
            weight = float(self.weight_input.text())
            height = float(self.height_input.text())
            if ((weight / (height * height) * 703)) < 18.5:

                QMessageBox.information(self, 'Result', "Your BMI result is: " + str('%.2f' %(weight / (height * height) * 703)) + "\n Category: Underweight", QMessageBox.Ok)

            
            elif ((weight / (height * height) * 703)) < 25 and ((weight / (height * height) * 703)) >= 18.5:
                
                QMessageBox.information(self, 'Result', "Your BMI result is: " + str('%.2f' %(weight / (height * height) * 703)) + "\n Category: Normal weight", QMessageBox.Ok)


            elif ((weight / (height * height) * 703)) < 30 and ((weight / (height * height) * 703)) >= 25:
                
                QMessageBox.information(self, 'Result', "Your BMI result is: " + str('%.2f' %(weight / (height * height) * 703)) + "\n Category: Overweight", QMessageBox.Ok)

            else:
                QMessageBox.information(self, 'Result', "Your BMI result is: " + str('%.2f' %(weight / (height * height) * 703)) + "\n Category: Obesity", QMessageBox.Ok)
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

