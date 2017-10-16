import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout
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
        sender = self.sender()
        ab_s = armor_build_window()
        ab_s.show()



class armor_build_window(QWidget):
    def __init__(self):
        super().__init__()
        self.div = divsqlite("Divinity.db")
        self.initial()

    def initial(self):
        self.armor_table()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.ab_table)
        #self.show()

    def armor_table(self):
        self.ab_table = QTableWidget()
        
        #get row and column counts
        self.div.curr.execute("SELECT count(*) FROM armor_builds")
        ab_rows = int(self.div.curr.fetchall()[0][0])
        ab_columns = 5  #helmet, boots, chest and gloves with armor rating
        self.ab_table.setRowCount(ab_rows)
        self.ab_table.setColumnCount(ab_columns)

        #insert items
        self.div.curr.execute("SELECT armor_rating, helmet, chest, gloves, boots FROM armor_builds")
        sets = self.div.curr.fetchall()
        for a in range(0,ab_rows):
            for b in range(0,5):
                if b != 0:
                    self.div.curr.execute("SELECT name FROM armor_main WHERE armor_id = '{0}'".format(sets[a][b]))
                    a_name = self.div.curr.fetchall()[0][0]
                    a_name = QTableWidgetItem(a_name)
                    self.ab_table.setItem(a,b,a_name)
                else:
                    a_rating = QTableWidgetItem(str(sets[a][b]))
                    self.ab_table.setItem(a,b,a_rating)
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())