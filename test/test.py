# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication,
#                              QLabel, QScrollArea, QGridLayout, QFileDialog)
# from PyQt5.QtGui import QPixmap
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.lbl = QLabel()
#
#         scroll_area = QScrollArea()
#         scroll_area.setWidget(self.lbl)
#         scroll_area.setWidgetResizable(True)
#
#         open_btn = QPushButton()
#         open_btn.setText('Показать изображение')
#         open_btn.clicked.connect(self.show_image)
#
#         grid = QGridLayout()
#         grid.addWidget(scroll_area, 0, 0)
#         grid.addWidget(open_btn, 1, 0)
#         self.setLayout(grid)
#
#     def show_image(self):
#         fileName, _ = QFileDialog.getOpenFileName(self,
#                       "Open Image", ".", "Image Files (*.png *.jpg *.bmp)")
#         if fileName:
#             self.pixmap = QPixmap(fileName)
#             self.lbl.setPixmap(self.pixmap)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.resize(700, 500)
#     ex.show()
#     sys.exit(app.exec_())


3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
import sys
from PyQt5.QtGui import QPixmap


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Adding Image To Label"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("P80612-175558.jpg")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.setLayout(vbox)
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())