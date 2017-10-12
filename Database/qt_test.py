#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a quit
button. When we press the button,
the application terminates. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import QCoreApplication
from DivSqlite import divsqlite

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        #set up divinity database manager
        div = divsqlite("Divinity.db")
        
        #set up table
        self.tableWidget = QTableWidget()
        div.curr.execute("SELECT COUNT(*) FROM armor_builds")
        count = div.curr.fetchall()[0][0]
        self.tableWidget.setRowCount(int(count))
        self.tableWidget.setColumnCount(10)
        div.curr.execute("SELECT * FROM armor_builds")
        builds = div.curr.fetchall()
        for a in range(0,len(builds)):
            for b in range(1,11):
                self.tableWidget.setItem(a,b-1,QTableWidgetItem(str(builds[a][b])))
        self.tableWidget.move(0,0)
        
        """qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)"""    
        
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
        
        self.setGeometry(700, 700, 250, 150)
        self.setWindowTitle('Table')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())