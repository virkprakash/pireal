# -*- coding: utf-8 -*-
#
# Copyright 2015 - Gabriel Acosta <acostadariogabriel@gmail.com>
#
# This file is part of Pireal.
#
# Pireal is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# Pireal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pireal; If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QMenu,
    QAbstractItemView,
    QMessageBox
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import (
    Qt,
    pyqtSignal
)
#from src.gui.main_window import Pireal
from src import translations as tr


class LateralWidget(QListWidget):

    itemRemoved = pyqtSignal(int)

    def __init__(self):
        super(LateralWidget, self).__init__()
        # Multiple selection
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

        # Connections
        self.customContextMenuRequested['const QPoint'].connect(
            self.__show_context_menu)

    def __show_context_menu(self, point):
        """ Context menu """

        menu = QMenu()
        edit_action = menu.addAction(tr.TR_MENU_RELATION_EDIT_RELATION)
        remove_action = menu.addAction(QIcon(":img/remove-rel"),
                                        tr.TR_MENU_RELATION_DELETE_RELATION)

        remove_action.triggered.connect(self._remove)
        edit_action.triggered.connect(self._edit)

        menu.exec_(self.mapToGlobal(point))

    def _edit(self):
        pass

    #def _change_item(self, index):
        #table_widget = Pireal.get_service("main").table_widget
        #table_widget.stacked.setCurrentIndex(index)

    #def add_item_list(self, items):
        #if not self.isVisible():
            #self.show()
        #for i in items:
            #item = QListWidgetItem(i)
            #item.setTextAlignment(Qt.AlignHCenter)
            #self._list_widget.addItem(item)
    def add_item(self, text, nrow):
        item = QListWidgetItem(text + ' [' + str(nrow) + ']')
        item.setTextAlignment(Qt.AlignHCenter)
        self.addItem(item)

    def _remove(self):
        r = QMessageBox.question(self, tr.TR_CENTRAL_CONFIRM_DELETE_REL_TITLE,
                                 tr.TR_CENTRAL_CONFIRM_DELETE_REL.format(
                                     self.currentItem().text().split()[0]),
                                 QMessageBox.No | QMessageBox.Yes)
        if r == QMessageBox.No:
            return
        else:
            index = self.currentRow()
            self.takeItem(index)
            self.itemRemoved.emit(index)
        #container = Pireal.get_service("container")
        #items = self._list_widget.selectedItems()
        #for item in items:
            #index = self._list_widget.row(item)
            #container.table_widget.remove_table(index)
            #self.remove_item(index)
        #container.remove_relation(items)

    def clear_items(self):
        """ Remove all items and selections in the view """

        self.clear()

    def get_relation_name(self):
        """ Returns the text of the item """

        item = self._list_widget.currentItem()
        if item is None:
            return False
        return item.text()

    def current_index(self):
        """ Returns the current index """

        return self._list_widget.currentRow()

    def remove_item(self, index):
        """ Removes the item from the given index in the list widget"""

        self._list_widget.takeItem(index)
