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
    QWidget,
    QVBoxLayout,
    QStackedWidget
)
from src.gui import (
    view,
    model,
    delegate
)


class TableWidget(QWidget):

    def __init__(self):
        super(TableWidget, self).__init__()

        vbox = QVBoxLayout(self)
        vbox.setContentsMargins(0, 0, 0, 0)

        self.relations = {}

        # Stack
        self.stacked = QStackedWidget()
        vbox.addWidget(self.stacked)

    def count(self):
        return self.stacked.count()

    def remove_table(self, index):
        widget = self.stacked.widget(index)
        self.stacked.removeWidget(widget)
        del widget

    def current_table(self):
        return self.stacked.currentWidget()

    def remove_relation(self, name):
        del self.relations[name]

    def add_relation(self, name, rela):
        if self.relations.get(name, None) is None:
            self.relations[name] = rela
            return True
        return False

    def add_table(self, rela, name, table):
        """ Add new table from New Relation Dialog """

        self.add_relation(name, rela)
        self.stacked.addWidget(table)

    def add_tuple(self):
        current_view = self.current_table()
        if current_view is not None:
            model = current_view.model()
            model.insertRow(model.rowCount())

    def add_column(self):
        current_view = self.current_table()
        if current_view is not None:
            model = current_view.model()
            model.insertColumn(model.columnCount())

    def delete_tuple(self):
        current_view = self.current_table()
        if current_view is not None:
            model = current_view.model()
            selection = current_view.selectionModel()
            if selection.hasSelection():
                selection = selection.selection()
                rows = set([index.row() for index in selection.indexes()])
                rows = sorted(list(rows))
                previous = -1
                i = len(rows) - 1
                while i >= 0:
                    current = rows[i]
                    if current != previous:
                        model.removeRow(current)
                    i -= 1

    def delete_column(self):
        """ Elimina la/las columnas seleccionadas """

        current_view = self.current_table()
        if current_view is not None:
            model = current_view.model()
            selection = current_view.selectionModel()
            if selection.hasSelection():
                selection = selection.selection()
                columns = set(
                    [index.column() for index in selection.indexes()])
                columns = sorted(list(columns))
                previous = -1
                i = len(columns) - 1
                while i >= 0:
                    current = columns[i]
                    if current != previous:
                        model.removeColumn(current)
                    i -= 1

    def create_table(self, rela, editable=True):
        """ Se crea la vista y el modelo """

        _view = view.View()
        _model = model.Model(rela)
        if not editable:
            _model.editable = False
        _view.setModel(_model)
        _view.setItemDelegate(delegate.Delegate())
        _view.setHorizontalHeader(view.Header())
        return _view
