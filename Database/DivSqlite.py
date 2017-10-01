#import necessary libraries
import sys
import os.path
import os
from os.path import abspath, curdir
import csv
import re
import math
from math import ceil
import operator
import random
import sqlite3


class DivSqlite(sqlite3):
    
    def __init__(self, path):
        self.path = path
        super().__init__()
        self.initDB(path)
        
    def initDB(self, path):
        self.conn = self.connect(path)
        self.curr = self.conn.cursor()
        
    #Armor builder
    def armor_building(self, character):
    	#Armor lists
    	Helmets=[]
    	Boots=[]
    	Chest=[]
    	Gloves=[]
    	#Get armors that don't have requirements
    	self.curr.execute("SELECT armor_id, type, armor_rating FROM armor_main where requirement_name is Null ORDER BY type")
    	easy_armor=self.curr.fetchall()
    	for b in easy_armor:
    		if b[1]=="Boots":
    			Boots.append(b)
    		elif b[1]=="Chest":
    			Chest.append(b)
    		elif b[1]=="Gloves":
    			Gloves.append(b)
    		elif b[1]=="Helmet":
    			Helmets.append(b)
    	#Store attr. requirements from armors to a list
    	self.curr.execute("SELECT requirement_name FROM armor_main WHERE requirement_name NOT NULL GROUP BY requirement_name")
    	req_names=[]
    	for a in self.curr:
    		req_names.append(a[0])
    	#get armors within range
    	for a in req_names:
    		char_query="SELECT %s FROM attributes WHERE Name=\'%s\'" % (a,character)
    		armors_query="SELECT armor_id, type,armor_rating FROM armor_main WHERE requirement_name=\'%s\' AND requirement_level<=(%s) GROUP BY type" % (a,char_query)
    		self.curr.execute(armors_query)
    		selections=self.curr.fetchall()
    		for b in selections:
    			if b[1]=="Boots":
    				Boots.append(b)
    			elif b[1]=="Chest":
    				Chest.append(b)
    			elif b[1]=="Gloves":
    				Gloves.append(b)
    			elif b[1]=="Helmets":
    				Helmets.append(b)
    	self.combo_maker_plain([Helmets,Chest,Boots,Gloves])
        
        #combo generator
    def combo_maker_plain(self, lists):
    	items={}
    	armor_types=[]
    	#fetch armor types
    	for a in range(0,len(lists)):
    		self.curr.execute("SELECT type from armor_main where armor_id=\'%s\'" % lists[a][0][0])
    		temp=self.curr.fetchall()
    		armor_type=temp[0][0]
    		items[a]=lists[a]
    		armor_types.append(armor_type)
    	print(armor_types)
    	#calculate total number of combos
    	no_combos=1
    	for a in items:
    		no_combos*=len(items[a])
    	print("There are %d number of combos." % no_combos)
    	list_frequency = no_combos
    	self.curr.execute("DELETE FROM armor_builds")
    	#actually generate the combos
    	set_id=1
    	for a in lists[0]:
    		for b in lists[1]:
    			for c in lists[2]:
    				for d in lists[3]:
    					insert_query="INSERT INTO armor_builds (set_id, %s,%s,%s,%s,armor_rating) VALUES(%d,\'%s\',\'%s\',\'%s\',\'%s\',%d)" \
    						% (a[1],b[1],c[1],d[1],set_id,a[0],b[0],c[0],d[0],a[2]+b[2]+c[2]+d[2])
    					if set_id==1:
    						print(insert_query)
    					self.curr.execute(insert_query)
    					set_id+=1
    	self.conn.commit()
    
    
#Connect to database
#conn = sqlite3.connect(abspath(curdir)+"/Divinity.db")
#print(abspath(curdir)+"\\Database\\Divinity.db")
#conn = sqlite3.connect(abspath(curdir)+"\\Database\\Divinity.db")
#curr = conn.cursor()

#physical weapon builder
def weapon_build(weap_type, character):
	reqs_get="SELECT requirement_name FROM weapon_main WHERE type=\'%s\' GROUP BY requirement_name" % weap_type
	print(reqs_get)	#DEBUG LINE
	curr.execute(reqs_get)
	weap_reqs=curr.fetchall()
	#GET CHAR equipement
	weapons=[]
	curr.execute("DELETE FROM weapon_builds")
	curr.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME=\'weapon_builds\'")
	for a in weap_reqs:
		char_lvl_get="(SELECT %s FROM attributes WHERE name=\'%s\')" % (a[0], character)
		weap_get="SELECT weapon_id, hands FROM weapon_main WHERE type=\'%s\' AND requirement_name=\'%s\' AND requirement_level<=%s" % (weap_type, a[0], char_lvl_get)
		print(weap_get)	#DEBUG LINE
		curr.execute(weap_get)
		temp=curr.fetchall()
		for b in temp:
			insert_query="INSERT INTO weapon_builds (weapon) VALUES(\'%s\')" % b[0]
			print(insert_query)	#Debug lin
			curr.execute(insert_query)
	conn.commit()




#build permutations of accessories
def accessory_builder():
	#get accessories
	curr.execute("SELECT accs_id FROM accessory_main WHERE type=\'Accessory\'")
	accs=curr.fetchall()
	#create temp table hold
	accs_perms=[]
	for a in range(0,len(accs)):
		for b in range(a+1,len(accs)):
			accs_perms.append([accs[a][0],accs[b][0]])
			#print([accs[a][0],accs[b][0]]) #DEBUG LINE
	return accs_perms

#accessory buff calculations




#number selection
def num_select(no_choices):
	print("Please enter only the number from the selections above: ")
	selection_made = False
	#loop until selection made
	while not selection_made:
		choice=input()
		#check if number
		if choice.isnumeric():
			if int(choice) in range(1,no_choices+1):
				print("SELECTION GOOD")
				selection_made = True
				return int(choice)
				break
		print("Invalid input. \nPlease enter only the number of your selection from the choices above.")
        