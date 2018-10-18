# -*- coding: utf-8 -*-

import os, sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib import *



if __name__ == """__main__""":
    app = QApplication(sys.argv)
    ex = ConwaysApp(100,100)
    timer = QTimer()
    timer.timeout.connect(ex.conway_grid.update)
    timer.start(125)
    sys.exit(app.exec_())
