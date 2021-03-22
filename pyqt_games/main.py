import window
from PyQt5 import QtWidgets


class Example(QtWidgets.QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication([])
    window = Example()
    window.show()
    app.exec()


if __name__=="__main__":
    main()
