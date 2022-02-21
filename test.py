import os, sys, time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from MyWatcher import *

ftxt = 'test_file.txt'


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #self.filewatcher = MyFileSystemWatcher()
        self.filewatcher.addPath(ftxt)
        self.label = QLabel('Content of {0}:'.format(ftxt))
        self.textedit = QTextEdit()
        self.slot_load_show_text()  # init
        self.filewatcher.fileChanged.connect(self.slot_fileChanged_update)
        layout_vbox = QVBoxLayout()
        layout_vbox.addWidget(self.label)
        layout_vbox.addWidget(self.textedit)
        self.setLayout(layout_vbox)
        self.setWindowTitle('Mainwindow')
        self.setGeometry(300, 300, 500, 200)
        self.show()

    def slot_load_show_text(self):
        if os.path.exists(ftxt):
            time_modified = os.stat(ftxt).st_mtime
            time_modified_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_modified))
            self.textedit.setText(open(ftxt, 'r').read())
            self.textedit.append('*** last modified at {0} ***'.format(time_modified_str))
        else:
            self.textedit.setText('** {0} does not exist **'.format(ftxt))

    def slot_fileChanged_update(self, pathModified, infoModify):
        self.slot_load_show_text()
        print(pathModified, infoModify)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec_())
