import sys
from DivSqlite import divsqlite
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QTabWidget,
    QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QTextEdit)
from PyQt5.QtWidgets import QPlainTextDocumentLayout as QTextDocument
from PyQt5.QtCore import pyqtSlot


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        #Make a tab
        self.tabs = QTabWidget()
        #self.tab1 = QTextEdit()
        #self.tab2 = QTextEdit()
        self.tab1 = QTextDocument("")
        self.tab2 = QTextDocument("")
        #self.tab1.setReadOnly(True)
        #self.tab2.setReadOnly(True)
        self.tab1.setDefaultStyleSheet("<style> body {background: blue; font-family: \"Comic Sans MS\";} div {background: grey; border-style: solid; border-width: 5px; padding: 5px; border-color: black;}</style>")
        self.tab1.setHtml(self.char_sheet_read())
        self.tab2.setHtml(self.char_sheet_read())
        #self.tab1.setText(self.char_sheet_read())
        #self.tab2.setText(self.char_sheet_read())
        self.tabs.addTab(self.tab1,"Tab 1")
        self.tabs.addTab(self.tab2,"Tab 2")

        #show extra window button
        sbtn = QPushButton('Show Armors', self)
        sbtn.clicked.connect(lambda: self.on_click())
        sbtn.resize(sbtn.sizeHint())

        #wrangle buttons
        vBox = QVBoxLayout()
        vBox.addStretch(1)
        vBox.addWidget(self.tabs)
        vBox.addWidget(qbtn)
        vBox.addWidget(sbtn)
        self.setLayout(vBox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

    @pyqtSlot()
    def on_click(self):
        #set up second Window
        self._2nd = tableView()
        self._2nd.show()

    def char_sheet_read(self):
        file = open("sample_char_sheet.html", "r")
        text = ""
        for a in file.readlines():
            text+=a
        print(text)
        return text

class tableView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setWindowTitle("Second Window")
        div = divsqlite("Divinity.db")
        armor_set = div.get_armors()
        armor_set = armor_set[:10]
        self.tw = QTableWidget()
        self.tw.setRowCount(len(armor_set))
        self.tw.setColumnCount(11)
        self.tw.setHorizontalHeaderLabels(["SET ID","Helmet","Chest","Gloves",\
            "Boots","Waist","Undergarment","Amulet","Accs. 1","Accs. 2","Armour Rating"])
        for a in range(0,len(armor_set)):
            x = armor_set[a]
            b=0
            for y in x:
                if y!="set_id" and y!="armor_rating":
                    self.tw.setItem(a,b,QTableWidgetItem(str(x[y]["name"])))
                else:
                    self.tw.setItem(a,b,QTableWidgetItem(str(x[y])))
                b+=1
        div.conn.close()
        self.tw.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw.move(0,0)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tw)
        #define equip button and check buttons
        eqBox = QtWidgets.QCheckBox("Equip Set", self)
        self.layout.addWidget(eqBox)
        eqBox.stateChanged.connect(self.boxTick)
        self.setLayout(self.layout)
        # table selection change
        self.tw.doubleClicked.connect(self.on_click)

    def boxTick(self):
        temp = QtWidgets.QMessageBox.information(self,'Message','Checkbox ticked.',QtWidgets.QMessageBox.Ok)
        #if temp:
            #print("I dunno")

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tw.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
