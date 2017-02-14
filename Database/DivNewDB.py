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
	#This is the main program area
	weapon_type_select()
	return
	
#Connect to database
conn = sqlite3.connect(abspath(curdir)+"/Divinity.db")
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
def armor_buliding(character):
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
			Boots.append([b[0],b[2])
		elif b[1]=="Chest":
			Chest.append(b[0],b[2])
		elif b[1]=="Gloves":
			Gloves.append(b[0],b[2])
		elif b[1]=="Helmet":
			Helmets.append(b[0],b[2])
	#Store attr. requirements from armors to a list
	curr.execute("SELECT requirement_name FROM armor_main WHERE requirement_name NOT NULL GROUP BY requirement_name")
	req_names=[]
	for a in curr:
		req_names.append(a[0])
	#get armors within range
	for a in req_names:
		char_query="SELECT %s FROM attributes WHERE Name=\'%s\'" % [a,character]
		armors_query="SELECT armor_id, type,armor_rating FROM armor_main WHERE requirement_name=\'%s\' AND requirement_level<=(%s) GROUP BY type" % [a,char_query]
		curr.execute(armors_query)
		selections=curr.fetchall()
		for b in selections:
			if b[1]=="Boots":
				Boots.append([b[0],b[2])
			elif b[1]=="Chest":
				Chest.append(b[0],b[2])
			elif b[1]=="Gloves":
				Gloves.append(b[0],b[2])
			elif b[1]=="Helmets":
				Helmet.append(b[0],b[2])
	#start armor building
	
#combo generator
def combo_maker_plain(lists):
	
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
