from __future__ import annotations

import contextlib
import importlib
import sys
from collections.abc import Iterator
from typing import TYPE_CHECKING

from qt_themes._theme import QtGui, QtWidgets

if TYPE_CHECKING:
    from PySide6 import QtCore

    Signal = QtCore.Signal
else:
    QtCore = importlib.import_module(f'{QtWidgets.__name__.rpartition(".")[0]}.QtCore')
    Signal = getattr(QtCore, "Signal", None) or QtCore.pyqtSignal

__all__ = ["QtCore", "QtGui", "QtWidgets", "Signal", "application"]


@contextlib.contextmanager
def application() -> Iterator[QtWidgets.QApplication]:
    app = QtWidgets.QApplication.instance()
    if isinstance(app, QtWidgets.QApplication):
        yield app
        return

    app = QtWidgets.QApplication(sys.argv)
    yield app
    app.exec()
