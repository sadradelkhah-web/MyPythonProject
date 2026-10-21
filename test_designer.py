import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow

app = QApplication(sys.argv)

window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
ui.btnOpenKar.clicked.connect(lambda: print("باز کردن درخواست کار"))
window.show()

sys.exit(app.exec())
