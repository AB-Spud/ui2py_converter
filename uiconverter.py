# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Owner/Documents/python-projects/converter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

dirs = {'source': None, 'output': None, 'file': None}

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(549, 194)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.selectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectBtn.setGeometry(QtCore.QRect(0, 0, 101, 31))
        self.selectBtn.setObjectName("selectBtn")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(100, 0, 431, 111))
        self.listWidget.setObjectName("listWidget")
        self.createBtn = QtWidgets.QPushButton(self.centralwidget)
        self.createBtn.setGeometry(QtCore.QRect(0, 60, 101, 31))
        self.createBtn.setObjectName("createBtn")
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(0, 110, 531, 45))
        self.exitBtn.setObjectName("exitBtn")
        self.destinationBtn = QtWidgets.QPushButton(self.centralwidget)
        self.destinationBtn.setGeometry(QtCore.QRect(0, 30, 101, 31))
        self.destinationBtn.setObjectName("destinationBtn")
        self.openBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openBtn.setGeometry(QtCore.QRect(0, 90, 101, 23))
        self.openBtn.setObjectName("openBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.selectBtn.clicked.connect(self.selectFile)
        self.destinationBtn.clicked.connect(self.destinationDir)
        self.exitBtn.clicked.connect(sys.exit)
        self.createBtn.clicked.connect(self.create_py)
        self.openBtn.clicked.connect(self.openLocation)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Converter .ui to .py"))
        self.selectBtn.setText(_translate("MainWindow", "Select File"))
        self.createBtn.setText(_translate("MainWindow", "Create .py"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.destinationBtn.setText(_translate("MainWindow", "Destination"))
        self.openBtn.setText(_translate("MainWindow", "Open Location"))

    def clearDic(self):
        dirs['source'] = None
        dirs['output'] = None
        dirs['file'] =  None
     
    def selectFile(self):
        if dirs['output']:
            dirs['source'] = None; dirs['output'] = None; dirs['file'] =  None
        else:
            pass
        self.listWidget.clear()
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select .ui File", "", ".ui Files (*.ui)")

        dirs['source'] = str(self.filename)

        self.listWidget.addItem(f"From: {str(self.filename)}")
        self.file_name = str(self.filename).split('/')[-1].replace('.ui', '.py')

        dirs['file'] = self.file_name.replace(' ', '')
    
    def destinationDir(self, clearDic):
        if dirs['source']:
            if dirs['output']:
                self.listWidget.clear()
                self.dirname = QtWidgets.QFileDialog.getExistingDirectory()
                self.listWidget.addItem(f"From: {dirs['source']}")
                self.listWidget.addItem(f"To: {str(self.dirname)}")

                if self.dirname.replace(' ', '') == '':
                    dirs['source'] = None; dirs['output'] = None; dirs['file'] =  None
                    self.listWidget.clear()
                    self.listWidget.addItem('Invalid Directory.')
                else:
                    dirs['output'] = str(self.dirname) + '/' + dirs['file'].replace(' ', '')

            else:
                self.dirname = QtWidgets.QFileDialog.getExistingDirectory()
                self.listWidget.addItem(f"To: {str(self.dirname)}")   

                if self.dirname.replace(' ', '') == '':
                    dirs['source'] = None; dirs['output'] = None; dirs['file'] =  None
                    self.listWidget.clear()
                    self.listWidget.addItem('Invalid Directory.')
                else:
                    dirs['output'] = str(self.dirname) + '/' + dirs['file'].replace(' ', '')
        else:
            self.listWidget.clear()
            self.listWidget.addItem("Please select a file to convert first!")
    
    def create_py(self):
        if dirs['source'] and dirs['output']:
            try:
                os.system(f"pyuic5 -x {dirs['source']} -o {dirs['output']}")
            except Exception as ex:
                self.listWidget.addItem(ex)

            if os.path.isfile(dirs['output']):
                self.listWidget.clear()
                self.listWidget.addItem(f"Directory: {dirs['output']}")
                self.listWidget.addItem(f"Successfully created {dirs['file']}!")
            else:
                dirs['source'] = None; dirs['output'] = None; dirs['file'] =  None
                self.listWidget.clear()
                self.listWidget.addItem('Creation Failed.', 'Most likely null directory selected.')

        else:
            self.listWidget.addItem('Error: Missing args (file.ui and directory.)')

    def openLocation(self):
        if os.path.isfile(dirs['output']):
            self.listWidget.addItem('Opening Directory...')
            os.system(f"start {os.path.realpath(dirs['output'])}")
        else:
            self.listWidget.addItem('Unable to open directory because it does not exist')

if __name__ == "__main__":
    import sys; import os; import os.path; import time
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
