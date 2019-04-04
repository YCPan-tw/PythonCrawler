import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QApplication, QHBoxLayout
from myui import Ui_Dialog
from myCrawler import initurllist,getdata

class MyDlg(QDialog):
    def __init__(self):
        super(MyDlg, self).__init__() 
        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # new method
        #https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/433908/
        self.ui.buttonBox.accepted.connect(lambda: self.onButtonClick(self.ui.lineEdit.text(),self.ui.lineEdit_2.text(),self.ui.lineEdit_3.text()))

    def onButtonClick(self,crypto_name,sdate,edate):
        
        cryto_dict = initurllist(crypto_name,sdate,edate)
        getdata(cryto_dict)
        #print(crypto_name,"data is download")  
        QMessageBox.information(self, "Notification", crypto_name+" data is download")

def main_start():
    app = QApplication(sys.argv)
    window = MyDlg()
    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main_start()