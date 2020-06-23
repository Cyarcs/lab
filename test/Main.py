import PyQt5.QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QIcon

# Наследуемся от QMainWindow
import xlrd

book = xlrd.open_workbook('New_List_of_lab_Equipmemt_05.04.19.xlsx')
sheet = book.sheets()[0]
# print(sheet.ncols)
# print(sheet.nrows)
data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)]for r in range(sheet.nrows)]
print(data[0][3])
# print(len(data[0]))

class MainWindow(PyQt5.QtWidgets.QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        PyQt5.QtWidgets.QMainWindow.__init__(self)


        self.setMinimumSize(QSize(930, 930))  # Устанавливаем размеры
        self.setWindowTitle("Работа с QTableWidget")  # Устанавливаем заголовок окна
        central_widget = PyQt5.QtWidgets.QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет
        self.btn = PyQt5.QtWidgets.QPushButton("+", self)
        self.btn.move(0, 0)
        self.btn.resize(30, 30)
        self.btn.clicked.connect(self.getData)
        grid_layout = PyQt5.QtWidgets.QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет

        self.table = PyQt5.QtWidgets.QTableWidget(self)  # Создаём таблицу

        self.table.move(50,50)
        self.table.setColumnCount(len(data[0][:3]))  # Устанавливаем три колонки
        self.table.setRowCount(len(data)-1)  # и одну строку в таблице
        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(data[0][:3])
       # # Устанавливаем всплывающие подсказки на заголовки
        # table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        # table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        # table.horizontalHeaderItem(2).setToolTip("Column 3 ")

        # Устанавливаем выравнивание на заголовки
        # table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        # table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        # table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        for i in range(len(data[0][:3])):
            self.table.horizontalHeaderItem(i).setTextAlignment(Qt.AlignHCenter)
        # заполняем первую строку
        for i in range(len(data)):
            for z in range(len(data[i])):
                if i > 49:
                    break
                # print(data[i + 1][z])
                self.table.setItem(i, z, PyQt5.QtWidgets.QTableWidgetItem(str(data[i + 1][z])))

        # table.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        # table.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        # table.setItem(0, 2, QTableWidgetItem("Text in column 3"))

        # делаем ресайз колонок по содержимому
        self.table.resizeColumnsToContents()
        grid_layout.addWidget(self.table, 50, 50)  # Добавляем таблицу в сетку
    def getData(self):
        rows = self.table.rowCount()
        cols = self.table.columnCount()
        rows1 = self.table.currentColumn()
        cols1 = self.table.currentRow()
        qwe=self.table.item(cols1,rows1)
        qwer= self.table.model()
        index =qwer.index(cols1,rows1)

        # data = []
        # for row in range(rows):
        #     tmp = []
        #     for col in range(cols):
        #         try:
        #             tmp.append(self.table.item(row, col).text())
        #         except:
        #             tmp.append('No data')
        #     data.append(tmp)
        # for i in data: print(i)

        print(qwe())
        print(qwer.data(index))



if __name__ == "__main__":
    import sys

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())