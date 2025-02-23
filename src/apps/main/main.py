import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QWidget


class Widget(QWidget):

    """ Displays a main window widget with a tree-like list window widget as well as a sub-window widget, with a button:

        menu_widget: The list window widget
        text_widget: The sub-window widget
        button: The button widget

        content_layout: Organises the full layout of the resulting window.
        main_widget: The entire main window widget, with the QVBoxLayout.

    """

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)

        _placeholder = "somethinggg"
        text_widget = QLabel(_placeholder)
        button = QPushButton("Something")

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_widget = Widget()
    main_widget.show()

#    label = QLabel("Placeholder text")
#    label.setAlignment(Qt.AlignCenter)
#    label.setStyleSheet("""
#        
#        color: #FFFFFF;
#        font-family: Titillium;
#        """)
#    label.show()

    with open("main.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
