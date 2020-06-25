import PyQt5
from PyQt5 import QtWidgets
from equip import Ui_MainWindow  # импорт нашего сгенерированного файла
from ls_equip import Ui_ls_equip
from zaivka import Ui_zaivka
import sys
import xlrd
import time
book = xlrd.open_workbook('New_List_of_lab_Equipmemt_05.04.19.xlsx')
sheet = book.sheets()[0]

data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

# line=[ self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.lineEdit_4.text(), self.ui.lineEdit_5.text()]
# list=['listWidget','listWidget_2','listWidget_4','listWidget_5']
# widget=['widget','widget_2','widget_4','widget_5']

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.data = data
        self.ui.setupUi(self)

class zaivka(QtWidgets.QMainWindow):
    def __init__(self):
        super(zaivka, self).__init__()
        self.ui = Ui_zaivka()
        self.data = data
        self.ui.setupUi(self)
        self.ui.Delete.clicked.connect(self.dell)
        self.ui.Add.clicked.connect(self.add_equio)
        self.ui.add_projeck.clicked.connect(self.add_projeck)
        self.ui.add_workplace.clicked.connect(self.add_workplace)
        self.ui.add_team.clicked.connect(self.add_team)
        self.ui.add_task.clicked.connect(self.add_task)
        self.ui.listWidget.itemDoubleClicked.connect(self.dell_add_projeck)
        self.ui.listWidget_2.itemDoubleClicked.connect(self.dell_add_workplace)
        self.ui.listWidget_4.itemDoubleClicked.connect(self.dell_add_team)
        self.ui.listWidget_5.itemDoubleClicked.connect(self.dell_add_task)
        self.ui.add_zaivka.clicked.connect(self.add_zaivka)
        # self.list = [self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.lineEdit_4.text(), self.ui.lineEdit_5.text()]
        # self.clear = [self.ui.lineEdit.clear(), self.ui.lineEdit.clear(), self.ui.lineEdit.clear(), self.ui.lineEdit.clear()]

    def add_zaivka(self):
        projeck = self.ui.listWidget.count()
        workplace = self.ui.listWidget_2.count()
        equip = self.ui.listWidget_3.count()
        team = self.ui.listWidget_4.count()
        task = self.ui.listWidget_5.count()
        print(projeck)
        print(workplace)
        print(equip)
        print(team)
        print(task)
        if projeck!=0 and workplace!=0 and equip!=0 and team!=0 and task!=0:
            items_all=[]
            items_projeck = []
            items_workplace = []
            items_equip = []
            items_team = []
            items_task = []
            for i in range(projeck):
                item = self.ui.listWidget.item(i)
                items_projeck.append(item.text())

            items_all.append(items_projeck)
            for i in range(workplace):
                item = self.ui.listWidget.item(i)
                items_workplace.append(item.text())
            items_all.append(items_workplace)
            for i in range(equip):
                item = self.ui.listWidget.item(i)
                items_equip.append(item.text())
            items_all.append(items_equip)
            for i in range(team):
                item = self.ui.listWidget.item(i)
                items_team.append(item.text())
            items_all.append(items_team)
            for i in range(task):
                item = self.ui.listWidget.item(i)
                items_task.append(item.text())
            items_all.append(items_task)

            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            self.ui.listWidget_3.clear()
            self.ui.listWidget_4.clear()
            self.ui.listWidget_5.clear()
            with open('list_widget.json', mode='w', encoding='utf-8') as f:
                import json
                json.dump(items_all, f, indent=4, ensure_ascii=False)
        else:
            print('none')
    def add_projeck(self):
        self.ui.listWidget.addItem(str(self.ui.lineEdit.text()))
        self.ui.lineEdit.clear()

    def add_workplace(self):
        self.ui.listWidget_2.addItem(str(self.ui.lineEdit_2.text()))
        self.ui.lineEdit_2.clear()

    def add_team(self):
        self.ui.listWidget_4.addItem(str(self.ui.lineEdit_4.text()))
        self.ui.lineEdit_4.clear()

    def add_task(self):
        self.ui.listWidget_5.addItem(str(self.ui.lineEdit_5.text()))
        self.ui.lineEdit_5.clear()

    def dell_add_projeck(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def dell_add_workplace(self):
        self.ui.listWidget_2.takeItem(self.ui.listWidget_2.currentRow())

    def dell_add_team(self):
        self.ui.listWidget_4.takeItem(self.ui.listWidget_4.currentRow())

    def dell_add_task(self):
        self.ui.listWidget_5.takeItem(self.ui.listWidget_5.currentRow())

    def dell(self):
        self.ui.listWidget_3.takeItem(self.ui.listWidget_3.currentRow())

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
        if len(self.qwe)==0:
            pass
        else:
            self.ui.listWidget_3.addItem(str(self.qwe))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = zaivka()
    application.show()

    sys.exit(app.exec())
