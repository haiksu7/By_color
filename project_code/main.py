from project_code.start_window import StartWindow
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartWindow()
    ex.show()
    sys.exit(app.exec_())
