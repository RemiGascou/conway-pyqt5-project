# -*- coding: utf-8 -*-

import os, sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib.ConwaysCanvas import *

class ConwaysApp(QMainWindow):
    """docstring for ConwaysApp."""
    def __init__(self, gridwidth=10, gridheight=10, parent=None):
        super(ConwaysApp, self).__init__()
        self.title           = "Conway's Game of Life"
        self.gridwidth       = gridwidth
        self.gridheight      = gridheight
        self.cellsize        = 25
        self.margin_left     = 200
        self.margin_top      = 200
        self.width           = self.gridwidth*self.cellsize
        self.height          = self.gridheight*self.cellsize
        self.timer_period    = 125
        self.timer_state     = False

        self._initUI()

        self.timer  = QTimer()
        self.timer.timeout.connect(self.conway_canvas.updateGridEvent)

    def _initUI(self):
        self.setWindowTitle(self.title + " - [PAUSED]")
        self.setWindowIcon(QIcon('lib/ico.png'))
        self.setGeometry(self.margin_left, self.margin_top, self.width, self.height)
        #self.setFixedSize(self.size())
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.conway_canvas = ConwaysCanvas(self.cellsize, self.gridwidth, self.gridheight)
        self.setCentralWidget(self.conway_canvas)
        self.show()

    def _updateUI(self):
        self.timer.stop()
        self.width  = self.gridwidth*self.cellsize
        self.height = self.gridheight*self.cellsize
        self.setGeometry(self.margin_left, self.margin_top, self.width, self.height)
        #self.setFixedSize(self.size())
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.conway_canvas  = ConwaysCanvas(self.cellsize, self.gridwidth, self.gridheight)
        self.setCentralWidget(self.conway_canvas)
        self.timer_state    = False
        self.timer          = QTimer()
        self.timer.timeout.connect(self.conway_canvas.updateGridEvent)
        self.show()



    def keyPressEvent(self, event):
        if   event.key() == Qt.Key_Space:
            if self.timer_state == True :
                self.timer_state = False
                self.timer.stop()
                self.setWindowTitle(self.title +" - [PAUSED]")
            else :
                self.timer_state = True
                self.timer.start(self.timer_period)
                self.setWindowTitle(self.title)
        elif event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_R:
            self.conway_canvas.regen()
        elif event.key() == Qt.Key_C:
            self.conway_canvas.cleargrid()
        elif event.key() == Qt.Key_Down:
            self.set_gridheight(max(min(self.get_gridheight()+1, 50), 5))
            print(self.get_gridheight())
        elif event.key() == Qt.Key_Up:
            self.set_gridheight(max(min(self.get_gridheight()-1, 50), 5))
            print(self.get_gridheight())
        elif event.key() == Qt.Key_Right:
            self.set_gridwidth(max(min(self.get_gridwidth()+1, 50), 5))
        elif event.key() == Qt.Key_Left:
            self.set_gridwidth(max(min(self.get_gridwidth()-1, 50), 5))


    # *----------------------------GET--SET------------------------------------*
    def get_cellsize (self):
        return self.cellsize

    def set_cellsize (self, cellsize):
        self.cellsize = max(0,cellsize)
        self.conway_canvas.set_cellsize(self.cellsize)
        self._updateUI()

    def get_gridwidth (self):
        return self.gridwidth

    def set_gridwidth (self, gridwidth):
        self.gridwidth = max(0,gridwidth)
        self.conway_canvas.set_gridwidth(self.gridwidth)
        self._updateUI()

    def get_gridheight (self):
        return self.gridheight

    def set_gridheight (self, gridheight):
        self.gridheight = max(0,gridheight)
        self.conway_canvas.set_gridheight(self.gridheight)
        self._updateUI()


if __name__ == """__main__""":
    app = QApplication(sys.argv)
    ex = ConwaysApp(38,20) #76,40
    sys.exit(app.exec_())
