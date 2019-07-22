#!/usr/bin/env python3

from pathlib import Path

from PyQt5 import uic  # type: ignore
from PyQt5.QtWidgets import QApplication

root = Path(__file__).parent

Form, Window = uic.loadUiType(root.joinpath("not_implemented.ui"))
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()
