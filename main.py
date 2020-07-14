from PyQt5 import QtWidgets
import PyQt5
import numpy
import datetime
import time
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
        self.ui.a= datetime.date.today()
        print(self.ui.a)
        self.data=self.ui.a
        print(self.ui.a.year)
        print(self.ui.a.month)
        print(self.ui.a.day)
        # self.ui.tableWidget.setItem(0, 0, PyQt5.QtWidgets.QTableWidgetItem(str(item.text())))
        # self.list = [self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.lineEdit_4.text(), self.ui.lineEdit_5.text()]
        # self.clear = [self.ui.lineEdit.clear(), self.ui.lineEdit.clear(), self.ui.lineEdit.clear(), self.ui.lineEdit.clear()]

    def add_zaivka(self):
        name=self.ui.lineEdit_3.text()
        projeck = self.ui.listWidget.count()
        workplace = self.ui.listWidget_2.count()
        equip = self.ui.listWidget_3.count()
        team = self.ui.listWidget_4.count()
        task = self.ui.listWidget_5.count()
        if projeck != 0 and workplace != 0 and equip != 0 and team != 0 and task != 0:
        # if projeck!=0:
            items_all=[]
            items_from = []
            items_projeck = []
            items_workplace = []
            items_equip = []
            items_team = []
            items_task = []
            items_time = []
            items_time.append(self.ui.a.year-self.ui.a.month-self.ui.a.day)
            items_from.append(self.ui.lineEdit_3.text())
            # print(items_from)
            # print('9999')
            self.ui.lineEdit_3.clear()
            items_all.append(items_from)
            for i in range(projeck):
                item_projeck = self.ui.listWidget.item(i)
                items_projeck.append(item_projeck.text())
                self.ui.tableWidget.setWordWrap(True)
            items_all.append(items_projeck)
            for i in range(workplace):
                item_workplace = self.ui.listWidget_2.item(i)
                items_workplace.append(item_workplace.text())

            items_all.append(items_workplace)
            for i in range(equip):
                item_equip = self.ui.listWidget_3.item(i)
                items_equip.append(item_equip.text())
            items_all.append(items_equip)
            for i in range(team):
                item_team = self.ui.listWidget_4.item(i)
                items_team.append(item_team.text())
            items_all.append(items_team)
            for i in range(task):
                item_task = self.ui.listWidget_5.item(i)
                items_task.append(item_task.text())
            items_all.append(items_task)
            items_all.append(items_time)
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            self.ui.listWidget_3.clear()
            self.ui.listWidget_4.clear()
            self.ui.listWidget_5.clear()
            print('***')
            print(items_all)
            print('***')
            items_all_r=[]
            with open('list_widget.json', mode='r', encoding='utf-8') as fh:
                import json
                items_all_r = json.load(fh)
            print(items_all_r)
            items_all_r.append(items_all)
            with open('list_widget.json', mode='w', encoding='utf-8') as f:
                import json
                json.dump(items_all_r, f, indent=4, ensure_ascii=False)
        else:
            print('none')
            print('none21111111111')
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
