from gui_poc.gui import *
from PyQt5.QtWidgets import  *



if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=QMainWindow()
    lohin_aialog=Ui_MainWindow()
    lohin_aialog.setupUi(main)
    main.show()
    sys.exit(app.exec_())