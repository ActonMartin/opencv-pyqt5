import cv2
import numpy as np

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from flags import OPEN_DIR

class FileSystemTreeView(QTreeView, QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.mainwindow = parent
        # 设置根目录
        self.fileSystemModel = QFileSystemModel()  # 1
        self.setModel(self.fileSystemModel)  # 2
        self.fileSystemModel.setRootPath(QDir.rootPath())  # 3
        self.setRootIndex(self.fileSystemModel.index(OPEN_DIR))  # 4

        # 隐藏size,date等列
        self.setColumnWidth(0, 200)
        self.setColumnHidden(1, True)
        self.setColumnHidden(2, True)
        self.setColumnHidden(3, True)
        # 不显示标题栏
        self.header().hide()
        # 设置动画
        self.setAnimated(True)
        # 选中不显示虚线
        self.setFocusPolicy(Qt.NoFocus)
        self.doubleClicked.connect(self.select_image)
        self.setMinimumWidth(200)

    def select_image(self, file_index):
        file_name = self.fileSystemModel.filePath(file_index)
        if file_name.endswith(('.jpg', '.png', '.bmp', 'jpeg')):
            src_img = cv2.imdecode(np.fromfile(file_name, dtype=np.uint8), -1)
            self.mainwindow.change_image(src_img)

