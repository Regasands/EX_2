from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QRectF, QSize

from PyQt6 import uic
import sys
import random
from ui_main import Ui_Form


class A(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.b_1.clicked.connect(self.creats)
        self.b = False
    
    def creats(self):
        self.b = True
        self.update()
    def paintEvent(self, event):
        if not self.b:
            return
        painter = QPainter(self)
        painter.setBrush(QColor(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))
        y = random.randint(1, 100)
        painter.drawEllipse(200, 200, y, y)



if __name__ == '__main__':
    a = QApplication(sys.argv)
    e = A()
    e.show()
    sys.exit(a.exec())