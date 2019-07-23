#!/usr/bin/env python3

import sys
from pathlib import Path

from PyQt5.QtCore import QDir, Qt  # type: ignore
from PyQt5.QtWidgets import (  # type: ignore
    QApplication,
    QMainWindow,
    QDialog,
    QFileSystemModel,
)
from PyQt5.uic import loadUi  # type: ignore

ROOT = Path(__file__).parent.joinpath("__ui__")
MAIN_UI = ROOT.joinpath("main.ui")
ABOUT_UI = ROOT.joinpath("about.ui")


# TODO: Refresh and home buttons for directory/file listings
# TODO: Fill about About Dialog, programmatically ideally
# TODO: Fix path to UI files when using `python -m xrfp`


class Xrfp(QMainWindow):
    def __init__(self, parent=None):
        super(Xrfp, self).__init__(parent)
        loadUi(MAIN_UI, self)
        self.__buttons()
        self.__directories()

    def __buttons(self):
        self.actionAbout.triggered.connect(self.executeAbout)
        self.btnHome.clicked.connect(self.goHomePath)

    def __directories(self):
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.model.sort(0, Qt.AscendingOrder)
        self.treeInputDir.setModel(self.model)
        # Update the list of files if directory is selected
        self.treeInputDir.clicked.connect(self.updateList)
        # Hide all except the Name column
        cols = self.model.columnCount()
        for col in range(cols - 1):
            self.treeInputDir.hideColumn(col + 1)
        # Files only model
        self.file_model = QFileSystemModel()
        self.file_model.setFilter(QDir.NoDotAndDotDot | QDir.Files)
        # self.file_model.setRootPath(QDir.currentPath())
        self.listFiles.setModel(self.file_model)

    def executeAbout(self):
        about = About()
        about.exec_()

    def updateList(self, index):
        dir_path = self.model.fileInfo(index).absoluteFilePath()
        self.listFiles.setRootIndex(self.file_model.setRootPath(dir_path))

    def goHomePath(self):
        home = QDir.homePath()
        index = self.model.index(home)
        self.treeInputDir.scrollTo(self.model.setRootPath(home))
        self.treeInputDir.setCurrentIndex(index)
        self.updateList(index)


class About(QDialog):
    def __init__(self):
        super(About, self).__init__()
        loadUi(ABOUT_UI, self)


def main() -> None:
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    form = Xrfp()
    form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
