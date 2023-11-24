from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QMovie
import os

class CatDancer(QLabel):
    def init(self):
        super().__init__()
        self.gif = QMovie(imgDir() + "cat.gif")
        self.setScaledContents(True)
        self.setMovie(self.gif)
        self.movie().start()
        self.setMaximumSize(200, 200)
    
def imgDir():
    url = os.path.join(os.path.dirname(__file__), "images/")
    return url

def uiDir():
    url = os.path.join(os.path.dirname(__file__), "interface/")
    return url

def backupDir():
    url = os.path.join(os.path.dirname(__file__), "backups/")
    return url