from functools import partial
from PySide6 import QtWidgets, QtCore, QtGui

class FileExplorer(QtWidgets.QMainWindow):
    """
    FileExplorer is a class representing the main window of a 
    file explorer. 
    Inherits from QtWidgets.QMainWindow.

    """

    view_mode = QtWidgets.QListView.ViewMode.IconMode
    def __init__(self, ctx):

        """Initialises the module"""

        super().__init__()
        self.ctx = ctx
        self.setWindowTitle('YT-DLP Explorer')
        self.setup_ui()
        self.create_file_model()

    def setup_ui(self):
        """Set's up all the necessary widgets, layouts and events."""
        self.create_widgets()
        self.modify_widgets()
        self.create_layout()
        self.add_widgets_to_layouts()


    def create_widgets(self):
        """Initialises the widgets that will appear in the final UI."""
        self.toolbar = QtWidgets.QToolBar()
        self.tree_view = QtWidgets.QTreeView()
        self.listview = QtWidgets.QListView()
        self.slider = QtWidgets.QSlider()
        self.main_widget = QtWidgets.QWidget()

    def modify_widgets(self):
        """For styling of widgets using css."""

        self.listview.setViewMode(self.view_mode)
        self.listview.setUniformItemSizes(True)
        self.listview.setIconSize(QtCore.QSize(48, 48))

        self.slider.setRange(48, 256)
        self.slider.setValue(48)

        self.tree_view.setSortingEnabled(True)
        self.tree_view.setAlternatingRowColors(True)
        self.tree_view.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

    def create_layout(self):

        """Initialises layout designs using QV and QHBoxLayout functions."""

        self.main_layout = QtWidgets.QHBoxLayout(self.main_widget)
        self.setCentralWidget(self.main_widget)
        self.setLayout(self.main_layout)


    def add_widgets_to_layouts(self):
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.main_layout.addWidget(self.tree_view)
        self.main_layout.addWidget(self.listview)
        self.main_layout.addWidget(self.slider)


    def setup_events(self):
        self.tree_view.clicked.connect(self.tree_view_clicked)
        self.listview.clicked.connect(self.list_view_clicked)
        self.listview.doubleClicked.connect(self.list_view_double_clicked)
        self.slider.valueChanged.connect(self.change_icon_size)

    def change_icon_size(self, value):
        self.listview.setIconSize(QtCore.QSize(value, value))


    def create_file_model(self):
        self.model = QtWidgets.QFileSystemModel()
        root_path = QtCore.QDir.rootPath()

        self.tree_view.setModel(self.model)
        self.listview.setModel(self.model)
        self.listview.setRootIndex(self.model.index(root_path))
        self.tree_view.setRootIndex(self.model.index(root_path))

    def tree_view_clicked(self, index):
        if self.model.isDir(index):
            self.listview.setRootIndex(index)
        else:
            self.listview.setRootIndex(index.parent())

    def list_view_clicked(self, index):
        self.tree_view.selectionModel().setCurrentIndex(index, QtCore.QItemSelectionModel.ClearAndSelect)

    def list_view_double_clicked(self, index):
        self.listview.setRootIndex(index)

    def add_actions_to_toolbar(self):
        locations = ["Home", "Desktop", "Documents", "Downloads"]
        for location in locations:
            icon = self.ctx.get_resource(f"{location}.svg")
            action = self.toolbar.addAction(QtGui.QIcon(icon), location.capitalize())
            action.triggered.connect(partial(self.change_location, location))

    def change_location(self, location):
        standard_path = QtCore.QStandardPaths()
        path = eval(f"standard_path.standardLocations(QtCore.QStandardPaths.{location.capitalize()}Location)")
        path = path[0]
        self.tree_view.setRootIndex(self.model.index(path))
        self.listview.setRootIndex(self.model.index(path))
