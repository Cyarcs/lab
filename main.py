import PyQt5
from PyQt5 import QtWidgets
from equip import Ui_MainWindow  # импорт нашего сгенерированного файла
from ls_equip import Ui_ls_equip
import sys
import xlrd

book = xlrd.open_workbook('New_List_of_lab_Equipmemt_05.04.19.xlsx')
sheet = book.sheets()[0]

data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.data = data
        self.ui.setupUi(self)



class ls(QtWidgets.QMainWindow):

    def __init__(self):
        super(ls, self).__init__()
        self.ui = Ui_ls_equip()
        self.ui.setupUi(self)
        self.ui.Delete.clicked.connect(self.dell)
        self.ui.pushButton.clicked.connect(self.add_equio)


    def dell(self):
        pass
        rowww = self.ui.listWidget.currentRow()
        self.ui.listWidget.takeItem(rowww)

    def add_equio(self):
        pass
        self.qq = mywindow()
        self.qq.ui.tableWidget.setColumnCount(len(self.qq.data[0][:3]))
        self.qq.ui.tableWidget.setRowCount(len(self.qq.data) - 1)
        self.qq.ui.tableWidget.setHorizontalHeaderLabels(self.qq.data[0][:3])
        self.qq.ui.pushButton.clicked.connect(self.qq.close)
        self.qq.ui.tableWidget.setSelectionMode(self.qq.ui.tableWidget.SingleSelection)
        self.qq.ui.tableWidget.setEditTriggers(self.qq.ui.tableWidget.NoEditTriggers)
        # заполняем таблицу из экселя
        for i in range(len(self.qq.data)):
            for z in range(len(self.qq.data[i])):
                if i > 49:
                    break
                # print(self.qq.data[i + 1][z])
                self.qq.ui.tableWidget.setItem(i, z, PyQt5.QtWidgets.QTableWidgetItem(str(self.qq.data[i + 1][z])))
        self.qq.ui.tableWidget.resizeColumnsToContents()
        self.qq.ui.gridLayout.sizeConstraint()
        self.qq.ui.tableWidget.itemDoubleClicked.connect(self.qasw)
        self.qq.show()

    def qasw(self):
        rows1 = self.qq.ui.tableWidget.currentColumn()
        cols1 = self.qq.ui.tableWidget.currentRow()
        self.qwe = self.qq.ui.tableWidget.item(cols1, rows1).text()
        self.ui.listWidget.addItem(str(self.qwe))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = ls()
    application.show()

    sys.exit(app.exec())
