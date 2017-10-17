import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QMainWindow
#from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from DivSqlite import divsqlite

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        #self.div = divsqlite("Divinity.db")
        self.initial()
        
    def initial(self):
        btn1 = QPushButton(("Armor Builds"), self)
        btn1.move(30,30)
        btn1.clicked.connect(self.open_table)
        self.show()

    def open_table(self):
        #sender = self.sender()
        self.ab_s = armor_build_window()



class armor_build_window(QWidget):
    def __init__(self):
        super().__init__()
        self.div = divsqlite("Divinity.db")
        self.initial()

    def initial(self):
        self.div.armor_set_name()
        self.armor_table()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.ab_table)
        self.setLayout(self.layout)
        self.show()

    def armor_table(self):
        self.ab_table = QTableWidget()
        
        #get row and column counts
        self.div.curr.execute("SELECT count(*) FROM armor_builds_named")
        ab_rows = int(self.div.curr.fetchall()[0][0])
        ab_columns = 5  #helmet, boots, chest and gloves with armor rating
        self.ab_table.setRowCount(ab_rows)
        self.ab_table.setColumnCount(ab_columns)

        #insert items
        self.div.curr.execute("SELECT armor_rating, helmet, chest, gloves, boots FROM armor_builds_named ORDER BY armor_rating DESC")
        sets = self.div.curr.fetchall()
        for a in range(0,ab_rows):
            for b in range(0,5):
                a_item = QTableWidgetItem(str(sets[a][b]))
                self.ab_table.setItem(a,b,a_item)
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())