# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zaivka.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_zaivka(object):
    def setupUi(self, zaivka):
        zaivka.setObjectName("zaivka")
        zaivka.setEnabled(True)
        zaivka.resize(1139, 705)
        self.centralwidget = QtWidgets.QWidget(zaivka)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_10 = QtWidgets.QWidget(self.centralwidget)
        self.widget_10.setObjectName("widget_10")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_10)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 0, 2, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_10)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_7.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_10)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 3, 1, 1)
        self.verticalLayout_6.addWidget(self.widget_10)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.widget_6)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.add_projeck = QtWidgets.QPushButton(self.widget)
        self.add_projeck.setObjectName("add_projeck")
        self.verticalLayout.addWidget(self.add_projeck)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_6)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listWidget_2 = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.add_workplace = QtWidgets.QPushButton(self.widget_2)
        self.add_workplace.setObjectName("add_workplace")
        self.verticalLayout_2.addWidget(self.add_workplace)
        self.horizontalLayout.addWidget(self.widget_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.widget_6)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.listWidget_3 = QtWidgets.QListWidget(self.widget_3)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout_3.addWidget(self.listWidget_3)
        self.gridLayout_3.addWidget(self.widget_3, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Add = QtWidgets.QPushButton(self.widget_6)
        self.Add.setObjectName("Add")
        self.gridLayout_2.addWidget(self.Add, 0, 0, 1, 1)
        self.Delete = QtWidgets.QPushButton(self.widget_6)
        self.Delete.setObjectName("Delete")
        self.gridLayout_2.addWidget(self.Delete, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_6)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.listWidget_4 = QtWidgets.QListWidget(self.widget_4)
        self.listWidget_4.setObjectName("listWidget_4")
        self.verticalLayout_4.addWidget(self.listWidget_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_4.addWidget(self.lineEdit_4)
        self.add_team = QtWidgets.QPushButton(self.widget_4)
        self.add_team.setObjectName("add_team")
        self.verticalLayout_4.addWidget(self.add_team)
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_5 = QtWidgets.QWidget(self.widget_6)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.listWidget_5 = QtWidgets.QListWidget(self.widget_5)
        self.listWidget_5.setObjectName("listWidget_5")
        self.verticalLayout_5.addWidget(self.listWidget_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_5.addWidget(self.lineEdit_5)
        self.add_task = QtWidgets.QPushButton(self.widget_5)
        self.add_task.setObjectName("add_task")
        self.verticalLayout_5.addWidget(self.add_task)
        self.horizontalLayout.addWidget(self.widget_5)
        self.verticalLayout_6.addWidget(self.widget_6)
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout.setObjectName("gridLayout")
        self.add_zaivka = QtWidgets.QPushButton(self.widget_7)
        self.add_zaivka.setObjectName("add_zaivka")
        self.gridLayout.addWidget(self.add_zaivka, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 2, 1, 1)
        self.verticalLayout_6.addWidget(self.widget_7)
        self.gridLayout_8.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.centralwidget)
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_8 = QtWidgets.QWidget(self.widget_9)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.send_zaivka = QtWidgets.QPushButton(self.widget_8)
        self.send_zaivka.setObjectName("send_zaivka")
        self.gridLayout_4.addWidget(self.send_zaivka, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 2, 1, 1)
        self.gridLayout_5.addWidget(self.widget_8, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout_5.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.widget_9, 1, 0, 1, 1)
        zaivka.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(zaivka)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1139, 21))
        self.menubar.setObjectName("menubar")
        zaivka.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(zaivka)
        self.statusbar.setObjectName("statusbar")
        zaivka.setStatusBar(self.statusbar)

        self.retranslateUi(zaivka)
        QtCore.QMetaObject.connectSlotsByName(zaivka)

    def retranslateUi(self, zaivka):
        _translate = QtCore.QCoreApplication.translate
        zaivka.setWindowTitle(_translate("zaivka", "MainWindow"))
        self.label_6.setText(_translate("zaivka", "Имя"))
        self.label.setText(_translate("zaivka", "Project"))
        self.add_projeck.setText(_translate("zaivka", "Add Projeck"))
        self.label_2.setText(_translate("zaivka", "Workplace"))
        self.add_workplace.setText(_translate("zaivka", "Add Workplace"))
        self.label_3.setText(_translate("zaivka", "Equipment"))
        self.Add.setText(_translate("zaivka", "Add"))
        self.Delete.setText(_translate("zaivka", "Delete"))
        self.label_4.setText(_translate("zaivka", "Team"))
        self.add_team.setText(_translate("zaivka", "Add Team"))
        self.label_5.setText(_translate("zaivka", "Task"))
        self.add_task.setText(_translate("zaivka", "Add Task"))
        self.add_zaivka.setText(_translate("zaivka", "Сформироватьзаявку"))
        self.send_zaivka.setText(_translate("zaivka", "Отправить заявку"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("zaivka", "From"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("zaivka", "Project"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("zaivka", "Workplace"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("zaivka", "Equipment"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("zaivka", "Team"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("zaivka", "Task"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
