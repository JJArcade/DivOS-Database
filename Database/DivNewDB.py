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
