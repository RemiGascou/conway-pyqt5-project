# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib.ConwayWidget import *

class ConwaysApp(QMainWindow):
    """docstring for ConwaysApp."""
    def __init__(self, gridx=10, gridy=10, parent=None):
        super(ConwaysApp, self).__init__()
        self.title  = "Conway's Game of Life"
        self.gridx  = gridx
        self.gridy  = gridy
        self.cellsize = 5
        self.left   = 10
        self.top    = 10
        self.width  = self.gridx*self.cellsize+10
        self.height = self.gridy*self.cellsize+10
        self._initUI()

    def _initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setAttribute(Qt.WA_DeleteOnClose)
        #Trick to center window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        #EndTrick
        self.conway_grid = ConwayWidget(self.cellsize, self.gridx, self.gridy)
        self.setCentralWidget(self.conway_grid)
        self.show()
