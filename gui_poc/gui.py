# -*- coding: utf-8 -*-
from gui_poc.poc import *
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDir, pyqtSignal
from PyQt5.QtGui import QTextCursor, QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog, QMessageBox


class Ui_MainWindow(QtWidgets.QMainWindow):
    my_senddata = pyqtSignal(str)
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.Child_UI=child()
        self.Child_UI.send_msg.connect(self.print_text)
        self.Child_UI.progressbar_signal.connect(self.updata_ProgressBar)






    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 600)
        self.setWindowIcon(QIcon('../image.ico'))
        MainWindow.setFixedSize(self.width(), self.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 110, 811, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 851, 41))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(0, 530, 841, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 741, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setCursorPosition(16)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("redis未授权")
        self.comboBox.addItem("FTP匿名访问")
        self.comboBox.addItem("MongoDB未授权")
        self.comboBox.addItem("Zookeeper未授权")
        self.comboBox.addItem("全量检测")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.changebutton)
        self.pushButton.clicked.connect(self.run)
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.clicked.connect(self.send_data)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.show_Ui_Dialog)
        self.horizontalLayout.addWidget(self.pushButton_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage('作者： 小薛同学')
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.lineEdit)
        self.retranslateUi(MainWindow)




    def changebutton(self):
      if self.pushButton.text()=="运行":
        self.pushButton.setText("运行中")
      elif self.pushButton.text()=="运行中":
         self.pushButton.setText("运行")

    def show_Ui_Dialog(self):

        self.Child_UI.show()
        self.Child_UI.exec_()


    def send_data(self):
        poc_mode = self.comboBox.currentText()
        self.my_senddata.emit(poc_mode)

    def run(self):
        select_poc=self.comboBox.currentText()
        input=self.lineEdit.text()
        if len(input)==0:
            QMessageBox.about(self,'输入错误','ip端口不能为空')
            self.pushButton.setText('运行')
        elif ':' not in input:
            QMessageBox.about(self,'输入错误提示','请输入英文:')
            self.pushButton.setText('运行')
        else:

            index = input.index(':')
            ip = input[:index]
            port = input[index + 1:]
            self.star_work = work_poc()
            self.star_work.ProgressBar_signal.connect(self.updata_ProgressBar)
            res=self.star_work.checkip(input)
            if res !='invalid':

                self.star_work.mode=select_poc
                self.star_work.ip=ip
                self.star_work.port=port
                self.star_work.mysignal.connect(self.print_text)
                self.star_work.ProgressBar_signal.connect(self.updata_ProgressBar)

                self.star_work.start()
            else:
                self.pushButton.setText('运行')

    def inputwaring(self,data):
        QMessageBox.about(self,'输入错误提示',data)

    def updata_ProgressBar(self,number):
        self.progressBar_2.setValue(number)
        self.pushButton.setText("运行中")
        if number==100:
            self.pushButton.setText('运行')
        pass

    def recv_singal(self):
        self.recv = work_poc()
        self.recv.mysignal.connect(self.print_text)

    def print_text(self,data):
        self.textBrowser.insertPlainText(data + '\n')
        self.textBrowser.moveCursor(QTextCursor.End)
        pass



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "未授权检测工具  by___小薛同学"))
        self.label.setText(_translate("MainWindow", "请输入："))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "例：127.0.0.1:1234"))
        self.label_2.setText(_translate("MainWindow", "测试项："))
        self.pushButton.setText(_translate("MainWindow", "运行"))
        self.pushButton_2.setText(_translate("MainWindow", "批量导入"))


class child(QDialog):
    send_msg=pyqtSignal(str)
    progressbar_signal=pyqtSignal(int)
    def __init__(self):
        super(child, self).__init__()
        self.setWindowTitle("123")
        self.setObjectName("Dialog")
        self.resize(623, 473)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 40, 521, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 30, 130, 200))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.selectfile)
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.run)
        # self.pushButton_2.clicked.connect(self.read_file)
        self.pushButton_2.clicked.connect(self.close_window)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("redis未授权")
        self.comboBox.addItem("FTP匿名访问")
        self.comboBox.addItem("MongoDB未授权")
        self.comboBox.addItem("Zookeeper未授权")
        self.comboBox.addItem("全量检测")
        self.verticalLayout.addWidget(self.comboBox)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def close_window(self):
        self.close()
    def selectfile(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            filenames= dialog.selectedFiles()
            f= open(filenames[0],encoding='utf-8')
            with f:
                data = f.read()
                self.textEdit.setText(data)



    def read_file(self):
        count=0
        file=self.textEdit.toPlainText().split('\n')

        for x in file:
            count=count+1
            if ':' not in x:
                QMessageBox.about(self,'输入错误提示','在第'+str(count)+'行发现错误，未使用英文:')
            else:
                index = x.index(':')
                ip = x[:index]
                port = x[index + 1:]
                self.check_work = work_poc()
                res=self.check_work.checkip(x)
                if res=='invalid':
                   QMessageBox.about(self,'输入错误提示','在第'+str(count)+'行发现检测ip书写错误')

                   return 'invalid'
        return 'ok'



    def run(self):
      poc_mode = self.comboBox.currentText()
      res= self.read_file()
      if res=='invalid':
          QMessageBox.about(self,'提示','请重新读取ip文件')
      elif res=='ok':


          file = self.textEdit.toPlainText().split('\n')
          self.start_all = many_run(poc_mode, file)
          self.start_all.mysignal.connect(self.main_gui)
          self.start_all.ProgressBar_signal.connect(self.send_progressbar)
          self.start_all.start()


    def send_progressbar(self,data):
        self.progressbar_signal.emit(data)




    def main_gui(self,data):
        self.send_msg.emit(data)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "选择文件"))
        self.pushButton_2.setText(_translate("Dialog", "确认"))


if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=QMainWindow()
    lohin_aialog=Ui_MainWindow()
    lohin_aialog.setupUi(main)
    main.show()
    sys.exit(app.exec_())