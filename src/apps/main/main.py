import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from packages.file_explorer import FileExplorer


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = FileExplorer(ctx=app)
    window.resize(650, 650)
    window.show()

    sys.exit(app.exec())
