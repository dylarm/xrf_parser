#!/usr/bin/env python3

import sys
from pathlib import Path

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileSystemModel
from PyQt5.uic import loadUi  # type: ignore

ROOT = Path(__file__).parent.joinpath("__ui__")
MAIN_UI = ROOT.joinpath("main.ui")
ABOUT_UI = ROOT.joinpath("about.ui")


# TODO: Get selected directory
# TODO: Show files in directory
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

    def __directories(self):
        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())
        model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
        self.treeInputDir.setModel(model)
        # Hide all except the Name column
        cols = model.columnCount()
        for col in range(cols - 1):
            self.treeInputDir.hideColumn(col + 1)

    def executeAbout(self):
        about = About()
        about.exec_()


class About(QDialog):
    def __init__(self):
        super(About, self).__init__()
        loadUi(ABOUT_UI, self)


def main() -> None:
    app = QApplication(sys.argv)
    form = Xrfp()
    form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
