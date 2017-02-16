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

def __main__():
	#This is the main program area weapon_type_select()
	armor_building("Leon")
	accessory_builder()
	input("press enter to end")
	quit()
	return

#Connect to database
conn = sqlite3.connect(abspath(curdir)+"/Divinity.db")
#print(abspath(curdir)+"\\Database\\Divinity.db") conn = sqlite3.connect(abspath(curdir)+"\\Database\\Divinity.db")
curr = conn.cursor()

curr.execute("SELECT * FROM Abilities") 
print(curr.fetchall())

#Select weapon types
def weapon_type_select():
	curr.execute("SELECT type FROM weapon_main GROUP BY type")
	weapon_types=curr.fetchall()
	for a in range(0,len(weapon_types)):
		typ=weapon_types[a][0]
		print(str(a+1)+"\t"+typ)
	typ_choice=num_select(len(weapon_types))
	print("You chose "+weapon_types[a-1][0]+" types of weapons.")
	quit()

#Armor builder
def armor_building(character):
	#Armor lists
	Helmets=[]
	Boots=[]
	Chest=[]
	Gloves=[]
	#Get armors that don't have requirements
	curr.execute("SELECT armor_id, type, armor_rating FROM armor_main where requirement_name is Null ORDER BY type")
	easy_armor=curr.fetchall()
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
	curr.execute("SELECT requirement_name FROM armor_main WHERE requirement_name NOT NULL GROUP BY requirement_name")
	req_names=[]
	for a in curr:
		req_names.append(a[0])
	#get armors within range
	for a in req_names:
		char_query="SELECT %s FROM attributes WHERE Name=\'%s\'" % (a,character)
		armors_query="SELECT armor_id, type,armor_rating FROM armor_main WHERE requirement_name=\'%s\' AND requirement_level<=(%s) GROUP BY type" % (a,char_query)
		curr.execute(armors_query)
		selections=curr.fetchall()
		for b in selections:
			if b[1]=="Boots":
				Boots.append(b)
			elif b[1]=="Chest":
				Chest.append(b)
			elif b[1]=="Gloves":
				Gloves.append(b)
			elif b[1]=="Helmets":
				Helmets.append(b)
	#cut down size of lists
	'''print(len(Helmets))
	for a in [Helmets,Chest,Boots,Gloves]:
		curr.execute("DROP TABLE IF EXISTS temp_armors")
		curr.execute("CREATE TABLE temp_armors(id VARCHAR(50) NOT NULL PRIMARY KEY, type TEXT NOT NULL, armor_rating INT NOT NULL)")
		for b in a:
			insert_query="INSERT INTO temp_armors (id, type, armor_rating) VALUES(\'%s\',\'%s\',%d)" % tuple(b)
			print(insert_query)	
			#input("Press enter to continue")'''
	combo_maker_plain([Helmets,Chest,Boots,Gloves])

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
			print([accs[a][0],accs[b][0]]) #DEBUG LINE
	return accs_perms

#accessory buff calculations


#combo generator
def combo_maker_plain(lists):
	items={}
	armor_types=[]
	#fetch armor types
	for a in range(0,len(lists)):
		curr.execute("SELECT type from armor_main where armor_id=\'%s\'" % lists[a][0][0])
		temp=curr.fetchall()
		armor_type=temp[0][0]
		items[a]=lists[a]
		armor_types.append(armor_type)
	print(armor_types)
	#calculate total number of combos
	no_combos=1
	for a in items:
		no_combos*=len(items[a])
	print("There are %d number of combos." % no_combos)
	list_frequency=no_combos
	curr.execute("DELETE FROM armor_builds")
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
					curr.execute(insert_query)
					set_id+=1
	conn.commit()

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

while True:
	__main__() 
	quit()
