# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (
    QTableView,
    QHeaderView,
    QLineEdit,

    QAbstractItemView
)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import (
    Qt,
    QModelIndex
)


class Table(QTableView):

    def __init__(self):
        super(Table, self).__init__()
        # Stretch horizontal header
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().hide()
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Model
        model = QStandardItemModel()
        self.setModel(model)


class Header(QHeaderView):

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(Header, self).__init__(orientation, parent)
        self.setSectionsClickable(True)
        self.setSectionResizeMode(QHeaderView.Stretch)
        self.line = QLineEdit(parent=self.viewport())
        self.line.setAlignment(Qt.AlignTop)
        self.line.setHidden(True)
        self.line.blockSignals(True)
        self.col = 0

        # Connections
        self.sectionDoubleClicked[int].connect(self.__edit)
        self.line.editingFinished.connect(self.__done_editing)

    def __edit(self, index):
        geo = self.line.geometry()
        geo.setWidth(self.sectionSize(index))
        geo.moveLeft(self.sectionViewportPosition(index))
        current_text = self.model().headerData(index, Qt.Horizontal)
        self.line.setGeometry(geo)
        self.line.setHidden(False)
        self.line.blockSignals(False)
        self.line.setText(str(current_text))
        self.line.setFocus()
        self.line.selectAll()
        self.col = index

    def __done_editing(self):
        self.line.blockSignals(True)
        self.line.setHidden(False)
        text = self.line.text()
        self.model().setHeaderData(self.col, Qt.Horizontal, text)
        self.line.setText("")
        self.line.hide()
        self.setCurrentIndex(QModelIndex())
