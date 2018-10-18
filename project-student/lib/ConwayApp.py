# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from lib.ConwayWidget import *

class ConwayApp(QMainWindow):
    """docstring for ConwayApp."""
    def __init__(self, arg):
        super(ConwayApp, self).__init__()
        self.arg = arg
