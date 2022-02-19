
from PyQt5.QtWidgets import (QStyledItemDelegate, QDoubleSpinBox,
                             QComboBox, QDateTimeEdit, QWidget,
                             QSpinBox)

from PyQt5.QtCore import  Qt, QDateTime, QModelIndex, QAbstractItemModel


class QmyFloatSpinDelegate(QStyledItemDelegate):
    def __init__(self, minV=0, maxV=10000, digi=2, parent=None):
        super(QmyFloatSpinDelegate, self).__init__(parent)
        self.__min == minV
        self.__max == maxV
        self.__decimals = digi

    def createEditor(self, parent, option, index):
        editor = QDoubleSpinBox(parent)
        editor.setFrame(False)
        editor.setRange(self.__min, self.__max)
        editor.setDecimals(self.__decimals)
        return editor

    def setEditorData(self, editor, index):
        model = index.model()
        text = model.data(index, Qt.EditRole)
        editor.setValue(float(text))

    def setModelData(self, editor, model, index):
        value = editor.value()
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

class QmyComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(QmyComboBoxDelegate, self).__init__(parent=None)
        self.__isEditable = False
        self.__itemList = ["未审核", "审核通过"]

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.setFrame(False)
        editor.setEditable(self.__isEditable)
        editor.addItems(self.__itemList)
        return editor

    def setModelData(self, editor, model, index):
        text = editor.currentText()
        model.setData(index, text, Qt.EditRole)

    def setEditorData(self, editor, index):
        model = index.model()
        text = model.data(index, Qt.EditRole)
        editor.setCurrentText(text)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


#日期时间代理
class QmyTimeEditDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(QmyTimeEditDelegate, self).__init__(parent)

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QModelIndex) -> QWidget:
        editor = QDateTimeEdit(parent)
        editor.setFrame(False)  #关闭边框
        editor.setDateTime(QDateTime().currentDateTime())   #设置系统当前时间
        editor.setCalendarPopup(True)
        return editor

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, index: QModelIndex) -> None:
        datetime = editor.dateTime()
        model.setData(index, datetime, Qt.EditRole)

    def setEditorData(self, editor: QWidget, index: QModelIndex) -> None:
        model = index.model()
        datetime = model.data(index, Qt.EditRole)
        if not isinstance(datetime, QDateTime):
            datetime = QDateTime().fromString(datetime, "yyyy-MM-dd hh:mm:ss")
        editor.setDateTime(datetime)

    def updateEditorGeometry(self, editor: QWidget, option: 'QStyleOptionViewItem', index: QModelIndex) -> None:
        editor.setGeometry(option.rect)

class QmyIntDelegate(QStyledItemDelegate):
    def __init__(self, min=0, max=15, parent=None):
        super(QmyIntDelegate, self).__init__(parent)
        self.__min = min
        self.__max = max

    def createEditor(self, parent: QWidget, option: 'QStyleOptionViewItem', index: QModelIndex) -> QWidget:
        editor = QSpinBox(parent)
        editor.setFrame(False)
        editor.setRange(self.__min, self.__max)
        return editor

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, index: QModelIndex) -> None:
        value = editor.value()
        model.setData(index, value, Qt.DisplayRole)

    def setEditorData(self, editor: QWidget, index: QModelIndex) -> None:
        model = index.model()
        text = model.data(index, Qt.EditRole)
        editor.setValue(int(text))

    def updateEditorGeometry(self, editor, option, index) -> None:
        editor.setGeometry(option.rect)

