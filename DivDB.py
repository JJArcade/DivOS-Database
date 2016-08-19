'''#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  DivDB.py
#  
#  Copyright 2016 JJArcade
#  '''

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



#declare necessary dictionaries
weapon_headers = {}
armor_headers = {}
abil_headers = {}
attr_headers = {}
chars = {}
helmets = {}
chest = {}
undergar = {}
waist = {}
boots = {}
gloves = {}
amulets = {}
shields = {}
accessories = {}
equipment_headers={ 0: 'Helmet', 1: 'Chest', 2: 'Under', 3: 'Waist', 4: 'Boots', 
	5: 'Gloves', 6: 'Hand 1', 7: 'Hand 2', 8: 'Amulet', 9: 'Access. 1', 10: 'Access. 2' }
ratings_headers={ 0: 'Damage', 1: 'Armor Rating', 2: 'Blocking', 3: 'Critical Chance', 
	4: 'Offense Rating', 5: 'Defense Rating', 6: 'Vitality', 7: 'Action Points', 8: 'Movement'}
resistance_headers={ 0: 'Fire Res.', 1: 'Water Res.', 2: 'Earth Res.', 3: 'Air Res.', 
	4: 'Tenebrium Res.', 5: 'Poison Res.'}
weapon_print_headers={0: 'Item Name', 1: 'Type', 2: 'Hands', 3: 'Damage', 4: 'Crit. %',
	5: 'Crit. Dmg.', 6: 'Elem. 1', 7: 'Elem. 1 Dmg.', 8: 'Elem. 2', 9: 'Elem. 2 Dmg',
	10: 'Rarity', 11: 'Value', 12: 'Req.', 13: 'Level', 14: 'Range', 15: 'Spc. 1',
	16: 'Spc. 2', 17: 'Spc. 3', 18: 'Spc. 4'}
def get_table_headers(table):	#Go through the first row of a table and store the info for each column
	column_number = 0
	if table == "weapons":						#Check if it is the weapons table
		for x in weapons[0]:					#lock the row at the first row in the table and cycle through each column
			weapon_headers[column_number]=str(x)#Assign the info stored in each column with it's number in the weapon_headers dictionary
			column_number += 1
	elif table == "armor":
		for x in armor[0]:
			armor_headers[column_number]=str(x)
			column_number += 1
	elif table == "abilities":
		for x in abilities[0]:
			abil_headers[column_number] = str(x)
			column_number += 1
	elif table == "attributes":
		for x in attributes[0]:
			attr_headers[column_number] = str(x)
			column_number += 1
		
def get_characters ():	#Store character names from attributes table
	no_char = list(range(1, len(attributes)))
	for x in no_char:
		chars[x]=str(attributes[x][0])

def store_armor_types():
	#Store each armor entry that matches the declared category
	#in matching dictionary holder
	dict_pos=0
	for x in unq_ident_armor:	#Helmets
		i = str(armor[x][1])
		j = 'Helmet'
		if i==j:
			helmets[dict_pos]=int(x)
		dict_pos+=1
	dict_pos=0
	for x in unq_ident_armor:	#Chest
		i = str(armor[x][1])
		j = 'Chest'
		if i==j:
			chest[dict_pos]=int(x)
			dict_pos+=1
	dict_pos=0
	for x in unq_ident_armor:	#undergarments
		i = str(armor[x][1])
		j = 'Undergarment'
		if i==j:
			undergar[dict_pos]=int(x)
			dict_pos+=1
	dict_pos=0
	for x in unq_ident_armor:	#Waist
		i = str(armor[x][1])
		j = 'Waist'
		if i==j:
			waist[dict_pos]=int(x)
			dict_pos+=1
	dict_pos=0
	for x in unq_ident_armor:	#boots
		i = str(armor[x][1])
		j = 'Boots'
		if i==j:
			boots[dict_pos]=int(x)
			dict_pos+=1
	dict_pos=0
	for x in unq_ident_armor:	#gloves
		i = str(armor[x][1])
		j = 'Gloves'
		if i==j:
			gloves[dict_pos]=int(x)
			dict_pos+=1
	dict_pos=0
	for x in unq_ident_armor:	#amulets
		i = str(armor[x][1])
		j = 'Amulet'
		if i==j:
			amulets[dict_pos]=int(x)
			dict_pos+=1
	dict_pos=0
	for x in unq_ident_armor:	#shields
		i = str(armor[x][1])
		j = 'Shield'
		if i==j:
			shields[dict_pos]=int(x)
			dict_pos+=1
	dict_pos=0
	for x in unq_ident_armor:	#accesories
		i = str(armor[x][1])
		j = 'Accessory'
		if i==j:
			accessories[dict_pos]=int(x)
			dict_pos+=1
		
#
#print out a table format of items provided, specify if 
def view_inventory(is_armor, items_ordered):
	###
	if is_armor:
		headers=armor_headers
		table=armor
	else:
		headers=weapon_print_headers
		table=weapons
	number_of_columns=list(range(0,len(headers)))
	column_spacing=[0]*len(number_of_columns)
	column_spacing[0]=30
	for a in headers:
		if (len(headers[a])+1)>column_spacing[a]:
			column_spacing[a]=len(headers[a])+1
	for a in number_of_columns:
		if a!=0:
			for b in items_ordered:
				if (len(table[b][a])+1)>column_spacing[a]:
					column_spacing[a]=len(table[b][a])+1
	row_str=''
	for a in headers:
		if a<len(headers)-4:
			row_str+=headers[a].ljust(column_spacing[a], ' ')+'|'
		elif a<len(headers)-1:
			row_str+=headers[a]+' |'
		else:
			row_str+=headers[a]
	print(row_str)
	print(''.ljust(sum(column_spacing),'-'))
	##BEGIN PRINTING ROWS
	row_count=0
	for a in items_ordered:
		row_count+=1
		row_str=''
		for b in number_of_columns:
			if b==0:
				if (len(table[a][b])+5)>=column_spacing[b]:
					row_str+=str(row_count)+': '+table[a][b][0:column_spacing[b]-8]+'...'
					row_str=row_str.ljust(column_spacing[b],' ')+'|'
				else:
					row_str+=(str(row_count)+': '+table[a][b]).ljust(column_spacing[b],' ')+'|'
			elif b<len(number_of_columns)-4:
				row_str+=table[a][b].ljust(column_spacing[b],' ')+'|'
			elif b<len(number_of_columns)-1:
				row_str+=table[a][b]+' |'
			else:
				row_str+=table[a][b]
		print(row_str)
	
#	
#sort either weapons or armors by the specified column			
def sorting_order(is_armor, column):
	if is_armor:
		sort_list=[]
		for a in armor_headers:
			if a==column:
				for b in unq_ident_armor:
					if armor[b][column]=='N/A':
						sort_list.append([b,'0'])
					else:
						sort_list.append([b,armor[b][column]])
		is_number=True
		for a in sort_list:
			if not check_numeric(a[1]):
				is_number=False
		if is_number:
			for a in range(0,len(sort_list)):
				sort_list[a][1]=int(sort_list[a][1])
		sort_list=sorted(sort_list, key=operator.itemgetter(1), reverse=True)
		for a in range(0,len(sort_list)):
			sort_list[a]=sort_list[a][0]
	else:
		sort_list=[]
		for a in weapon_headers:
			if a==column:
				for b in unq_ident_weapons:
					if weapons[b][column]=='N/A':
						sort_list.append([b,'0'])
					else:
						sort_list.append([b,weapons[b][column]])
		is_number=True
		for a in sort_list:
			if not check_numeric(a[1]):
				is_number=False
		if is_number:
			for a in range(0,len(sort_list)):
				sort_list[a][1]=float(sort_list[a][1])
		sort_list=sorted(sort_list, key=operator.itemgetter(1), reverse=True)
		for a in range(0,len(sort_list)):
			sort_list[a]=sort_list[a][0]
	return sort_list

#
#Check if value is numeric
def check_numeric(val):
	try:
		float(val)
		return True
	except ValueError:
		return False

#
#print the players data formatted		
def print_players():
	##GET LONGEST FOR EACH COLUMN
	column_spaces={}
	##COLUMN 1
	COLUMN2=[attr_headers, ratings_headers, resistance_headers]
	temp_longest=0
	for a in chars:
		if len(chars[a])>temp_longest:
			temp_longest=len(chars[a])
	column_spaces[1]=temp_longest+1
	##COLUMN 2
	temp_longest=len('Attributes 99')
	for a in COLUMN2:
		for b in a:
			if (len(a[b])+15)>temp_longest:
				temp_longest=len(a[b])+15
	column_spaces[2]=temp_longest
	##COLUMN 3
	temp_longest=0
	for a in abil_headers:
		if (len(abil_headers[a])+6)>temp_longest:
			temp_longest=len(abil_headers[a])+6
	column_spaces[3]=temp_longest
	##START PRINT
	for x in char_list:
		curr_char=char_list[x]
		row_count=1
		row_string=''
		while row_count!=30:
			#print(row_count)
			if row_count==1:	#Print first headers
				row_string=str(curr_char.name).ljust(column_spaces[1],' ')	#column 1
				row_string+='Attributes'.ljust(column_spaces[2],' ')		#column 2
				row_string+='Abilities'.ljust(column_spaces[3],' ')			#column 3
				row_string+='Equipment'										#column 4
				print(row_string)
				equip_count=0
				attr_count=1
				abil_count=1
			elif row_count<=8:	#until end of attributes
				##go until end of attributes
				curr_abil=str(curr_char.abil[abil_count])
				curr_attr=str(curr_char.attr[attr_count])
				curr_equip=curr_char.equipped[equip_count]
				row_string=''.ljust(column_spaces[1],' ')	#column 1
				row_string+=attr_headers[attr_count].ljust(column_spaces[2]-5,' ')+curr_attr.ljust(5,' ')	#column 2
				row_string+=abil_headers[abil_count].ljust(column_spaces[3]-5,' ')+curr_abil.ljust(5,' ')	#column 3
				#Equipment column
				if equip_count!=6 and equip_count!=7:
					row_string+=equipment_headers[equip_count]+": "
					row_string+=armor[curr_equip][0]
				elif equip_count==6:
					row_string+=equipment_headers[equip_count]+": "
					row_string+=weapons[curr_equip][0]
				elif equip_count==7:
					if curr_char.has_shield:
						row_string+=equipment_headers[equip_count]+": "
						row_string+=armor[curr_equip][0]
					else:
						row_string+=equipment_headers[equip_count]+": "
						row_string+=weapons[curr_equip][0]
				##move to next slots
				equip_count+=1
				attr_count+=1
				abil_count+=1
				print(row_string)
			elif row_count==9:	#First break slot
				curr_abil=str(curr_char.abil[abil_count])
				#curr_attr=curr_char.attr[attr_count]
				curr_equip=curr_char.equipped[equip_count]
				row_string=''.ljust(column_spaces[1],' ')	#column 1
				row_string+=''.ljust(column_spaces[2],'-')	#column 2
				row_string+=abil_headers[abil_count].ljust(column_spaces[3]-5,' ')+curr_abil.ljust(5,' ')	#column 3
				#Equipment column
				if equip_count!=6 and equip_count!=7:
					row_string+=equipment_headers[equip_count]+": "
					row_string+=armor[curr_equip][0]
				elif equip_count==6:
					row_string+=equipment_headers[equip_count]+": "
					row_string+=weapons[curr_equip][0]
				elif equip_count==7:
					if curr_char.has_shield:
						row_string+=equipment_headers[equip_count]+": "
						row_string+=armor[curr_equip][0]
					else:
						row_string+=equipment_headers[equip_count]+": "
						row_string+=weapons[curr_equip][0]
				##move to next slots
				equip_count+=1
				#attr_count+=1
				abil_count+=1
				print(row_string)
			elif row_count==10:	#Begin ratings
				curr_abil=str(curr_char.abil[abil_count])
				#curr_attr=curr_char.attr[attr_count]
				curr_equip=curr_char.equipped[equip_count]
				row_string=''.ljust(column_spaces[1],' ')	#column 1
				row_string+='Ratings'.ljust(column_spaces[2],' ')	#column 2
				row_string+=abil_headers[abil_count].ljust(column_spaces[3]-5,' ')+curr_abil.ljust(5,' ')	#column 3
				#Equipment column
				if equip_count!=6 and equip_count!=7:
					row_string+=equipment_headers[equip_count]+": "
					row_string+=armor[curr_equip][0]
				elif equip_count==6:
					row_string+=equipment_headers[equip_count]+": "
					row_string+=weapons[curr_equip][0]
				elif equip_count==7:
					if curr_char.has_shield:
						row_string+=equipment_headers[equip_count]+": "
						row_string+=armor[curr_equip][0]
					else:
						row_string+=equipment_headers[equip_count]+": "
						row_string+=weapons[curr_equip][0]
				##move to next slots
				equip_count+=1
				rate_count=0
				abil_count+=1
				print(row_string)
			elif row_count<=12:	#until end of equipment
				curr_abil=str(curr_char.abil[abil_count])
				curr_rate=str(curr_char.ratings[rate_count])
				curr_equip=curr_char.equipped[equip_count]
				#####
				row_string=''.ljust(column_spaces[1],' ')	#Column 1
				row_string+=ratings_headers[rate_count].ljust(column_spaces[2]-14)+curr_rate.ljust(14,' ')	#Column 2
				row_string+=abil_headers[abil_count].ljust(column_spaces[3]-5,' ')+curr_abil.ljust(5,' ')	#column 3
				#Equipment column
				if equip_count!=6 and equip_count!=7:
					row_string+=equipment_headers[equip_count]+": "
					row_string+=armor[curr_equip][0]
				elif equip_count==6:
					row_string+=equipment_headers[equip_count]+": "
					row_string+=weapons[curr_equip][0]
				elif equip_count==7:
					if curr_char.has_shield:
						row_string+=equipment_headers[equip_count]+": "
						row_string+=armor[curr_equip][0]
					else:
						row_string+=equipment_headers[equip_count]+": "
						row_string+=weapons[curr_equip][0]
				##move to next slots
				equip_count+=1
				rate_count+=1
				abil_count+=1
				print(row_string)
			elif row_count<=19:	#unitl end of ratings
				curr_abil=str(curr_char.abil[abil_count])
				curr_rate=str(curr_char.ratings[rate_count])
				#####
				row_string=''.ljust(column_spaces[1],' ')	#Column 1
				row_string+=ratings_headers[rate_count].ljust(column_spaces[2]-14)+curr_rate.ljust(14,' ')	#Column 2
				row_string+=abil_headers[abil_count].ljust(column_spaces[3]-5,' ')+curr_abil.ljust(5,' ')	#column 3
				##move to next slots
				rate_count+=1
				abil_count+=1
				print(row_string)
			elif row_count==20: #second break
				curr_abil=str(curr_char.abil[abil_count])
				#####
				row_string=''.ljust(column_spaces[1],' ')	#column 1
				row_string+=''.ljust(column_spaces[2],'-')	#column 2
				row_string+=abil_headers[abil_count].ljust(column_spaces[3]-5,' ')+curr_abil.ljust(5,' ')	#column 3
				##move to next slots
				abil_count+=1
				print(row_string)
			elif row_count==21:	#Begin Resistance
				curr_abil=str(curr_char.abil[abil_count])
				#####
				row_string=''.ljust(column_spaces[1],' ')	#column 1
				row_string+='Resistances'.ljust(column_spaces[2],' ')	#column 2
				row_string+=abil_headers[abil_count].ljust(column_spaces[3]-5,' ')+curr_abil.ljust(5,' ')	#column 3
				##move to next slots
				abil_count+=1
				res_count=0
				print(row_string)
			elif row_count<=27:	#until end of resistances
				curr_abil=str(curr_char.abil[abil_count])
				curr_res=str(curr_char.resistance[res_count])+'%'
				#####
				row_string=''.ljust(column_spaces[1],' ')	#column 1
				row_string+=resistance_headers[res_count].ljust(column_spaces[2]-8)+curr_res.ljust(8,' ')	#column 2
				row_string+=abil_headers[abil_count].ljust(column_spaces[3]-5,' ')+curr_abil.ljust(5,' ')	#column 3
				##move to next slots
				abil_count+=1
				res_count+=1
				print(row_string)
			elif row_count<=30:	#until end
				curr_abil=str(curr_char.abil[abil_count])
				#####
				row_string=''.ljust(column_spaces[1],' ')	#column 1
				row_string+=''.ljust(column_spaces[2],' ')	#column 2
				row_string+=abil_headers[abil_count].ljust(column_spaces[3]-5,' ')+curr_abil.ljust(5,' ')	#column 3
				##move to next slots
				abil_count+=1
				print(row_string)
			row_count+=1
		print(''.ljust(column_spaces[1]+column_spaces[2]+column_spaces[3], '-'))

#
#remove weapons from a list that can't be equipped from a characters current attributes				
def filter_weapon_req(wp_list, character):
	req_list = []
	match_list = []
	req_col = 0
	lvl_col = 0
	char_lvl = character.attr[1]
	#Go thorugh weapon headers and find/store the requirements and level column
	for x in weapon_headers:
		if weapon_headers[x] == 'Requirements':
			req_col = x
		elif weapon_headers[x] == 'Level':
			lvl_col = x
	for x in wp_list:
		#go through weapon list and get attr/level requirements
		lvl_req = weapons[x][lvl_col]
		attr_req = weapons[x][req_col]
		#Create tuple list of identifier, required level
		#and atribute requirements
		xstr = (x, lvl_req, str(attr_req))
		req_list.append(xstr)	#Add to req_list
	#Go through entire req_list that was formed
	for x in list(range(0, len(req_list))):
		lvl_match = bool(int(char_lvl) >= int(req_list[x][1]))
		#begin to check attribute requirements
		attr_col = 0
		attr_lvl = 0
		#Filter out the numeric value of attribute requirements
		attr_req = int(req_list[x][2][4:len(req_list[x][2])])
		#cycle through attr headers to look for the match of req attr
		for y in attr_headers:
			attr_head_match = re.match(req_list[x][2][0:3], attr_headers[y][0:3], re.IGNORECASE)
			attr_head_match = bool(attr_head_match)
			if attr_head_match:
				#if match is found, store column number & attr level
				attr_col = y
				attr_lvl = int(character.attr[y])
		attr_match = bool(attr_lvl >= attr_req)
		if attr_match and lvl_match:
			match_list.append(req_list[x][0])
	return match_list

#
#remove armors from a list that can't be equipped from a characters current attributes	
def filter_armor_req(arm_list, character):
	###DEBUG LINE
	#filter_armors_files=open("filtered items.csv", 'w')
	###
	req_list=[]
	match_list=[]
	char_lvl = int(character.attr[1])
	req_col=7
	lvl_col=6
	for x in arm_list:
		#Find level and attribute requirement of each item
		attr_req_str = armor[x][req_col]
		attr_met=False
		if attr_req_str == 'N/A':	#Check  if any attribute is required
			attr_met=True
			attr_req='None'
			attr_req_lvl=0
		else:	#If any attribute is required
			attr_lvl_location = re.search('[0-9]+', attr_req_str)
			attr_lvl_start = attr_lvl_location.start()
			attr_lvl_end = attr_lvl_location.end()
			attr_req_lvl = int(attr_req_str[attr_lvl_start:attr_lvl_end])
			attr_req = attr_req_str[0:3]
		lvl_req = int(armor[x][lvl_col])
		#begin checking those levels against character attributes
		lvl_met = bool(char_lvl>=lvl_req)
		#cycle through attributes and check levels with requirement
		#store_str=str(x)+','+armor[x][0]+','+attr_req_str+','+attr_req+str(attr_req_lvl)+','+str(lvl_req)+','+str(character.attr)	###DEBUG LINE
		for y in attr_headers:
			header_short = attr_headers[y][0:3]
			if header_short == attr_req:
				if int(character.attr[y]) >=attr_req_lvl:
					#store_str+=','+str(y)+header_short+','+str(character.attr[y])	###DEBUG LINE
					attr_met=True
		if lvl_met and attr_met:
			match_list.append(x)
			#store_str+=',Good'	###DEBUG LINE
			#print(armor[x][0] + ' is equippable!')
		#filter_armors_files.write(store_str+'\n')	###DEBUG LINE
	### DEBUG LINE
	#filter_armors_files.close()
	###
	return match_list
	
#	
#Return integer value of a weapons damage range, must specify the high or low range		
def dmg_hilo(weap, typ, hilo):
	if typ == 'physical':
		for x in weapon_headers:
			i = weapon_headers[x]
			if i == 'Damage':
				j = x
		dam = weapons[weap][j]
		dash_loc = re.search('-', dam)
		if bool(re.match('[0-9]', dam)) == False:
			return 0
		dam_lo = int(dam[0:dash_loc.start()])
		dam_hi = int(dam[dash_loc.end():len(dam)])
		if hilo == 'hi':
			return dam_hi
		elif hilo == 'lo':
			return dam_lo
		
#
#get any possible attribute/ability/resistance value buffs that an item will have and return them as a list		
def find_specials(it, typ):
	attr_adj=[0]*(int(len(char1.attr)))
	abil_adj=[0]*(len(char1.abil))
	res_adj=[0]*(len(char1.resistance))
	if it!=0:
		if typ == 'armor':
			spc_cols=[]
			for x in armor_headers:
				i=bool(re.search('special', armor_headers[x], re.IGNORECASE))
				if i:
					spc_cols.append(x)
			for x in spc_cols:
				special = str(armor[it][x])
				find_per = re.search('%', special)
				find_plus = re.search('[+]', special)
				find_min = re.search('-', special)
				if_comma = bool(re.search(',', special))
				if bool(find_plus) or bool(find_min):
					if bool(find_plus):
						attr_abil=special[find_plus.end()+1:len(special)]
						val=float(special[0:find_plus.start()])
					else:
						attr_abil=special[find_min.end()+1:len(special)]
						val=float(special[0:find_min.start()])
					match = 0
					for y in attr_headers:
						if attr_headers[y]==attr_abil:
							attr_adj[y]+=val
							match = 1
					if match==0:
						match=0
					for y in abil_headers:
						if abil_headers[y]==attr_abil:
							abil_adj[y]+=val
							match=1
					if attr_abil=='HP':
						match=1
					if match==0:
						match=0
				elif bool(find_per):
					res_loc=re.search('resistance', special, re.IGNORECASE)
					num_loc=re.search('[0-9]+',special)
					val=float(special[num_loc.start():num_loc.end()])
					if res_loc is None:
						res_typ='NONE'
					else:
						res_typ=special[find_per.end()+1:res_loc.start()-1]
					match = 0
					for y in resistance_headers:
						i=bool(re.search(res_typ, resistance_headers[y], re.IGNORECASE))
						if i:
							res_adj[y]+=val
							match=1
					if match==0:
						match=0
		elif typ=='weapon':
			spc_cols=[]
			#get the numner of special columns in the headers
			for x in weapon_headers:
				i=bool(re.search('special', weapon_headers[x], re.IGNORECASE))
				if i:
					spc_cols.append(x)
			for x in spc_cols:
				special = str(weapons[it][x])
				find_per = re.search('%', special)
				find_plus = re.search('[+]', special)
				find_min = re.search('-', special)
				if_comma = bool(re.search(',', special))
				if bool(find_plus) or bool(find_min):
					if bool(find_plus):
						attr_abil=special[find_plus.end()+1:len(special)]
						val=float(special[0:find_plus.start()])
					else:
						attr_abil=special[find_min.end()+1:len(special)]
						val=float(special[0:find_min.start()])
					match = 0
					for y in attr_headers:
						if attr_headers[y]==attr_abil:
							match = 1
					if match==0:
						match=0
					for y in abil_headers:
						if abil_headers[y]==attr_abil:
							match=1
					if attr_abil=='HP':
						match=1
					if match==0:
						match=0
				elif bool(find_per):
					res_loc=re.search('resistance', special, re.IGNORECASE)
					if res_loc is None:
						res_typ='NONE'
					else:
						res_typ=special[find_per.end()+1:res_loc.start()-1]
					match = 0
					for y in resistance_headers:
						val=float(special[0:find_per.start()])
						i=bool(re.search(res_typ, resistance_headers[y], re.IGNORECASE))
						if i:
							res_adj[y]+=val
							match=1
					if match==0:
						match=0
	total_adj=[attr_adj, abil_adj, res_adj]
	return total_adj

#
#gather all possible armor sets and from highest to lowest armour rating for a character
def armor_max_def(char):
	#Get all possible armor combos
	equipped=[0,1,4,5]
	all_armors=get_all_equips(equipped)
	armors_combos=armor_item_combos(all_armors, False)
	count=len(armors_combos)
	print('Total possible Armour set combinations: '+str(count))
	if len(used_items.armors)>0:
		print('Would you like to remove any items that have conflicts with other characters now?')
		armor_combos=[]
		if 'y'==yes_or_no():
			for a in armors_combos:
				set_good=True
				for b in a:
					if b in used_items.armors:
						set_good=False
				if set_good:
					armor_combos.append(a)
			print("New number of combinations: "+str(len(armor_combos)))
		else:
			armor_combos=armors_combos
	else:
		armor_combos=armors_combos
	##ADD ARMOUR RATING FROM COMBO TO LIST
	for x in range(0,len(armor_combos)):
		total_armour_rating=0
		for y in armor_combos[x]:
			if y!=0:
				curr_armour_rating=int(armor[y][2])
				total_armour_rating+=curr_armour_rating
		armor_combos[x]=[armor_combos[x], total_armour_rating]
		
	armor_combos=sorted(armor_combos, key=operator.itemgetter(1), reverse=True)
	##THIN THE HERD
	print("Please enter the number of armors you would like to search."+
		'\n'+"Note the larger the number of sets, the longer the calculation will take."+
		'\n'+"Suggested value should result in number of sets less than 10,000.")
	print("Enter integer value, number will rounded if not.")
	thin_num=number_select(len(armor_combos))
	thin_margin=int(thin_num)
	del armor_combos[thin_margin:len(armor_combos)]
	print("Sets cut down to "+str(len(armor_combos))+" sets.")
	good_armors=[]
	##GO THROUGH COMOBOS TO SEE WHICH ONES ARE EQUIPABLE
	#store_sets=open(abspath('.')+'\\armors sets.txt', 'w')	#DELETE LATER
	for x in armor_combos:
		store_str=str(x)
		##GET JUST THE ACTUAL ITEMS IN 
		curr_combo=[]
		for y in x[0]:
			if y!=0:
				curr_combo.append(y)
		##GET CHARACTER ATTRIBUTES 
		curr_attr=[0]*len(char.attr)
		for y in range(0,len(char.attr)):
			if y!=0:
				curr_attr[y]=int(char.attr[y])
		##ADD ANY BUFFS FROM ARMOR
		armor_buffs=[0]*len(char.attr)
		for y in curr_combo:	#ADD TOTAL BUFFS FROM ARMOR TO 'armor_buffs'
			item_buffs=find_specials(y, 'armor')
			item_buffs=item_buffs[0]
			for z in range(0,len(item_buffs)):
				armor_buffs[z]+=item_buffs[z]
		for y in range(0,len(curr_attr)): #ADD BUFFS TO CHARACTER'S CURRENT ATTRIBUTES
			curr_attr[y]+=armor_buffs[y]
		##GET ALL REQUIREMENTS OF SET
		set_req=[0]*len(char.attr)
		reqs_for_armors=[]
		for y in curr_combo:
			curr_req=armor[y][7]
			##FIND LEVEL OF CURRENT ITEM REQUIREMENT
			if curr_req!='N/A':
				num_loc=re.search('[0-9]+', curr_req)
				curr_req_level=int(curr_req[num_loc.start():num_loc.end()])
			##GET REQUIRENT ATTRIBUTE NAME AND LOCATION
			for z in attr_headers:
				if attr_headers[z][0:3]==curr_req[0:3]:
					##IF HIGHEST REQUIREMENT REPLACE
					if set_req[z]<curr_req_level:
						set_req[z]=curr_req_level
		for y in range(0,len(curr_attr)):
			i_char=curr_attr[y]
			j_set=set_req[y]
			if i_char<j_set:
				if len(reqs_for_armors)==0:
					reqs_for_armors.append(attr_headers[y])
				else:
					already_there=False
					for a in reqs_for_armors:
						if a==attr_headers[y]:
							already_there=True
					if not already_there:
						reqs_for_armors.append(attr_headers[z])
		#store_str+=', '+str(set_req)+', '+str(curr_attr)+', '+str(reqs_for_armors)
		##IF THERE ARE SEARCH TERMS, ACCESSORIES WILL BE REQUIRED TO EQUIP SET
		if len(reqs_for_armors)>0:
			##GET SLOTS TO GET BUFFS FROM
			skip_list=[0,1,4,5,6,7,10]	#SKIP ALL ARMOR PIECES, WEAPONS, AND SHIELDS
			buff_equip_slots=[2,3,8,9]
			buff_items=search_for_specials(buff_equip_slots, reqs_for_armors)
			##MAKE COMBOS AND TEST BUFFS
			buff_combos=armor_item_combos(buff_items, True)
			for a in buff_combos:
				total_attr_buff=[0]*len(curr_attr)
				for b in a:
					if b!=0:
						curr_specials=find_specials(b, 'armor')
						curr_specials=curr_specials[0]
						for c in range(0,len(curr_specials)):
							total_attr_buff[c]+=curr_specials[c]
				##CHECK IF COMBO BUFFS ALLOW FOR ARMOR TO BE EQUIPPED
				good_combo=True
				for b in range(0,len(total_attr_buff)):
					total_attr=curr_attr[b]+total_attr_buff[b]
					if total_attr<set_req[b]:
						good_combo=False
				if good_combo:	#add good combo to list
					store_str+=', '+str(a)
					x.append(a)
			if len(x)>2:
				good_armors.append(x)
		else:	##ARMOR SET IS EQUIPPABLE AS IS
			good_armors.append(x)
		#store_sets.write(store_str+'\n')
	#store_sets.close()
	print("Total Armour set solutions found: "+str(len(good_armors)))
	#print(good_armors[0])
	return good_armors

#
#gather all possible armor sets from a characters open slots from highest to lowest armour rating
def armor_max_open(char):
	#Get all possible armor combos
	equipped=[0,1,4,5]
	open_equipped=[]
	for a in equipped:
		if char.equipped[a]==0:
			open_equipped.append(a)
	if len(open_equipped)!=0:
		equipped=open_equipped
	else:
		print("All armour slots full, building sets from default slots.")
	all_armors=get_all_equips(equipped)
	armor_combos=armor_item_combos(all_armors, False)
	count=len(armor_combos)
	##ADD ARMOUR RATING FROM COMBO TO LIST
	for x in range(0,len(armor_combos)):
		total_armour_rating=0
		for y in armor_combos[x]:
			if y!=0:
				curr_armour_rating=int(armor[y][2])
				total_armour_rating+=curr_armour_rating
		armor_combos[x]=[armor_combos[x], total_armour_rating]
	print('Total possible Armour set combinations: '+str(count))
	armor_combos=sorted(armor_combos, key=operator.itemgetter(1), reverse=True)
	##THIN THE HERD
	print("Please enter the number of armors you would like to search."+
		'\n'+"Note the larger the number of sets, the longer the calculation will take."+
		'\n'+"Suggested value should result in number of sets less than 10,000.")
	print("Enter integer value, number will rounded if not.")
	thin_num=number_select(len(armor_combos))
	thin_margin=int(thin_num)
	del armor_combos[thin_margin:len(armor_combos)]
	print("Sets cut down to "+str(len(armor_combos))+" sets.")
	good_armors=[]
	##GO THROUGH COMOBOS TO SEE WHICH ONES ARE EQUIPABLE
	#store_sets=open(abspath('.')+'\\armors sets.txt', 'w')	#DELETE LATER
	for x in armor_combos:
		store_str=str(x)
		##GET JUST THE ACTUAL ITEMS IN 
		curr_combo=[]
		for y in x[0]:
			if y!=0:
				curr_combo.append(y)
		##GET CHARACTER ATTRIBUTES 
		curr_attr=[0]*len(char.attr)
		for y in range(0,len(char.attr)):
			if y!=0:
				curr_attr[y]=int(char.attr[y])
		##ADD ANY BUFFS FROM ARMOR
		armor_buffs=[0]*len(char.attr)
		for y in curr_combo:	#ADD TOTAL BUFFS FROM ARMOR TO 'armor_buffs'
			item_buffs=find_specials(y, 'armor')
			item_buffs=item_buffs[0]
			for z in range(0,len(item_buffs)):
				armor_buffs[z]+=item_buffs[z]
		for y in range(0,len(curr_attr)): #ADD BUFFS TO CHARACTER'S CURRENT ATTRIBUTES
			curr_attr[y]+=armor_buffs[y]
		##GET ALL REQUIREMENTS OF SET
		set_req=[0]*len(char.attr)
		reqs_for_armors=[]
		for y in curr_combo:
			curr_req=armor[y][7]
			##FIND LEVEL OF CURRENT ITEM REQUIREMENT
			if curr_req!='N/A':
				num_loc=re.search('[0-9]+', curr_req)
				curr_req_level=int(curr_req[num_loc.start():num_loc.end()])
			##GET REQUIRENT ATTRIBUTE NAME AND LOCATION
			for z in attr_headers:
				if attr_headers[z][0:3]==curr_req[0:3]:
					##IF HIGHEST REQUIREMENT REPLACE
					if set_req[z]<curr_req_level:
						set_req[z]=curr_req_level
		#COMPARE SET REQUIREMENTS TO CHAR ATTRIBUTES AFTER BUFFS FROM ARMOR
		for y in range(0,len(curr_attr)):
			i_char=curr_attr[y]
			j_set=set_req[y]
			if i_char<j_set:	#SET REQ IS HIGHER, ADD ATTRIBUTE REQ TO LIST IF NOT ALREADY THERE
				if len(reqs_for_armors)==0:
					reqs_for_armors.append(attr_headers[y])
				else:
					already_there=False
					for a in reqs_for_armors:
						if a==attr_headers[y]:
							already_there=True
					if not already_there:
						reqs_for_armors.append(attr_headers[z])
		#store_str+=', '+str(set_req)+', '+str(curr_attr)+', '+str(reqs_for_armors)
		##IF THERE ARE SEARCH TERMS, ACCESSORIES WILL BE REQUIRED TO EQUIP SET
		if len(reqs_for_armors)>0:
			##GET SLOTS TO GET BUFFS FROM
			skip_list=[0,1,4,5,6,7,10]	#SKIP ALL ARMOR PIECES, WEAPONS, AND SHIELDS
			#buff_equip_slots=[2,3,8,9]
			buff_equip_slots=[]
			##ADD ONLY SLOTS THAT ARE EMPTY
			for a in range(0,len(char.equipped)):
				if a not in skip_list:
					ie=char.equipped[a]
					if ie==0:
						buff_equip_slots.append(a)
			buff_items=search_for_specials(buff_equip_slots, reqs_for_armors)
			##MAKE COMBOS AND TEST BUFFS
			buff_combos=armor_item_combos(buff_items, True)
			for a in buff_combos:
				total_attr_buff=[0]*len(curr_attr)
				for b in a:
					if b!=0:
						curr_specials=find_specials(b, 'armor')
						curr_specials=curr_specials[0]
						for c in range(0,len(curr_specials)):
							total_attr_buff[c]+=curr_specials[c]
				##CHECK IF COMBO BUFFS ALLOW FOR ARMOR TO BE EQUIPPED
				good_combo=True
				for b in range(0,len(total_attr_buff)):
					total_attr=curr_attr[b]+total_attr_buff[b]
					if total_attr<set_req[b]:
						good_combo=False
				if good_combo:	#add good combo to list
					store_str+=', '+str(a)
					x.append(a)
			if len(x)>2:
				good_armors.append(x)
		else:	##ARMOR SET IS EQUIPPABLE AS IS
			good_armors.append(x)
		#store_sets.write(store_str+'\n')
	#store_sets.close()
	print("Total Armour set solutions found: "+str(len(good_armors)))
	#print(good_armors[0])
	return good_armors

#
#gather all possible armor sets from armor pieces that meet character's attributes
def armor_max_filtered(char):
	#Get all possible armor combos
	equipped=[0,1,4,5]
	all_armors_raw=get_all_equips(equipped)
	all_armors=filter_armor_req(all_armors_raw, char)
	#####	Debug file section
	'''raw_armors_file=open("filtered armors.txt", 'w')
	for a in all_armors_raw:
		store_str=str(a)
		if a in all_armors:
			store_str+=",Good"+'\n'
		else:
			store_str+=",REMOVED"+'\n'
		raw_armors_file.write(store_str)
	raw_armors_file.close()'''
	#####
	armor_combos_Wconflicts=armor_item_combos(all_armors, False)
	count=len(armor_combos_Wconflicts)
	print('Total possible Armour set combinations: '+str(count))
	if len(used_items.armors)>0:
		print('Would you like to remove any items that have conflicts with other characters now?')
		armor_combos=[]
		if 'y'==yes_or_no():
			for a in armor_combos_Wconflicts:
				set_good=True
				for b in a:
					if b in used_items.armors:
						set_good=False
				if set_good:
					armor_combos.append(a)
			print("New number of combinations: "+str(len(armor_combos)))
		else:
			armor_combos=armor_combos_Wconflicts
	else:
		armor_combos=armor_combos_Wconflicts
	##ADD ARMOUR RATING FROM COMBO TO LIST
	for x in range(0,len(armor_combos)):
		total_armour_rating=0
		for y in armor_combos[x]:
			if y!=0:
				curr_armour_rating=int(armor[y][2])
				total_armour_rating+=curr_armour_rating
		armor_combos[x]=[armor_combos[x], total_armour_rating]
		
	armor_combos=sorted(armor_combos, key=operator.itemgetter(1), reverse=True)
	##THIN THE HERD
	print("Please enter the number of armors you would like to search."+
		'\n'+"Note the larger the number of sets, the longer the calculation will take."+
		'\n'+"Suggested value should result in number of sets less than 10,000.")
	print("Enter integer value, number will rounded if not.")
	thin_num=number_select(len(armor_combos))
	thin_margin=int(thin_num)
	del armor_combos[thin_margin:len(armor_combos)]
	print("Sets cut down to "+str(len(armor_combos))+" sets.")
	good_armors=[]
	##GO THROUGH COMOBOS TO SEE WHICH ONES ARE EQUIPABLE
	#store_sets=open(abspath('.')+'\\armors sets.txt', 'w')	#DELETE LATER
	for x in armor_combos:
		store_str=str(x)
		##GET JUST THE ACTUAL ITEMS IN 
		curr_combo=[]
		for y in x[0]:
			if y!=0:
				curr_combo.append(y)
		##GET CHARACTER ATTRIBUTES 
		curr_attr=[0]*len(char.attr)
		for y in range(0,len(char.attr)):
			if y!=0:
				curr_attr[y]=int(char.attr[y])
		##ADD ANY BUFFS FROM ARMOR
		armor_buffs=[0]*len(char.attr)
		for y in curr_combo:	#ADD TOTAL BUFFS FROM ARMOR TO 'armor_buffs'
			item_buffs=find_specials(y, 'armor')
			item_buffs=item_buffs[0]
			for z in range(0,len(item_buffs)):
				armor_buffs[z]+=item_buffs[z]
		for y in range(0,len(curr_attr)): #ADD BUFFS TO CHARACTER'S CURRENT ATTRIBUTES
			curr_attr[y]+=armor_buffs[y]
		##GET ALL REQUIREMENTS OF SET
		set_req=[0]*len(char.attr)
		reqs_for_armors=[]
		for y in curr_combo:
			curr_req=armor[y][7]
			##FIND LEVEL OF CURRENT ITEM REQUIREMENT
			if curr_req!='N/A':
				num_loc=re.search('[0-9]+', curr_req)
				curr_req_level=int(curr_req[num_loc.start():num_loc.end()])
			##GET REQUIRENT ATTRIBUTE NAME AND LOCATION
			for z in attr_headers:
				if attr_headers[z][0:3]==curr_req[0:3]:
					##IF HIGHEST REQUIREMENT REPLACE
					if set_req[z]<curr_req_level:
						set_req[z]=curr_req_level
		#COMPARE SET REQS WITH CHAR ATTRIBUTES
		for y in range(0,len(curr_attr)):
			i_char=curr_attr[y]
			j_set=set_req[y]
			if i_char<j_set:	#SET REQ HIGHER THAN ATTRIBUTE, ADD ATTRIBUTE TO SEARCH LIST OF NOT THERE ALREADY
				if len(reqs_for_armors)==0:
					reqs_for_armors.append(attr_headers[y])
				else:
					already_there=False
					for a in reqs_for_armors:
						if a==attr_headers[y]:
							already_there=True
					if not already_there:
						reqs_for_armors.append(attr_headers[z])
		#store_str+=', '+str(set_req)+', '+str(curr_attr)+', '+str(reqs_for_armors)
		##IF THERE ARE SEARCH TERMS, ACCESSORIES WILL BE REQUIRED TO EQUIP SET
		if len(reqs_for_armors)>0:
			##GET SLOTS TO GET BUFFS FROM
			skip_list=[0,1,4,5,6,7,10]	#SKIP ALL ARMOR PIECES, WEAPONS, AND SHIELDS
			buff_equip_slots=[2,3,8,9]
			buff_items=search_for_specials(buff_equip_slots, reqs_for_armors)
			##MAKE COMBOS AND TEST BUFFS
			buff_combos=armor_item_combos(buff_items, True)
			for a in buff_combos:
				total_attr_buff=[0]*len(curr_attr)
				for b in a:
					if b!=0:
						curr_specials=find_specials(b, 'armor')
						curr_specials=curr_specials[0]
						for c in range(0,len(curr_specials)):
							total_attr_buff[c]+=curr_specials[c]
				##CHECK IF COMBO BUFFS ALLOW FOR ARMOR TO BE EQUIPPED
				good_combo=True
				for b in range(0,len(total_attr_buff)):
					total_attr=curr_attr[b]+total_attr_buff[b]
					if total_attr<set_req[b]:
						good_combo=False
				if good_combo:	#add good combo to list
					store_str+=', '+str(a)
					x.append(a)
			if len(x)>2:
				good_armors.append(x)
		else:	##ARMOR SET IS EQUIPPABLE AS IS
			good_armors.append(x)
		#store_sets.write(store_str+'\n')
	#store_sets.close()
	print("Total Armour set solutions found: "+str(len(good_armors)))
	#print(good_armors[0])
	return good_armors

#
#get weapons sets from highest to lowest damage, specify damage type
def max_phys_damage(char, damage_type):
	##GO THROUGH WEAPON HEADERS TO FIND DAMAGE TYPE & DAMAGE COLUMN NUMBER
	for x in weapon_headers:
		if weapon_headers[x]=='Type':
			type_col=x
	##GO THROUGH ALL WEAPONS AND STORE WEAPONS OF SELECTED TYPE
	weapon_list=[]
	for x in unq_ident_weapons:
		match_type=re.search(damage_type, weapons[x][type_col], re.IGNORECASE)
		match_type=bool(match_type)
		current_dmg=dmg_hilo(x, 'physical', 'lo')
		if match_type:
			#STORE WEAPON NUMBER AND LO DAMAGE TO "weapon_list"
			weapon_list.append([x,current_dmg])
	print('Total number of '+damage_type+' weapons: '+str(len(weapon_list)))
	##CREATE SEPERATE LIST FOR SINGLE HANDED WEAPONS
	single_handed_weapons=[]
	for x in weapon_list:
		curr_weapon=x[0]
		hands_required=weapons[curr_weapon][2]
		if hands_required=='N/A':
			hands_required=0
		else:
			hands_required=int(hands_required)
		if hands_required==1:
			single_handed_weapons.append(x)
	##CREATE A LIST FOR ALL DUAL WIELDING WEAPONS AND THEIR DAMAGE
	##IF THERE ARE MORE THAN 1 SINGLE HANDED WEAPONS
	if len(single_handed_weapons)>1:
		dual_wield_combos=[]
		i=0
		for x in range(0,len(single_handed_weapons)):
			i+=1
			first_weap=single_handed_weapons[x][0]
			first_dam=single_handed_weapons[x][1]
			for y in range(i,len(single_handed_weapons)):
				second_weap=single_handed_weapons[y][0]
				second_dam=single_handed_weapons[y][1]
				current_combo=[first_weap, second_weap]
				combo_dam=first_dam+second_dam
				dual_wield_combos.append([current_combo, combo_dam])
		print('Total number of Dual Wield combinations is: '+str(len(dual_wield_combos)))
		##SORT 'dual_wield_combos' BY DAMAGE FROM HIGH-LOW
		dual_wield_combos=sorted(dual_wield_combos, key=lambda dual_wield_combos: dual_wield_combos[1], reverse=True)
	##SORT "weapon_list" BY DAMAGE
	weapon_list=sorted(weapon_list, key=lambda weapon_list: weapon_list[1], reverse=True)
	##BEGIN SEEING WHICH WEAPONS CAN BE EQUIPPED WITH THE MOST DAMAGE
	##DAMAGE=WEAPON DAMAGE+ABILITY FOR WEAPON TYPE+BUFFS
	##Calculate Character's damage with weapon equipped
	for x in range(0,len(weapon_list)):
		curr_weap=weapon_list[x][0]
		hands_required=weapons[curr_weap][2]
		if hands_required=='N/A':
			hands_required=0
		else:
			hands_required=int(hands_required)
		##2 HANDED WEAPONS
		if hands_required==2:
			##IF A CROSSBOW/ARBALEST
			if bool(re.search('crossbow', weapons[curr_weap][0], re.IGNORECASE)) or\
				bool(re.search('arbalest', weapons[curr_weap][0], re.IGNORECASE)):
				crossbow_col=2
				crossbow_abil=int(char.abil[crossbow_col])
				buff_damage=weapon_list[x][1]
				weapon_list[x].append(round(buff_damage,4))
			##IF A BOW
			elif bool(re.search('bow', weapons[curr_weapon][0], re.IGNORECASE)):
				bow_col=1
				bow_abil=int(char.abil[bow_col])
				buff_damage=weapon_list[x][1]*(1+.1*bow_abil)
				weapon_list[x].append(round(buff_damage,4))
			else:
				two_handed_col=5
				two_handed_abil=int(char.attr[two_handed_col])
				buff_damage=weapon_list[x][1]
				weapon_list[x].append(round(buff_damage,4))
		else:
			singlehand_col=4
			singlehand_abil=int(char.attr[singlehand_col])
			buff_damage=weapon_list[x][1]*(1+.1*singlehand_abil)
			weapon_list[x].append(round(buff_damage,4))
	##Calculate Dual Wielding equipped damage
	for x in dual_wield_combos:
		weapon_1=x[0][0]
		weapon_2=x[0][1]
		current_dmg=int(x[1])
		dual_wield_abil=char.abil[3]
		if dual_wield_abil==0:
			current_dmg*=.7
			current_dmg=round(current_dmg,3)
			x.append(current_dmg)
		elif dual_wield_abil==1 or dual_wield_abil==2:
			current_dmg*=.8
			current_dmg=round(current_dmg,3)
			x.append(current_dmg)
		elif dual_wield_combos==3:
			current_dmg*=.9
			current_dmg=round(current_dmg,3)
			x.append(current_dmg)
		elif dual_wield_combos==4 or dual_wield_combos==5:
			current_dmg*=1
			current_dmg=round(current_dmg,3)
			x.append(current_dmg)
		elif dual_wield_combos==6:
			current_dmg*=1.05
			current_dmg=round(current_dmg,3)
			x.append(current_dmg)	
	##GO THROUGH BEST WEAPONS AND CHECK IF IT'S EQUIPABLE
	for x in weapon_list:
		weap=x[0]
		req_col=12
		weap_req=weapons[weap][req_col]
		#Find character matching attribute level
		for y in attr_headers:
			if attr_headers[y][0:3]==weap_req[0:3]:
				attr_col=int(y)
		#Get weap_req integer value
		num_loc=re.search('[0-9]+', weap_req)
		weap_req=int(weap_req[num_loc.start():num_loc.end()])
		if int(char.attr[attr_col])>=weap_req:
			x.append('y')
		else:
			x.append('n')
			x.append([attr_headers[attr_col],weap_req])
			x.append(['none'])
	for x in dual_wield_combos:
		weap_1=x[0][0]
		weap_2=x[0][1]
		req_col=12
		weap_1_req=weapons[weap_1][req_col]
		weap_2_req=weapons[weap_2][req_col]
		#Find character matching attribute level
		for y in attr_headers:
			if attr_headers[y][0:3]==weap_1_req[0:3]:
				attr_col_1=int(y)
		for y in attr_headers:
			if attr_headers[y][0:3]==weap_2_req[0:3]:
				attr_col_2=int(y) 
		#Get weap_req integer value
		num_loc_1=re.search('[0-9]+', weap_1_req)
		num_loc_2=re.search('[0-9]+', weap_2_req)
		weap_1_req=int(weap_1_req[num_loc_1.start():num_loc_1.end()])
		weap_2_req=int(weap_2_req[num_loc_2.start():num_loc_2.end()])
		#Append lists to mark if equippable or not plus requirements
		if int(char.attr[attr_col_1])>=weap_1_req:
			if char.attr[attr_col_2]>=weap_2_req:
				x.append('y')
			else:
				x.append('n')
				x.append('none')
				x.append([attr_headers[attr_col_2],weap_2_req])
		else:
			if int(char.attr[attr_col_2])>=weap_2_req:
				x.append('n')
				x.append([attr_headers[attr_col_1],weap_1_req])
				x.append('none')
			else:
				x.append('n')
				x.append([attr_headers[attr_col_1],weap_1_req])
				x.append([attr_headers[attr_col_2],weap_2_req])
	##MAKE LIST OF WEAPONS THAT NEED BUFFS
	need_buffs=[]
	for x in weapon_list:
		if x[3]=='n':
			need_buffs.append(x)
	need_buffs_dual=[]
	for x in dual_wield_combos:
		if x[3]=='n':
			need_buffs_dual.append(x)
	##FOR EACH WEAPON THAT NEEDS BUFFS
	##SEARCH FOR ITEMS WITH THOSE BUFFS
	temp_attr=char.attr
	if len(need_buffs)>0:	#Single weapons that are unequipable
		for x in need_buffs:
			temp_attr=char.attr
			weap_specials=find_specials(x[0], 'weapon')
			weap_specials=weap_specials[0]
			##ADD ANY POSSIBLE BUFFS FROM WEAPONS TO CHARACTER ATTRIBUTES
			for y in range(0,len(temp_attr)):
				if y>1:
					temp_attr[y]+=int(weap_specials[y])
			for y in attr_headers:
				if x[4][0]==attr_headers[y]:
					attr_col=y
			if temp_attr[attr_col]<=x[4][1]:
				##ITEM STILL UNEQUIPABLE, BEGIN SEARCHING FOR 
				##ITEMS IN CHARACTER'S OPEN SLOTS
				equipped=char.equipped
				equip_item_list=[]
				search_item_list=[]
				make_access_combos=False
				for y in range(0,len(equipped)):
					if equipped[y]==0:
						if y==10:
							if equipped[9]!=0:
								equip_item_list.append(9)
							else:
								##BOTH ACCESS SLOTS OPEN
								make_access_combos=True
						elif y!=6:	#DO NOT ADD WEAPONS TO THIS LIST
							equip_item_list.append(y)
				search_item_list.append(x[4][0])	#add weapon req to search
				buff_items=search_for_specials(equip_item_list, search_item_list)
				##GENERATE COMBOS FROM SEARCHED ITEMS
				item_combos=armor_item_combos(buff_items, make_access_combos)
				##GET COMBINED BUFFS OF COMBO LIST
				temp_buffs=[]
				for y in item_combos:
					for h in range(0,len(y)):
						z=y[h]
						A=find_specials(z, 'armor')
						A=A[0]
						if len(temp_buffs)==0:
							temp_buffs=A
						else:
							for a in range(0,len(A)):
								temp_buffs[a]+=A[a]
					##IF BUFFS ARE ENOUGH TO MEET REQ,
					##ADD Y TO END OF COMBO_STRING, ELSE ADD N
					if temp_attr[attr_col]+temp_buffs[attr_col]>=x[4][1]:
						#y=[y, 'y']
						x[3]='y'
						x.append(y)
			else:
				##WEAPON IS EQUIPABLE JUST FROM WEAPON BUFFS
				x[3]='y'
		for x in need_buffs:	##ADD NEED BUFF ITEMS BACK TO MAIN LIST
			for y in weapon_list:
				if x[0:3]==y[0:3]:
					y=x
	if len(need_buffs_dual)>0:	#Dual wield combos that are unequipable
		for x in need_buffs_dual:
			temp_attr=[]
			for y in char.attr:
				if type(y)==str:
					temp_attr.append(0)
				else:
					temp_attr.append(y)
			weap_specials_1=find_specials(x[0][0], 'weapon')
			weap_specials_2=find_specials(x[0][1], 'weapon')
			weap_specials_1=weap_specials_1[0]
			weap_specials_2=weap_specials_2[0]
			weap_specials=[0]*len(weap_specials_1)
			for y in range(0,len(weap_specials_1)):	#Consolidate both weapons buffs into one list
				weap_specials[y]+=int(weap_specials_1[y])
				weap_specials[y]+=int(weap_specials_2[y])
			for y in range(0,len(temp_attr)):
				if y>1:
					temp_attr[y]+=int(weap_specials[y])
			for y in attr_headers:
				if x[4][0]==attr_headers[y]:
					attr_col_1=y
				elif x[5][0]==attr_headers[y]:
					attr_col_2=y
			if x[4]=='none':
				weap_req_1=0
				attr_col_1=0
			else:
				weap_req_1=x[4][1]
			if x[5]=='none':
				weap_req_2=0
				attr_col_2=0
			else:
				weap_req_2=x[5][1]
			if temp_attr[attr_col_1]<weap_req_1 and\
				temp_attr[attr_col_2]<weap_req_2:
				##ITEMS STILL UNEQUIPABLE, BEGIN SEARCHING FOR 
				##ITEMS IN CHARACTER'S OPEN SLOTS
				equipped=char.equipped
				equip_item_list=[]
				search_item_list=[]
				make_access_combos=False
				for y in range(0,len(equipped)):
					if equipped[y]==0:
						if y==10:
							if equipped[9]!=0:
								equip_item_list.append(9)
							else:
								##BOTH ACCESS SLOTS OPEN
								make_access_combos=True
						elif y>7 or y<6:	#DO NOT ADD WEAPONS TO THIS LIST
							equip_item_list.append(y)
				search_item_list.append(x[4][0])	#add weapon 1 req to search list
				if x[4][0]!=x[5][0]:
					search_item_list.append(x[5][0])	#add weapon 2 req to search list
				buff_items=search_for_specials(equip_item_list, search_item_list)
				##GENERATE ITEM COMBOS FOR SEARCHED ITEMS
				item_combos=armor_item_combos(buff_items, make_access_combos)
				##GET COMBINED BUFFS OF COMBO LIST
				temp_buffs=[]
				for y in item_combos:
					for z in y:
						if z!=0:
							A=find_specials(z, 'armor')
							A=A[0]
							if len(temp_buffs)==0:
								temp_buffs=A
							else:
								for a in range(0,len(A)):
									temp_buffs[a]+=A[a]
					##IF BUFFS ARE ENOUGH TO MEET REQ,
					##ADD COMBO TO X LIST AND CHANGE x[3] TO Y
					if len(temp_buffs)>0:
						if temp_attr[attr_col_1]+temp_buffs[attr_col_1]>=weap_req_1 and\
							temp_attr[attr_col_2]+temp_buffs[attr_col_2]>=weap_req_2:
							x[3]='y'
							x.append(y)
			elif temp_attr[attr_col_1]<weap_req_1:
				##ITEM 1 STILL UNEQUIPABLE, BEGIN SEARCHING FOR 
				##ITEMS IN CHARACTER'S OPEN SLOTS
				equipped=char.equipped
				equip_item_list=[]
				search_item_list=[]
				make_access_combos=False
				for y in range(0,len(equipped)):
					if equipped[y]==0:
						if y==10:
							if equipped[9]!=0:
								equip_item_list.append(9)
							else:
								##BOTH ACCESS SLOTS OPEN
								make_access_combos=True
						elif y>7 or y<6:	#DO NOT ADD WEAPONS TO THIS LIST
							equip_item_list.append(y)
				search_item_list.append(x[4][0])	#add weapon 1 req to search list
				#search_item_list.append(x[5][0])	#add weapon 2 req to search list
				buff_items=search_for_specials(equip_item_list, search_item_list)
				##GENERATE ITEM COMBOS FOR SEARCHED ITEMS
				item_combos=armor_item_combos(buff_items, make_access_combos)
				##GET COMBINED BUFFS OF COMBO LIST
				temp_buffs=[]
				for y in item_combos:
					for z in y:
						if z!=0:
							A=find_specials(z, 'armor')
							A=A[0]
							if len(temp_buffs)==0:
								temp_buffs=A
							else:
								for a in range(0,len(A)):
									temp_buffs[a]+=A[a]
					##IF BUFFS ARE ENOUGH TO MEET REQ,
					##ADD COMBO TO X LIST AND CHANGE x[3] TO Y
					if temp_attr[attr_col_1]+temp_buffs[attr_col_1]>=weap_req_1:
						x[3]='y'
						x.append(y)
			elif temp_attr[attr_col_2]<weap_req_2:
				##ITEM 2 STILL UNEQUIPABLE, BEGIN SEARCHING FOR 
				##ITEMS IN CHARACTER'S OPEN SLOTS
				equipped=char.equipped
				equip_item_list=[]
				search_item_list=[]
				make_access_combos=False
				for y in range(0,len(equipped)):
					if equipped[y]==0:
						if y==10:
							if equipped[9]!=0:
								equip_item_list.append(9)
							else:
								##BOTH ACCESS SLOTS OPEN
								make_access_combos=True
						elif y>7 or y<6:	#DO NOT ADD WEAPONS TO THIS LIST
							equip_item_list.append(y)
				#search_item_list.append(x[4][0])	#add weapon 1 req to search list
				search_item_list.append(x[5][0])	#add weapon 2 req to search list
				buff_items=search_for_specials(equip_item_list, search_item_list)
				##GENERATE ITEM COMBOS FOR SEARCHED ITEMS
				item_combos=armor_item_combos(buff_items, make_access_combos)
				
				##GET COMBINED BUFFS OF COMBO LIST
				temp_buffs=[]
				for y in item_combos:
					for z in y:
						if z!=0:
							A=find_specials(z, 'armor')
							A=A[0]
							if len(temp_buffs)==0:
								temp_buffs=A
							else:
								for a in range(0,len(A)):
									temp_buffs[a]+=A[a]
					##IF BUFFS ARE ENOUGH TO MEET REQ,
					##ADD COMBO TO X LIST AND CHANGE x[3] TO Y
					if temp_attr[attr_col_2]+temp_buffs[attr_col_2]>=weap_req_2:
						x[3]='y'
						x.append(y)
			else:
				##ITEM IS EQUIPABLE JUST FROM WEAPON BUFFS
				x[3]='y'
		for x in need_buffs_dual:	##ADD NEED BUFF ITEMS BACK TO MAIN LIST
			for y in dual_wield_combos:
				if x[0:3]==y[0:3]:
					y=x
	##CONSOLIDATE SINGE AND DUAL WIELD LISTS INTO ONE
	super_list=[]
	for x in weapon_list:
		if x[3]=='y':
			super_list.append(x)
	for x in dual_wield_combos:
		if x[3]=='y':
			super_list.append(x)
	super_list=sorted(super_list, key=lambda super_list: super_list[2], reverse=True)
	return super_list
					
#
#Find best bow equipment for a character
def max_bow_damage(char):
	##Get all bow weapons
	pierce_weapons=[]
	for a in weapon_headers:
		if weapon_headers[a]=='Type':
			type_col=a
		elif weapon_headers[a]=='Requirements':
			req_col=a
		elif weapon_headers[a]=='Damage':
			dmg_col=a
	for a in unq_ident_weapons:
		if weapons[a][type_col]=='Piercing':
			pierce_weapons.append(a)
	bow_weapons=[]
	for a in pierce_weapons:
		bow_strings=['bow', 'crossbow', 'arbalest']
		for b in bow_strings:
			if bool(re.search(b, weapons[a][0], re.IGNORECASE)):
				if a not in bow_weapons:
					bow_weapons.append(a)
	#add damages
	for a in range(0,len(bow_weapons)):
		bow_weapons[a]=[bow_weapons[a],dmg_hilo(bow_weapons[a], 'physical', 'lo')]
	##check which one need fixes
	for a in range(0,len(bow_weapons)):
		curr_attr=char.attr
		curr_weap=weapons[bow_weapons[a][0]]
		curr_req_lvl=int(curr_weap[req_col][4:len(curr_weap[req_col])])
		curr_req_attr=curr_weap[req_col][0:3]
		for b in attr_headers:
			matched=bool(re.search(curr_req_attr, attr_headers[b], re.IGNORECASE))
			if matched:
				attr_col=b
		if curr_attr[attr_col]<curr_req_lvl:
			bow_weapons[a].append('n')
			bow_weapons[a].append([attr_headers[attr_col],curr_req_lvl,attr_col])
		else:
			bow_weapons[a].append('y')
			bow_weapons[a].append(['none',0,0])
	##Find accesory combos that meet requirements
	for a in range(0,len(bow_weapons)):
		curr_list=bow_weapons[a]
		if curr_list[2]=='n':
			equip_list=[]
			for b in range(0,len(char.equipped)):
				if b!=6 and b!=7:
					if char.equipped[b]==0:
						equip_list.append(b)
			buff_items=search_for_specials(equip_list, [curr_list[3][0]])
			if (9 and 10) in equip_list:
				buff_combos=armor_item_combos(buff_items, True)
			else:
				buff_combos=armor_item_combos(buff_items, False)
			for b in buff_combos:
				total_buffs=[0]*len(attr_headers)
				for c in b:
					i=find_specials(c, 'armor')
					i=i[0]
					for d in range(0,len(i)):
						total_buffs[d]+=i[d]
				if (total_buffs[curr_list[3][2]]+char.attr[curr_list[3][2]])>=curr_list[3][1]:
					bow_weapons[a].append(b)
					bow_weapons[a][2]='y'
	##Return and sort good list
	good_list=[]
	for a in bow_weapons:
		if a[2]=='y':
			good_list.append(a)
	good_list=sorted(good_list, key=lambda good_list: good_list[1], reverse=True)
	return good_list
															
#
#get elemental weapons sets from highest to lowest, specify element type
def max_elem_damage(char, element_type):
	### DEBUG LINE
	'''elem_file=open('element debug.csv', 'w')
	elem_file.write(str(char.attr_raw)+'\n')'''
	###
	##GET ELEMENT COLUMN LOCATIONS
	for x in weapon_headers:
		if weapon_headers[x]=='Element 1':
			elem1=x
			elem1_dmg=x+1
		elif weapon_headers[x]=='Element 2':
			elem2=x
			elem2_dmg=x+1
	##PICK OUT ELEMENTAL WEAPONS FROM WEAPONS TABLE
	elem_weapons=[]
	for x in unq_ident_weapons:
		if weapons[x][elem1]!='N/A' or weapons[x][elem2]!='N/A':
			if weapons[x][elem1]!='N/A':
				i=weapons[x][elem1_dmg]
				if weapons[x][elem2]!='N/A':
					j=weapons[x][elem2_dmg]
				else:
					j=0
			elif weapons[x][elem2]!='N/A':
				j=weapons[x][elem2_dmg]
				if weapons[x][elem1]!='N/A':
					i=weapons[x][elem1_dmg]
				else:
					i=0
			else:
				i=0
				j=0
			k=[x, [weapons[x][elem1], i], [weapons[x][elem2], j]]
			### DEBUG LINE
			#elem_file.write(str(k)+'\n')
			elem_weapons.append(k)
	##GET WEAPONS THAT MATCH ELEMENT CHOSEN
	match_weapons=[]
	for x in elem_weapons:
		element1=x[1][0]
		element2=x[2][0]
		elem1_match=bool(re.search(element_type, element1, re.IGNORECASE))
		elem2_match=bool(re.search(element_type, element2, re.IGNORECASE))
		##STORE MATCHED WEAPONS
		if elem1_match or elem2_match:
			if elem1_match:
				match_weapons.append([x[0], x[1]])
			else:
				match_weapons.append([x[0], x[2]])
	###DEBUG LINE
	'''elem_file.write('Filtered Items.'+'\n')
	for x in match_weapons:		#DELETE LATER
		elem_file.write(str(x)+'\n')'''
	###
	##GET DAMAGE VALUE OF MATCHED WEAPONS
	for x in match_weapons:
		dmg1_lo=re.search('-', x[1][1])
		if bool(dmg1_lo):
			dmg1_lo=x[1][1][0:dmg1_lo.start()]
			dmg1_lo=int(dmg1_lo)
		else:
			dmg1_lo=0
		x[1].append(dmg1_lo)	
	##ADD REQUIREMENTS TO LIST
	for x in match_weapons:
		curr_req=weapons[x[0]][12]
		num_loc=re.search('[0-9]+', curr_req)
		for y in attr_headers:
			if curr_req[0:3]==attr_headers[y][0:3]:
				z=attr_headers[y]
		curr_req=[z, int(curr_req[num_loc.start():len(curr_req)])]
		x.append(curr_req)
	### DEBUG LINE
	'''elem_file.write('Damage and Requirements added.'+'\n')
	for x in match_weapons:		#DELETE LATER
		elem_file.write(str(x)+'\n'''
	###
	##GET DUAL EQUIP SETS
	dual_elem_sets=[]
	single_handed_elem=[]
	#elem_file.write("SINGLE HANDED WEAPONS"+'\n')	###DEBUG LINE
	for a in match_weapons:
		if int(weapons[a[0]][2])==1:
			#elem_file.write(str(a)+'\n')	###DEBUG LINE
			single_handed_elem.append(a)
	##IF MORE THAN 1 ITEM START MAKING COMBOS:
	if len(single_handed_elem)>1:
		#elem_file.write("DUAL COMBOS"+'\n')	###DEBUG LINE
		i=0
		for a in range(0,len(single_handed_elem)):
			i+=1
			temp_holder=[]
			x=single_handed_elem[a]
			for b in range(i,len(single_handed_elem)):
				y=single_handed_elem[b]
				for c in [1]:
					dual_dam_elem=int(x[1][2]+y[1][2])
					dual_wield_abil=char.abil[3]
					if dual_wield_abil==0:
						dual_dam_elem*=.7
						dual_dam_elem=round(dual_dam_elem,3)
					elif dual_wield_abil==1 or dual_wield_abil==2:
						dual_dam_elem*=.8
						dual_dam_elem=round(dual_dam_elem,3)
					elif dual_wield_combos==3:
						dual_dam_elem*=.9
						dual_dam_elem=round(dual_dam_elem,3)
					elif dual_wield_combos==4 or dual_wield_combos==5:
						dual_dam_elem*=1
						dual_dam_elem=round(dual_dam_elem,3)
					elif dual_wield_combos==6:
						dual_dam_elem*=1.05
						dual_dam_elem=round(dual_dam_elem,3)
				if x[2][0]==y[2][0]:
					if x[2][1]>y[2][1]:
						req_lvl=x[2][1]
					else:
						req_lvl=y[2][1]
					temp_holder=[[x[0],y[0]],[x[1][0],x[1][1],y[1][1],dual_dam_elem],[x[2][0],req_lvl]]
				else:
					temp_holder=[[x[0],y[0]],[x[1][0],x[1][1],y[1][1],dual_dam_elem],x[2],y[2]]
				dual_elem_sets.append(temp_holder)
				### DEBUG LINE
				#elem_file.write(str(temp_holder)+'\n')
	print("Number of Dual Wield Combos: "+str(len(dual_elem_sets)))
	print("Would you like to add dual wielding to solutions?")
	if 'y'==yes_or_no():
		for a in dual_elem_sets:
			match_weapons.append(a)		
	##CHECK WHICH ITEMS ARE EQUIPABLE
	###DEBUG LINE
	#elem_file.write("MARKED FOR EQUIP"+'\n')
	###
	equip_fixes=[]
	for x in match_weapons:
		curr_attr=char.attr
		##GO THROUGH REQS COLUMNS AND FIND IF WEAPONS NEED BUFFS
		for a in range(2,len(x)):
			attr_req=x[a][1]
			for y in attr_headers:
				if x[a][0]==attr_headers[y]:
					i=y
			if attr_req>int(curr_attr[i]):
				if type(x[len(x)-1])!=str:
					x.append('n')
					equip_fixes.append(x)
			elif a==len(x)-1:
				if type(x[len(x)-1])!=str:
					x.append('y')
		#elem_file.write(str(x)+'\n')	###DEBUG LINE
	##FIND ITEMS TO MAKE UNEQUIPABLE ITEMS WORK, IF ANY
	if len(equip_fixes)>0:
		curr_attr=char.attr
		equipped=char.equipped
		make_access_combos=False
		equip_item_list=[]
		##GET OPEN EQUIPMENT SLOTS OF CHAR
		for x in range(0,len(equipped)):
			if equipped[x]==0:
				if x==10:
					if equipped[9]!=0:
						equip_item_list.append(9)
					else:
						##BOTH ACCESS SLOTS OPEN
						make_access_combos=True
				elif x!=6:	#DO NOT ADD WEAPON SLOT TO THIS LIST
					equip_item_list.append(x)
		for x in equip_fixes:
			#Find weapons with buff of item requirement, store set requirements
			set_req=[0]*len(char.attr)
			if len(x)==5:
				search_str=[x[2][0],x[3][0]]
				for a in attr_headers:
					if attr_headers[a]==x[2][0]:
						set_req[a]=x[2][1]
					elif attr_headers[a]==x[3][0]:
						set_req[a]=x[3][1]
			else:
				search_str=[x[2][0]]
				for a in attr_headers:
					if attr_headers[a]==search_str[0]:
						set_req[a]=x[2][1]
			buff_items=search_for_specials(equip_item_list, search_str)
			##GET ALL POSSIBLE ITEM COMBOS
			item_combos=armor_item_combos(buff_items, make_access_combos)
			### DEBUG LINE
			'''if type(x[0])==int:
				elem_file.write(str(x[0])+' '+weapons[x[0]][0]+' Item Combos and their buffs'+'\n')
			else:
				elem_file.write(str(x[0])+' '+weapons[x[0][0]][0]+' '+weapons[x[0][1]][0]+' Item Combos and their buffs'+'\n')'''
			##GET COMBINED BUFFS OF COMBO LIST
			temp_buffs=[]
			for y in item_combos:
				for z in y:
					if z!=0:
						A=find_specials(z, 'armor')
						A=A[0]
						if len(temp_buffs)==0:
							temp_buffs=A
						else:
							for a in range(0,len(A)):
								temp_buffs[a]+=A[a]
				###DEBUG LINE
				#elem_file.write(str(y)+','+str(temp_buffs)+','+str(set_req)+'\n')
				###
				for z in range(0,len(temp_buffs)):
					combo_works=True
					if z>1:
						'''if (temp_buffs[z]+int(curr_attr[z]))<x[2][1]:
							combo_works=False'''
						if temp_buffs[z]+int(curr_attr[z])<set_req[z]:
							combo_works=False
				if combo_works:
					for a in range(0,len(x)):
						if type(x[a])==str:
							x[a]='y'
					x.append(y)
	##FILTER OUT USABLE ITEMS
	###DEBUG LINE
	#elem_file.write("COMPLETE LISTS"+'\n')
	###
	complete_list=[]
	for x in match_weapons:
		###DEBUG LINE
		#elem_file.write(str(x)+'\n')
		###	
		for a in x:
			if type(a)==str:
				if a=='y':
					complete_list.append(x)
	complete_list=sorted(complete_list, key=lambda complete_list: complete_list[1][len(complete_list[1])-1], reverse=True)
	### DEBUG LINE
	'''elem_file.write("SORTED:"+'\n')
	for a in complete_list:
		###DEBUG LINE
		elem_file.write(str(a)+'\n')
		###	
	###DEBUG END
	elem_file.close()'''
	return complete_list
	
#	
#search for equipable items in specified character equipment slots that have special buffs
#that are provided and return in an item list
def search_for_specials(equip_slots_list, specials_list):
	##SEARCH ARMORS/WEAPONS FOR ITEMS IN EQUIP SLOT
	##THAT HAVE BUFFS IN SPECIAL LIST
	item_list=[]
	##GO THROUGH EQUIP SLOTS AND LOOK THROUGH CORRESPONDING ITEMS
	for x in equip_slots_list:
		if x==0:	#HELMETS SLOT
			for y in helmets:
				curr_item=armor[helmets[y]]
				for z in specials_list:
					for a in range(len(curr_item)-4,len(curr_item)):
						match=bool(re.search(z, curr_item[a], re.IGNORECASE))
						if match:	#IF A MATCH ADD TO 'item_list'
							item_list.append(helmets[y])
		if x==1:	#CHEST SLOT
			for y in chest:
				curr_item=armor[chest[y]]
				for z in specials_list:
					for a in range(len(curr_item)-4,len(curr_item)):
						match=bool(re.search(z, curr_item[a], re.IGNORECASE))
						if match:	#IF A MATCH ADD TO 'item_list'
							item_list.append(chest[y])
		if x==2:	#UNDERGARMENT SLOT
			for y in undergar:
				curr_item=armor[undergar[y]]
				for z in specials_list:
					for a in range(len(curr_item)-4,len(curr_item)):
						match=bool(re.search(z, curr_item[a], re.IGNORECASE))
						if match:	#IF A MATCH ADD TO 'item_list'
							item_list.append(undergar[y])
		if x==3:	#WAIST SLOT
			for y in waist:
				curr_item=armor[waist[y]]
				for z in specials_list:
					for a in range(len(curr_item)-4,len(curr_item)):
						match=bool(re.search(z, curr_item[a], re.IGNORECASE))
						if match:	#IF A MATCH ADD TO 'item_list'
							item_list.append(waist[y])
		if x==4:	#BOOTS SLOT
			for y in boots:
				curr_item=armor[boots[y]]
				for z in specials_list:
					for a in range(len(curr_item)-4,len(curr_item)):
						match=bool(re.search(z, curr_item[a], re.IGNORECASE))
						if match:	#IF A MATCH ADD TO 'item_list'
							item_list.append(boots[y])
		if x==5:	#GLOVES SLOT
			for y in gloves:
				curr_item=armor[gloves[y]]
				for z in specials_list:
					for a in range(len(curr_item)-4,len(curr_item)):
						match=bool(re.search(z, curr_item[a], re.IGNORECASE))
						if match:	#IF A MATCH ADD TO 'item_list'
							item_list.append(gloves[y])
		if x==6:	#WEAPONS SLOT
			for y in unq_ident_weapons:
				curr_item=weapons[y]
				for z in specials_list:
					for a in range(len(curr_item)-4,len(curr_item)):
						match=bool(re.search(z, curr_item[a], re.IGNORECASE))
						if match:	#IF A MATCH ADD TO 'item_list'
							item_list.append(y)
		if x==7:	#SHIELDS SLOT
			for y in shields:
				curr_item=armor[shields[y]]
				for z in specials_list:
					for a in range(len(curr_item)-4,len(curr_item)):
						match=bool(re.search(z, curr_item[a], re.IGNORECASE))
						if match:	#IF A MATCH ADD TO 'item_list'
							item_list.append(shields[y])
		if x==8:	#AMULETS SLOT
			for y in amulets:
				curr_item=armor[amulets[y]]
				for z in specials_list:
					for a in range(len(curr_item)-4,len(curr_item)):
						match=bool(re.search(z, curr_item[a], re.IGNORECASE))
						if match:	#IF A MATCH ADD TO 'item_list'
							item_list.append(amulets[y])
		if x==9:	#ACESSORIES SLOT
			for y in accessories:
				curr_item=armor[accessories[y]]
				for z in specials_list:
					for a in range(len(curr_item)-4,len(curr_item)):
						match=bool(re.search(z, curr_item[a], re.IGNORECASE))
						if match:	#IF A MATCH ADD TO 'item_list'
							item_list.append(accessories[y])
	return item_list

#
#return list of all items that belong to provided equipment slots
def get_all_equips(equip_slots):
	item_list=[]
	for x in equip_slots:
		if x==0:	#Helmets Slot
			for y in unq_ident_armor:
				if armor[y][1]=='Helmet':
					item_list.append(y)
		elif x==1:	#Chest Slot
			for y in unq_ident_armor:
				if armor[y][1]=='Chest':
					item_list.append(y)
		elif x==2:	#Undergar Slot
			for y in unq_ident_armor:
				if armor[y][1]=='Undergarment':
					item_list.append(y)
		elif x==3:	#Waist Slot
			for y in unq_ident_armor:
				if armor[y][1]=='Waist':
					item_list.append(y)
		elif x==4:	#Boots Slot
			for y in unq_ident_armor:
				if armor[y][1]=='Boots':
					item_list.append(y)
		elif x==5:	#Gloves Slot
			for y in unq_ident_armor:
				if armor[y][1]=='Gloves':
					item_list.append(y)
		elif x==6:	#weapons Slot
			for y in unq_ident_weapons:
				item_list.append(y)
		elif x==7:	#Shields Slot
			for y in unq_ident_armor:
				if armor[y][1]=='Shield':
					item_list.append(y)
		elif x==8:	#Amulets Slot
			for y in unq_ident_armor:
				if armor[y][1]=='Amulet':
					item_list.append(y)
		elif x==9:	#Accessories Slot
			for y in unq_ident_armor:
				if armor[y][1]=='Accessory':
					item_list.append(y)
	return item_list

#
#search for items to equip and/or make builds to maximize search terms							
def special_builds(char):
	##ENTER SEARCH TERM
	no_pick=True
	while no_pick:
		search_term=input("Please enter your search term: ")
		search_items=[]
		##GET ALL ITEMS THAT MATCH SEARCH TERM
		for x in unq_ident_armor:
			i=armor[x]
			match_found=False
			for y in i:
				if bool(re.search(search_term, str(i), re.IGNORECASE)):
					match_found=True
			if match_found:
				search_items.append(x)
		if len(search_items)>0:
			print(str(len(search_items))+' items found with the search term')
			is_abil=False
			is_attr=False
			is_res=False
			make_abil=False
			make_attr=False
			make_res=False
			for x in abil_headers:
				abil_match=bool(re.search(search_term, abil_headers[x], re.IGNORECASE))
				if abil_match:
					is_abil=True
					search_term=abil_headers[x]
			for x in attr_headers:
				attr_match=bool(re.search(search_term, attr_headers[x], re.IGNORECASE))
				if attr_match:
					is_attr=True
					search_term=attr_headers[x]
			for x in resistance_headers:
				res_match=bool(re.search(search_term, resistance_headers[x], re.IGNORECASE))
				if res_match:
					is_res=True
					search_term=resistance_headers[x]
			if is_abil or is_attr or is_res:
				if is_abil:
					print('Ability match found.')
					abil_pick=True
					while abil_pick:
						k=input('Would you like to make builds to maximize ability, (y/n)?'+'\n')
						if k=='y' or k=='n':
							abil_pick=False
							if k=='y':
								make_abil=True
						else:
							print('Invaid entry, please enter only "y" or "n".')
				elif is_attr:
					print('Attribute match found.')
					attr_pick=True
					while attr_pick:
						k=input('Would you like to make builds to maximize attribute, (y/n)?'+'\n')
						if k=='y' or k=='n':
							attr_pick=False
							if k=='y':
								make_attr=True
						else:
							print('Invaid entry, please enter only "y" or "n".')
				elif is_res:
					print('Resistance match found.')
					res_pick=True
					while res_pick:
						k=input('Would you like to make builds to maximize resistance, (y/n)?'+'\n')
						if k=='y' or k=='n':
							res_pick=False
							if k=='y':
								make_res=True
						else:
							print('Invaid entry, please enter only "y" or "n".')
			no_pick=False
		else:
			print('No items found with matching terms. Please try again.')
	#IF MAXIMIZE BUILDS SELECTED BEGIN MAKING COMBOS
	if make_abil or make_attr or make_res:
		if make_attr:
			get_row=0
		elif make_abil:
			get_row=1
		elif make_res:
			get_row=2
		equipped=char.equipped
		make_access_combos=False
		equip_item_list=[]
		for x in range(0,len(equipped)):
			if equipped[x]==0:
				if x==10:
					if equipped[9]!=0:
						equip_item_list.append(9)
					else:
						##BOTH ACCESS SLOTS OPEN
						make_access_combos=True
				elif x!=6:	#DO NOT ADD WEAPON SLOT TO THIS LIST
					equip_item_list.append(x)
		no_pick=True
		while no_pick:
			print("Would you like to start a build from scratch or"
				+" build off "+char.name+"'s open slots?")
			num_pick=True
			while num_pick:
				print("Enter number for selection.")
				build_pick=input("1. Scratch build"+'\n'+"2. Open slots build"+'\n')
				#build_pick=int(build_pick)
				if build_pick=='1' or build_pick=='2':
					num_pick=False
					no_pick=False
				else:
					print("Invalid selection. Please enter '1' or '2' only.")
		if build_pick=='2':
			##REPLACE SEARCH ITEMS
			search_items=search_for_specials(equip_item_list, [search_term])
		else:
			##FOR SRACTCH BUILD, MAKE ACCESSORY COMBOS
			make_access_combos=True
		if len(search_items)>0:
			armor_combos=armor_item_combos(search_items, make_access_combos)
			final_armor_combos=[]
			for x in armor_combos:
				###DELETE LATER
				#print(x)
				###
				total_spc=[]
				for y in x:
					if y!=0:
						itm_spc=find_specials(y, 'armor')
						itm_spc=itm_spc[get_row]
						###DELETE LATER
						#print(armor[y][0])
						###
						if len(total_spc)==0:
							total_spc=itm_spc
						else:
							for z in range(0,len(total_spc)):
								total_spc[z]+=itm_spc[z]
				if make_abil:
					add_str=[]
					for y in abil_headers:
						if total_spc[y]>0:
							add_str.append('+'+str(total_spc[y])+' '+abil_headers[y])
							###DELETE LATER
							#print('+'+str(total_spc[y])+' '+abil_headers[y])
							###
						if abil_headers[y]==search_term:
							x=[x,[total_spc[y]]]
				elif make_attr:
					add_str=[]
					for y in attr_headers:
						if total_spc[y]>0:
							add_str.append('+'+str(total_spc[y])+' '+attr_headers[y])
							###DELETE LATER
							#print('+'+str(total_spc[y])+' '+attr_headers[y])
							###
						if attr_headers[y]==search_term:
							x=[x,[total_spc[y]]]
				elif make_res:
					add_str=[]
					for y in resistance_headers:
						if total_spc[y]>0:
							add_str.append('+'+str(total_spc[y])+' '+resistance_headers[y])
							###DELETE LATER
							#print('+'+str(total_spc[y])+' '+resistance_headers[y])
							###
						if resistance_headers[y]==search_term:
							x=[x,[total_spc[y]]]
				x.append(add_str)
				final_armor_combos.append(x)
				###DELETE LATER
				#print(x)
				#print(''.ljust(25,'-'))
				###DELETE LATER
			return final_armor_combos
		else:
			print("No combinations could be made from your specifications.")
	#NO MAXIMIZE BUILD OPTION, ADD SORT BY SEARCH VALUE IF RES/ATTR/ABIL MATCH
	elif is_abil or is_attr or is_res:
		if is_abil:
			get_row=1
		elif is_attr:
			get_row=0
		elif is_res:
			get_row=2
		for x in search_items:
			#print(armor[x][0])
			add_str=armor[x][0]+' '
			itm_spc=find_specials(x, 'armor')
			itm_spc=itm_spc[get_row]
			if is_abil:
				for y in abil_headers:
					if itm_spc[y]>0:
						add_str+='+'+str(itm_spc[y])+' '
						add_str+=abil_headers[y]+' '
						#print(add_str)
					if search_term==abil_headers[y]:
						x=[x, [itm_spc[y]]]
			elif is_attr:
				for y in attr_headers:
					if itm_spc[y]>0:
						add_str+='+'+str(itm_spc[y])+' '
						add_str+=attr_headers[y]
						#print(add_str)
					if search_term==attr_headers[y]:
						x=[x, [itm_spc[y]]]
			elif is_res:
				for y in resistance_headers:
					if itm_spc[y]>0:
						add_str+='+'+str(itm_spc[y])+' '
						add_str+=resistance_headers[y]
						#print(add_str)
					if search_term==resistance_headers[y]:
						x=[x, [itm_spc[y]]]
			###DELETE LATER
			print(add_str)
			###
		return search_items
	else:
		for x in range(0,len(search_items)):
			###DELETE LATER
			print(str(x+1)+': '+armor[search_items[x]][0])
			###
		return search_items

#
#make equipable item combos from items list
def armor_item_combos(item_list, accs_combos):
	make_access_combos=accs_combos
	buff_items=item_list
	if make_access_combos:	#MAKE ACCESSORY COMBOS
		access_combos=[]
		access_list=[]
		##FILTER OUT ALL ACCESSORIES FROM LIST
		for y in buff_items:
			if armor[y][1]=='Accessory':
				access_list.append(y)
		##IF MORE THAN 1 ACCESSORY, MAKE ALL POSSIBLE COMBOS
		##AND STORE THEM IN ACCESS_COMBOS
		if len(access_list)>1:
			i=1
			for y in range(0,len(access_list)):
				for z in range(i,len(access_list)):
					access_combos.append([access_list[y],access_list[z]])
				i+=1
		elif len(access_list)==0:
			access_list.append(0)
	else:
		access_combos=[]
		access_list=[]
		for y in buff_items:
			if armor[y][1]=='Accessory':
				access_list.append(y)
		if len(access_list)==0:
			access_list.append(0)
	##GENERATE ALL POSSIBLE ITEM COMBOS FROM 'buff_items'
	#SPLIT ITEMS INTO CATERGORIES
	buff_helmets=[]	#HELMETS
	for y in buff_items:
		if armor[y][1]=='Helmet':
			buff_helmets.append(y)
	if len(buff_helmets)==0:
		buff_helmets.append(0)	#add a 0 if no items
		
	buff_chest=[]	#CHEST PIECES
	for y in buff_items:
		if armor[y][1]=='Chest':
			buff_chest.append(y)
	if len(buff_chest)==0:
		buff_chest.append(0)
		
	buff_under=[]	#UNDERGARMENTS
	for y in buff_items:
		if armor[y][1]=='Undergarment':
			buff_under.append(y)
	if len(buff_under)==0:
		buff_under.append(0)
		
	buff_waist=[]	#WAIST PIECES
	for y in buff_items:
		if armor[y][1]=='Waist':
			buff_waist.append(y)
	if len(buff_waist)==0:
		buff_waist.append(0)
		
	buff_boots=[]	#BOOTS
	for y in buff_items:
		if armor[y][1]=='Boots':
			buff_boots.append(y)
	if len(buff_boots)==0:
		buff_boots.append(0)
		
	buff_gloves=[]	#GLOVES
	for y in buff_items:
		if armor[y][1]=='Gloves':
			buff_gloves.append(y)
	if len(buff_gloves)==0:
		buff_gloves.append(0)
		
	buff_shields=[]	#SHIELDS
	for y in buff_items:
		if armor[y][1]=='Shield':
			buff_shields.append(y)
	if len(buff_shields)==0:
		buff_shields.append(0)
		
	buff_amulets=[]	#AMULETS
	for y in buff_items:
		if armor[y][1]=='Amulet':
			buff_amulets.append(y)
	if len(buff_amulets)==0:
		buff_amulets.append(0)
	##BEGIN GENERATING COMBOS
	item_combos=[]
	for a in buff_helmets:
		for b in buff_chest:
			for c in buff_under:
				for d in buff_waist:
					for e in buff_boots:
						for f in buff_gloves:
							for g in buff_shields:
								for h in buff_amulets:
									if len(access_combos)>0:
										for i in access_combos:
											cmb=[a,b,c,d,e,f,g,h,i[0],i[1]]
											item_combos.append(cmb)
									else:
										for i in access_list:
											cmb=[a,b,c,d,e,f,g,h,i]
											item_combos.append(cmb)
	return item_combos

#
#user interface
def interface():
	print("Welcome to the Divinity Original Sin Database Manager.")
	print("The following characters were loaded:")
	print_players()
	print("Please choose an action.")
	print("1. Armor Build \n2. Maximize Damage \n3. View Inventory \n4. Search Inventory \n5. Clear Equipment \n"+
		"6. Save/Load equipment \n7. End Program")
	##GET ACTION CHOICE
	action_choice=number_select(7)
	##ACTIONS
	if action_choice==1:	#Armor Builds
		##SELECT A CHARACTER
		print("Select which character you would like to build the armor for.")
		for x in range(0,len(attributes)):
			if x!=0:
				print(str(x)+": "+attributes[x][0])
		char_num=number_select(len(attributes)-1)
		for x in char_list:
			if char_num==x:
				char_choice=char_list[x]
		print(char_choice.name+" was selected.")
		##ASK WHAT KIND OF ARMOR BUILD
		print("What kind of armor build?")
		print("1. Max Armour Rating \n"+"2. Maximize a special ability")
		armor_choice=number_select(2)
		##MAX ARMOR BUILD CHOSEN
		if armor_choice==1:		#Max armor rating
			print("Choose an option below:")
			print("1: MAX POSSIBLE (This will return the best possible combinations from the entire database.)")
			print("2: MAX FROM OPEN SLOTS (This will return armor sets that maximize armour rating from the character's open equipment slots.)")
			print("3: MAX WITHOUT ACCESSORIES, FASTEST (This will build sets from items that can be equipped from character's unaltered attributes.)")
			armor_flavor=number_select(3)
			if armor_flavor==1:
				print('Choose an option below:')
				print('1: Auto equip best set without conflict')
				print('2: View and select from set descriptions/values')
				if number_select(2)==1:
					char_armors=armor_max_def(char_choice)
					if len(char_armors)!=0:
						equip_armors(char_armors, 2, char_choice)
				else:
					print("Would you like to filter out conflict sets?")
					if 'y'==yes_or_no():
						char_armors=armor_max_def(char_choice)
						new_armors=remove_armor_conflicts(char_armors, 2)
						print("New number of combinations is: "+str(len(new_armors)))
						set_choice=select_armor_sets(new_armors, 2)
						if set_choice is not None:
							print(set_choice)
							set_choice=armor_equip_order(set_choice, char_choice)
							print(set_choice)
							for a in set_choice:
								char_choice.equipit(True, a)
						else:
							print("Nothing selected")
					else:
						char_armors=armor_max_def(char_choice)
						set_choice=select_armor_sets(char_armors, 2)
						if set_choice is not None:
							print(set_choice)
							set_choice=armor_equip_order(set_choice, char_choice)
							print(set_choice)
							for a in set_choice:
								char_choice.equipit(True, a)
						else:
							print("Nothing selected")
			elif armor_flavor==2:
				print('Choose an option below:')
				print('1: Auto equip best set without conflict')
				print('2: View and select from set descriptions/values')
				if number_select(2)==1:
					char_armors=armor_max_open(char_choice)
					if len(char_armors)!=0:
						equip_armors(char_armors, 2, char_choice)
				else:
					print("Would you like to filter out conflict sets?")
					if 'y'==yes_or_no():
						char_armors=armor_max_open(char_choice)
						new_armors=remove_armor_conflicts(char_armors, 2)
						print("New number of combinations is: "+str(len(new_armors)))
						set_choice=select_armor_sets(new_armors, 2)
						if set_choice is not None:
							print(set_choice)
							set_choice=armor_equip_order(set_choice, char_choice)
							print(set_choice)
							for a in set_choice:
								char_choice.equipit(True, a)
						else:
							print("Nothing selected")
					else:
						char_armors=armor_max_def(char_choice)
						set_choice=select_armor_sets(char_armors, 2)
						if set_choice is not None:
							print(set_choice)
							set_choice=armor_equip_order(set_choice, char_choice)
							print(set_choice)
							for a in set_choice:
								char_choice.equipit(True, a)
						else:
							print("Nothing selected")
			elif armor_flavor==3:
				print('Choose an option below:')
				print('1: Auto equip best set without conflict')
				print('2: View and select from set descriptions/values')
				if number_select(2)==1:
					char_armors=armor_max_filtered(char_choice)
					if len(char_armors)!=0:
						equip_armors(char_armors, 2, char_choice)
				else:
					print("Would you like to filter out conflict sets?")
					if 'y'==yes_or_no():
						char_armors=armor_max_filtered(char_choice)
						new_armors=remove_armor_conflicts(char_armors, 2)
						print("New number of combinations is: "+str(len(new_armors)))
						set_choice=select_armor_sets(new_armors, 2)
						if set_choice is not None:
							print(set_choice)
							set_choice=armor_equip_order(set_choice, char_choice)
							print(set_choice)
							for a in set_choice:
								char_choice.equipit(True, a)
						else:
							print("Nothing selected")
					else:
						char_armors=armor_max_def(char_choice)
						set_choice=select_armor_sets(char_armors, 2)
						if set_choice is not None:
							print(set_choice)
							set_choice=armor_equip_order(set_choice, char_choice)
							print(set_choice)
							for a in set_choice:
								char_choice.equipit(True, a)
						else:
							print("Nothing selected")
		elif armor_choice==2:	#Armor builds from searched terms
			char_armors=special_builds(char_choice)
			if char_armors is not None:
				'''for x in range(0,len(char_armors)):
					if type(char_armors[x][0])!=list:
						char_armors[x]=[char_armors[x]]'''
				for x in char_armors:
					print(x)
				print("Equip sets listed?")
				if 'y'==yes_or_no():
					#equip_armors(char_armors, 99, char_choice)
					set_choice=select_armor_sets(char_armors, 99)
					if set_choice is not None:
						print(set_choice)
						set_choice=armor_equip_order(set_choice, char_choice)
						print(set_choice)
						for a in set_choice:
							char_choice.equipit(True, a)
					else:
						print("Nothing selected")
			else:
				print("No items met your requirements.")
	elif action_choice==2:	#Weapon Builds
		##SELECT A CHARACTER
		print("Select which character you would like to build the armor for.")
		for x in range(0,len(attributes)):
			if x!=0:
				print(str(x)+": "+attributes[x][0])
		char_num=number_select(len(attributes)-1)
		for x in char_list:
			if char_num==x:
				char_choice=char_list[x]
		print(char_choice.name+" was selected.")
		##ASK WHAT KIND OF DAMAGE TO MAXIMIZE
		print("What type of damage would you like to maximize?")
		print("1. Physical Damage (i.e. Slashing, Crushing, etc.) \n"+
			"2. Elemental Damage (i.e. Fire, Poison, Air, etc.)")
		damage_choice=number_select(2)
		if damage_choice==1:	#MAXAMIZE PHYSICAL DAMAGE
			print("What type of physical damage would you like?")
			print("1. Crushing \n2. Slashing \n3. Piercing")
			phys_dam_types={1: 'Crushing', 2: 'Slashing', 3: 'Piercing'}
			phys_choice=phys_dam_types[number_select(3)]
			if phys_choice=='Piercing':
				print('Pick from the following Piercing damage:')
				print('1. Just bows \n2. Exclude bows \n3. Both')
				pierce_choice=number_select(3)
				if pierce_choice==1:
					physical_weapons=max_bow_damage(char_choice)
					print("Remove Crossbows?")
					if 'y'==yes_or_no():
						bow_weapons=[]
						for a in physical_weapons:
							weap_name=weapons[a[0]][0]
							is_crossbow=bool(re.search('crossbow', weap_name, re.IGNORECASE))
							is_arbalest=bool(re.search('arbalest', weap_name, re.IGNORECASE))
							if is_crossbow==False and is_arbalest==False:
								bow_weapons.append(a)
						equip_max_weapons(bow_weapons, 'Physical', char_choice)
					else:
						equip_max_weapons(physical_weapons, 'Physical', char_choice)
				elif pierce_choice==2:	##REMOVE ALL BOWS
					physical_weapons=max_phys_damage(char_choice, phys_choice)
					new_weapons=[]
					for a in physical_weapons:
						if type(a[0])==int:
							bow_strings=['bow', 'arbalest']
							is_bow=False
							for b in bow_strings:
								if bool(re.search(b, weapons[a[0]][0], re.IGNORECASE)):
									is_bow=True
							if not is_bow:
								new_weapons.append(a)
						else:
							new_weapons.append(a)
					print('Choose an option below:')
					print('1. Include single and dual wield \n2. Only single weapons \n3. Only dual wields')
					include_choice=number_select(3)
					if include_choice==1:
						equip_max_weapons(new_weapons, 'Physical', char_choice)
					elif include_choice==2:
						single_weapons=[]
						for a in new_weapons:
							if type(a[0])==int:
								single_weapons.append(a)
						equip_max_weapons(single_weapons, 'Physical', char_choice)
					elif include_choice==3:
						dual_wields=[]
						for a in new_weapons:
							if type(a[0])!=int:
								dual_wields.append(a)
						equip_max_weapons(dual_wields, 'Physical', char_choice)
				elif pierce_choice==3:
					physical_weapons=max_phys_damage(char_choice, phys_choice)
					print('Choose an option below:')
					print('1. Include single and dual wield \n2. Only single weapons \n3. Only dual wields')
					include_choice=number_select(3)
					if include_choice==1:
						equip_max_weapons(physical_weapons, 'Physical', char_choice)
					elif include_choice==2:
						single_weapons=[]
						for a in physical_weapons:
							if type(a[0])==int:
								single_weapons.append(a)
						equip_max_weapons(single_weapons, 'Physical', char_choice)
					elif include_choice==3:
						dual_wields=[]
						for a in physical_weapons:
							if type(a[0])!=int:
								dual_wields.append(a)
						equip_max_weapons(dual_wields, 'Physical', char_choice)
			else:
				physical_weapons=max_phys_damage(char_choice, phys_choice)
				print('Choose an option below:')
				print('1. Include single and dual wield \n2. Only single weapons \n3. Only dual wields')
				include_choice=number_select(3)
				if include_choice==1:
					equip_max_weapons(physical_weapons, 'Physical', char_choice)
				elif include_choice==2:
					single_weapons=[]
					for a in physical_weapons:
						if type(a[0])==int:
							single_weapons.append(a)
					equip_max_weapons(single_weapons, 'Physical', char_choice)
				elif include_choice==3:
					dual_wields=[]
					for a in physical_weapons:
						if type(a[0])!=int:
							dual_wields.append(a)
							print(a)
					equip_max_weapons(dual_wields, 'Physical', char_choice)
		elif damage_choice==2:	#MAX ELEMENTAL DAMAGE
			print("What type of Elemental damage would you like?")
			print("1. Fire \n2. Water \n3. Earth \n4. Air \n5. Tenebrium \n6. Poison")
			elem_dam_types={1: 'Fire', 2: 'Water', 3: 'Earth', 4: 'Air', 5: 'Tenebrium',
				6: 'Poison'}
			elem_choice=elem_dam_types[number_select(6)]
			elemental_weapons=max_elem_damage(char_choice, elem_choice)
			equip_max_weapons(elemental_weapons, 'elemental', char_choice)		
	elif action_choice==3:	#View Items in Inventory
		print("Please choose an action:")
		print("1. View items in use \n2. View Characters equipment details \n3. View Database")
		view_choice=number_select(3)
		if view_choice==1:
			for x in [used_items.armors, used_items.weapons]:
				if x==used_items.armors:
					print("Armors")
					print(''.ljust(len('Armors'),'-'))
					for y in x:
						print(armor[y])
				else:
					print("Weapons")
					print(''.ljust(len('Weapons'),'-'))
					for y in x:
						print(weapons[y])
		elif view_choice==2:
			print("Pick a character:")
			for x in char_list:
				add_str=str(x)+": "
				add_str+=char_list[x].name
				print(add_str)
			char_choice=char_list[number_select(len(char_list))]
			print(char_choice.name)
			for x in range(0,len(char_choice.equipped)):
				curr_item=char_choice.equipped[x]
				if x!=6 and x!=7:
					if curr_item!=0:
						print(armor[curr_item])
				else:
					if x==6 and curr_item==char_choice.equipped[7] and curr_item!=0:
						print(weapons[curr_item])
					elif x==6 and curr_item!=0:
						print(weapons[curr_item])
					elif x==7 and curr_item!=0:
						if char_choice.has_shield:
							print(armor[curr_item])
						else:
							print(weapons[curr_item])
		elif view_choice==3:
			'''print("Please choose an action:")
			print("1. Armors \n2. Weapons ")
			if number_select(2)==1:
				q=sorting_order(True, 1)
				view_inventory(True, q)
			else:
				view_inventory(False, unq_ident_weapons)'''
			view_database_interface()
	elif action_choice==4:	#Search Items
		print("Enter database to search.")
		print("1. Weapons \n2. Armors")
		database_choice=number_select(2)
		if database_choice==1:
			search_term=input("Enter your search term: ")
			search_list=[]
			for x in unq_ident_weapons:
				any_found=False
				for y in weapons[x]:
					if bool(re.search(search_term, y, re.IGNORECASE)) and not any_found:
						any_found=True
						search_list.append(x)
			if search_list is not None:
				count=1
				for x in search_list:
					add_str=str(count)+': '
					for y in weapons[x]:
						add_str+=str(y)+' |'
					print(add_str)
					count+=1
				print("Would you like to equip one of these items?")
				if 'y'==yes_or_no():
					#Pick a character
					print("Select which character you would like to build the armor for.")
					for x in range(0,len(attributes)):
						if x!=0:
							print(str(x)+": "+attributes[x][0])
					char_num=number_select(len(attributes)-1)
					for x in char_list:
						if char_num==x:
							char_choice=char_list[x]
					print(char_choice.name+" was selected.")
					#Filter items for character
					new_items=filter_weapon_req(search_list, char_choice)
					if new_items is not None:
						print("Enter the number next to the item you would like to equip.")
						item_choice=number_select(len(search_list))-1
						if search_list[item_choice] in new_items:
							for x in new_items:
								if x==search_list[item_choice]:
									equip_max_weapons([[x]], 'phys', char_choice)
						else:
							print("Item requirements not met by selected character.")
					else:
						print("None of the searched items can be equipped by the selected character.")
			else:
				print("No matches were found.")
		elif database_choice==2:
			search_term=input("Enter your search term: ")
			search_list=[]
			for x in unq_ident_armor:
				any_found=False
				for y in armor[x]:
					if bool(re.search(search_term, y, re.IGNORECASE)) and not any_found:
						any_found=True
						search_list.append(x)
			if search_list is not None:
				count=1
				for x in search_list:
					add_str=str(count)+': '
					for y in armor[x]:
						add_str+=str(y)+' |'
					print(add_str)
					count+=1
				print("Would you like to equip one of these items?")
				if 'y'==yes_or_no():
					#Pick a character
					print("Select which character you would like to build the armor for.")
					for x in range(0,len(attributes)):
						if x!=0:
							print(str(x)+": "+attributes[x][0])
					char_num=number_select(len(attributes)-1)
					for x in char_list:
						if char_num==x:
							char_choice=char_list[x]
					print(char_choice.name+" was selected.")
					#Filter items for character
					new_items=filter_armor_req(search_list, char_choice)
					if new_items is not None:
						print("Enter the number next to the item you would like to equip.")
						item_choice=number_select(len(search_list))-1
						if search_list[item_choice] in new_items:
							for x in new_items:
								if x==search_list[item_choice]:
									equip_armors([[x]], 2, char_choice)
						else:
							print("Item requirements not met by selected character.")
					else:
						print("None of the searched items can be equipped by the selected character.")
	elif action_choice==5:	#Clear equipment
		print("Select a character's equipment to clear.")
		for a in char_list:
			i=char_list[a]
			print(str(a)+': '+i.name)
		print("5: NONE")
		char_choice=number_select(len(char_list)+1)
		if char_choice<=len(char_list):
			char_choice=char_list[char_choice]
			for a in range(0,len(char_choice.equipped)):
				b=char_choice.equipped[a]
				if b!=0:
					char_choice.unequip(b, a)
	elif action_choice==6:	#save/load equipment
		save_found=False
		save_files={}
		save_count=1
		for a in os.listdir(curdir):
			if bool(re.search('.sav', a)):
				save_files[save_count]=abspath(curdir)+'\\'+a
				save_found=True
				save_count+=1
		if save_found:
			print("Save file(s) found.")
		print("Choose an option below. \n"+"1. Save \n"+"2. Load \n")
		if number_select(2)==1:
			save_files[len(save_files)+1]='New Save'
			print("Please select a file to save to.")
			for a in save_files:
				print(str(a)+': '+str(save_files[a]))
			file_choice=save_files[number_select(len(save_files))]
			if file_choice=='New Save':
				file_choice=input("Please enter the new file save name: ")+'.sav'
				file_choice=abspath(curdir)+'\\'+file_choice
			equip_file=open(file_choice, 'w')
			for a in char_list:
				i=char_list[a]
				store_string=i.name
				for b in i.equipped:
					store_string+=','+str(b)
				if i.has_shield:
					store_string+=','+'shield'
				else:
					store_string+=','+'none'
				equip_file.write(store_string+'\n')
			equip_file.close()
		else:
			print("Please select a file to load from.")
			for a in save_files:
				print(str(a)+': '+str(save_files[a]))
			file_choice=save_files[number_select(len(save_files))]
			equip_file=open(file_choice, 'r')
			equip_lines=csv.reader(equip_file)
			loaded_equipment=list(equip_lines)
			equip_file.close()
			for a in char_list:
				char_list[a].clear_equipment()
			if len(loaded_equipment)>0:
				for a in char_list:
					i=char_list[a]
					if loaded_equipment[a-1][0]==i.name:
						armor_set=[]
						weapon_set=[]
						for b in range(1,len(loaded_equipment[a-1])-1):
							equip_slot=b-1
							j=int(loaded_equipment[a-1][b])
							if equip_slot!=6 and equip_slot!=7:
									armor_set.append(j)
							else:
								if loaded_equipment[a-1][7]==loaded_equipment[a-1][8] and int(loaded_equipment[a-1][7])!=0:
									if int(loaded_equipment[a-1][7]) not in weapon_set:
										weapon_set.append(int(loaded_equipment[a-1][7]))
								elif equip_slot==7 and loaded_equipment[a-1][len(loaded_equipment[a-1])-1]=='shield':
									armor_set.append(j)
								elif equip_slot==7:
									weapon_set.append(j)
								elif equip_slot==6:
									weapon_set.append(j)
						armor_set=armor_equip_order(armor_set,i)
						for c in armor_set:
							i.equipit(True, c)
						for c in weapon_set:
							i.equipit(False, c)
				print("End of file.")
			else:
				print("File was empty.")
	elif action_choice==7:	#END PROGRAM
		print("Are you sure you want to end the program?")
		if 'y'==yes_or_no():
			return False	
	input("Press ENTER to continue.")
	return True			
	
#
#print formatted view of armor list and return a choice
def select_armor_sets(combos, combo_start):
	if len(combos)!=0:
		if len(combos)<3:
			print_end=len(combos)
		else:
			print_end=3
		print_start=0
		total_combo_items=[]
		set_chosen=False
		set_count=1
		while not set_chosen:
			if print_end>=len(combos):
				set_chosen=True
			for a in range(print_start, print_end):
				curr_set=combos[a]
				if type(curr_set[0])!=list:
					main_set=[curr_set[0]]
				else:
					main_set=curr_set[0]
				if len(curr_set)>combo_start:	#SET HAD ACCESORY COMBOS
					for b in range(combo_start, len(curr_set)):
						total_specials=[]
						appended_set=main_set+curr_set[b]
						for c in appended_set:
							i=find_specials(c, 'armor')
							if len(total_specials)==0:
								total_specials=i
							else:
								##ADD TO TOTAL SPECIAL VALUES
								for d in range(0,len(i)):
									for e in range(0,len(i[d])):
										total_specials[d][e]+=i[d][e]
						print(str(set_count)+':')
						print_set(appended_set, total_specials)
						total_combo_items.append(appended_set)
						set_count+=1
				else:
					total_specials=[]
					for c in main_set:
						i=find_specials(c, 'armor')
						if len(total_specials)==0:
							total_specials=i
						else:
							##ADD TO TOTAL SPECIAL VALUES
							for d in range(0,len(i)):
								for e in range(0,len(i[d])):
									total_specials[d][e]+=i[d][e]
					print(str(set_count)+':')
					print_set(main_set, total_specials)
					total_combo_items.append(main_set)
					set_count+=1
			print("Would you like to equip one of the above sets?")
			if 'y'==yes_or_no():
				print("Enter the armor set you want to equip.")
				set_picked=number_select(set_count-1)
				set_chosen=True
				return total_combo_items[set_picked-1]
			else:
				if (print_start+3)<=(len(combos)-3):
					print_start+=3
				else:
					print_start=len(combos)-3
				if (print_end+3)<=len(combos):
					print_end+=3
				else:
					print_end=len(combos)
	else:
		print("There are no combinations to choose from!")
				
#					
#print armor sets provided in formatted style
def print_set(combo, special_buffs):
	long_str=len('Armour Rating: 999.9')
	column_spaces=[0]*3
	##CHECK FOR C0NFLICTS
	conflicts=[]
	for a in combo:
		if a in used_items.armors:
			already_there=False
			for b in char_list:
				for c in char_list[b].equipped:
					if a==c:
						for d in conflicts:
							if char_list[b].name==d:
								already_there=True
						if not already_there:
							conflicts.append(char_list[b].name)
	for a in combo:
		if (len(armor[a][0])+len(equipment_headers[10])+2)>long_str:
			long_str=(len(armor[a][0])+len(equipment_headers[10])+2)
	column_spaces[0]=long_str
	long_str=0
	for a in attr_headers:
		if (len(attr_headers[a])+4)>long_str:
			long_str=len(attr_headers[a])+4
	for a in resistance_headers:
		if (len(resistance_headers[a])+6)>long_str:
			long_str=len(resistance_headers[a])+6
	column_spaces[1]=long_str
	#SORT ARMOR ITEMS
	armor_order=[0]*len(equipment_headers)
	for a in combo:
		if armor[a][1]=='Helmet':
			armor_order[0]=a
		elif armor[a][1]=='Chest':
			armor_order[1]=a
		elif armor[a][1]=='Undergarment':
			armor_order[2]=a
		elif armor[a][1]=='Waist':
			armor_order[3]=a
		elif armor[a][1]=='Boots':
			armor_order[4]=a
		elif armor[a][1]=='Gloves':
			armor_order[5]=a
		elif armor[a][1]=='Shield':
			armor_order[7]=a
		elif armor[a][1]=='Amulet':
			armor_order[8]=a
		elif armor[a][1]=='Accessory':
			if armor_order[9]==0:
				armor_order[9]=a
			else:
				armor_order[10]=a
	##Start printing rows
	row_count=0
	##GO THROUGH FIRST 6 ROWS
	for a in range(2,len(attr_headers)):
		if armor_order[row_count]==0:
			row_str=(equipment_headers[row_count]+': '+'').ljust(column_spaces[0],' ')
		else:
			row_str=(equipment_headers[row_count]+': '+armor[armor_order[row_count]][0]).ljust(column_spaces[0],' ')
		row_str+='|'
		row_str+=(attr_headers[a]+' '+str(special_buffs[0][a])).ljust(column_spaces[1],' ')
		row_str+='|'
		row_str+=(abil_headers[row_count]+' '+str(special_buffs[1][row_count]))
		print(row_str)
		row_count+=1
	##NEXT 5 ROWS, FINISH EQUIPMENT
	for a in range(0,5):
		if armor_order[row_count]==0:
			row_str=(equipment_headers[row_count]+': '+'').ljust(column_spaces[0],' ')
		else:
			row_str=(equipment_headers[row_count]+': '+armor[armor_order[row_count]][0]).ljust(column_spaces[0],' ')
		row_str+='|'
		row_str+=(resistance_headers[a]+' '+str(special_buffs[2][a])).ljust(column_spaces[1],' ')
		row_str+='|'
		row_str+=(abil_headers[row_count]+' '+str(special_buffs[1][row_count]))
		print(row_str)
		row_count+=1
	##LAST RESISTANCE ROW
	for a in [5]:
		##GET TOTAL ARMOUR RATING
		total_rating=0
		for b in armor_order:
			if armor[b][2]!='N/A' and b!=0:
				total_rating+=int(armor[b][2])
		row_str=('Armour Rating: '+str(total_rating)).ljust(column_spaces[0],' ')
		row_str+='|'
		row_str+=(resistance_headers[a]+' '+str(special_buffs[2][a])).ljust(column_spaces[1],' ')
		row_str+='|'
		row_str+=(abil_headers[row_count]+' '+str(special_buffs[1][row_count]))
		print(row_str)
		row_count+=1
	##TILL THE END OF THE ABILITIES, INCLUDE CONFLICTS
	conflict_count=0
	end_of_conflicts=False
	for a in range(row_count,len(abil_headers)):
		if len(conflicts)!=0 and end_of_conflicts==False:
			if conflict_count==0:
				row_str='Conflicts: '.ljust(column_spaces[0],' ')
				conflict_count+=1
			elif conflict_count<=len(conflicts):
				row_str=conflicts[conflict_count-1].ljust(column_spaces[0],' ')
				conflict_count+=1
				if conflict_count>len(conflicts):
					end_of_conflicts=True
		else:
			row_str=''.ljust(column_spaces[0],' ')
		row_str+='|'
		row_str+=(''.ljust(column_spaces[1],' '))
		row_str+='|'
		row_str+=(abil_headers[row_count]+' '+str(special_buffs[1][row_count]))
		print(row_str)
		row_count+=1
	
#
#remove all sets that have equipment already in use, return good sets
def remove_armor_conflicts(combos, combo_start):
	good_combos=[]
	for a in combos:	
		temp_holder=[]
		first_part_good=True
		if type(a[0])==list:
			for b in a[0]:
				if b in used_items.armors:
					first_part_good=False
		else:
			if a[0] in used_items.armors:
				first_part_good=False
		if first_part_good:
			temp_holder=a[0:combo_start]
		if len(a)>combo_start:
			for b in range(combo_start,len(a)):
				second_part_good=True
				for c in a[b]:
					if c in used_items.armors:
						second_part_good=False
				if second_part_good:
					temp_holder.append(a[b])
			if len(temp_holder)>combo_start:
				good_combos.append(temp_holder)
		else:
			if len(temp_holder)>0:
				good_combos.append(temp_holder)
	return good_combos
									
#
# Function to equip armors				
def equip_armors(armor_items, combo_start, char):
	occupied_armors=[]
	occupied_char_armors=[]
	occupied_char_accs=[]
	good_combos={}
	##GO THROUGH COMBOS AND LOOK AND CONFLICTS
	for a in range(0,len(armor_items)):
		good_combos[a]=[]	#Set default good combos to empty list
		x=armor_items[a]
		armor_in_use=False	#Var to set if armor set is in conflict
		good_accessories=False	#Var to mark if any single accessory combo is not in conflict
		if type(x[0])==list:	#Armor set, should be most of the armor items sets
			armors_name_holder=[]
			accs_name_holder=[]
			#check all items in armor set for conflicts
			for b in x[0]:
				if b in used_items.armors:
					#print('Conflict Found')
					armor_in_use=True
					##Search for character with item in use
					for c in char_list:
						for d in char_list[c].equipped:
							if b==d:
								#check if character has been flagged for a previous conflict
								already_there=False
								for e in armors_name_holder:
									if e==char_list[c].name:
										already_there=True
								if not already_there:
									armors_name_holder.append(char_list[c].name)
		else:
			#Check item for conflict
			armors_name_holder=[]
			accs_name_holder=[]
			for b in [x[0]]:
				if b in used_items.armors:
					armor_in_use==True
					##Search for character with item in use
					for c in char_list:
						for d in char_list[c].equipped:
							if b==d:
								#check if character has been flagged for a previous conflict
								already_there=False
								for e in armors_name_holder:
									if e==char_list[c].name:
										already_there=True
								if not already_there:
									armors_name_holder.append(char_list[c].name)
		if len(x)>combo_start:	#Set has accessory combos
			for b in range(combo_start,len(x)):
				curr_combo=x[b]	#set current combo
				good_combo=True
				for c in curr_combo:
					if c in used_items.armors:	#Item in use
						good_combo=False
						for d in char_list:	#go through characters
							for e in char_list[d].equipped:
								if c==e:	#Character has item
									already_there=False
									#Check if character had previous conflict
									for f in accs_name_holder:
										if f==char_list[d].name:
											already_there=True
									if not already_there:
										accs_name_holder.append(char_list[d].name)
				if good_combo:
					good_combos[a].append(curr_combo)
			if len(good_combos[a])!=0:
				good_accessories=True
		else:	#No accessory combos
			good_accessories=True
		if armor_in_use:
			#armor item/set has conflicts
			occupied_armors.append(a)
			occupied_char_armors.append(armors_name_holder)
			#check if the combos had any good sets
			if len(good_combos[a])==0:
				occupied_char_accs.append(accs_name_holder)
				#good_combos[a]=[[]]
			else:
				occupied_char_accs.append([])
		elif not good_accessories:
			occupied_armors.append(a)
			occupied_char_armors.append(armors_name_holder)
			occupied_char_accs.append(accs_name_holder)
	##START EQUIP CYCLE
	#print(len(occupied_armors))
	if len(occupied_armors)!=0:	#is at least once conflict
		print("There are sets with conflicts.")
		seq_count=0
		continue_armors=False
		for a in range(0,len(occupied_armors)):
			if a==occupied_armors[a]:
				seq_count+=1
		##THE FIRST ARMOR SET HAS NO CONFLICTS
		if seq_count==0:
			curr_set=armor_items[seq_count]
			if type(curr_set[0])==list:
				curr_armors=curr_set[0]
			else:
				curr_armors=[curr_set[0]]
			##GET SMALLEST ACCESSORY SET IF THERE ARE SOME
			if len(curr_set)>combo_start:
				if len(good_combos[a])==0:	#No good combos stored but the list is longer for some reason?
					curr_armors+=curr_set[combo_start]
					equip_order=armor_equip_order(curr_armors, char)
				else:
					#store the set with the least items
					long_set=100
					for b in good_combos[a]:
						num_of_items=0
						for c in b:
							if c!=0:
								num_of_items+=1
						if num_of_items<long_set:
							short_set=b
							long_set=num_of_items
					##add shortest set to current armor set and get equip order
					curr_armors+=short_set
					equip_order=armor_equip_order(curr_armors, char)
			else:
				equip_order=armor_equip_order(curr_armors,char)
			##Equip items in sorted equip order
			for b in equip_order:
				char.equipit(True, b)
		##AT LEAST 1 ARMOR SET HAS NO CONFLCITS
		elif seq_count!=len(armor_items):
			print("There are "+str(seq_count)+" armor sets before the first set "+
				"that doesn't have any conflicts with other characters' equipment.")
			#Begin adding up armor ratings for both
			best_armor=0
			other_armor=0
			for a in [0, seq_count]:
				rating_col=2
				temp_rating=0
				if type(armor_items[a][0])==list:
					for b in armor_items[a][0]:
						if b!=0:
							holder=armor[b][rating_col]
							if holder!='N/A':
								temp_rating+=int(holder)
				else:
					b=armor_items[a][0]
					if b!=0:
							holder=armor[b][rating_col]
							if holder!='N/A':
								temp_rating+=int(holder)
				if a==0:
					best_armor=temp_rating
				else:
					other_armor=temp_rating			
			print("The difference in armour rating between the top set and the first conflict free one is "+
				str(best_armor-other_armor)+". \nGo to first conflict free option?")
			if 'y'==yes_or_no():
				curr_set=armor_items[seq_count]
				if type(curr_set[0])==list:
					curr_armors=curr_set[0]
				else:
					curr_armors=[curr_set[0]]
				##GET SMALLEST ACCESSORY SET IF THERE ARE SOME
				if len(curr_set)>combo_start:
					if len(good_combos[a])==0:	#No good combos stored but the list is longer for some reason?
						curr_armors+=curr_set[combo_start]
						equip_order=armor_equip_order(curr_armors, char)
					else:
						#store the set with the least items
						long_set=100
						for b in good_combos[a]:
							num_of_items=0
							for c in b:
								if c!=0:
									num_of_items+=1
							if num_of_items<long_set:
								short_set=b
								long_set=num_of_items
						##add shortest set to current armor set and get equip order
						curr_armors+=short_set
						equip_order=armor_equip_order(curr_armors, char)
				else:
					equip_order=armor_equip_order(curr_armors,char)
				##Equip items in sorted equip order
				for b in equip_order:
					char.equipit(True, b)
		else:
			print("Every set has a conflict with one or more characters' equipment."+\
				"Try a larger set of combinations from total possible combinations.")
	else:
		a=0
		curr_set=armor_items[a]
		if type(curr_set[0])==list:
			curr_armors=curr_set[0]
		else:
			curr_armors=[curr_set[0]]
		##GET SMALLEST ACCESSORY SET IF THERE ARE SOME
		if len(curr_set)>combo_start:
			if len(good_combos[a])==0:	#No good combos stored but the list is longer for some reason?
				curr_armors+=curr_set[combo_start]
				equip_order=armor_equip_order(curr_armors, char)
			else:
				#store the set with the least items
				long_set=100
				for b in good_combos[a]:
					num_of_items=0
					for c in b:
						if c!=0:
							num_of_items+=1
					if num_of_items<long_set:
						short_set=b
						long_set=num_of_items
				##add shortest set to current armor set and get equip order
				curr_armors+=short_set
				equip_order=armor_equip_order(curr_armors, char)
		else:
			equip_order=armor_equip_order(curr_armors,char)
		##Equip items in sorted equip order
		for b in equip_order:
			char.equipit(True, b)
		
#
#function to equip weapons
def equip_max_weapons(weaps, weap_typ, char):
	occupied_weaps=[]
	occupied_char_weaps=[]
	occupied_char_accs=[]
	good_combos={}
	if weap_typ in ['elemental', 'Elemental']:
		print("Elemental Equip")
		for a in range(0, len(weaps)):	#begin going through entire list
			good_combos[a]=[]
			x=weaps[a]
			weapon_in_use=False	#Variable to mark if weapon in set is in conflict
			good_accessories=False	#variable to mark if any single accessory combo is not in conflict
			##DUAL WIELD COMBO
			if type(x[0])==list:
				temp_char_holder1=[]	#list holder for char_name conflicts with weapons
				temp_char_holder2=[]
				for b in x[0]:
					if b in used_items.weapons and not weapon_in_use:
						#occupied_weaps.append(a)
						weapon_in_use=True
					if b in used_items.weapons:
						#ITEM IS IN USE, LOG NAME OF CHARACTERS IT CONFLICTS WITH
						for c in char_list:
							already_there=False
							for d in char_list[c].equipped:
								if b == d:
									for e in temp_char_holder1:
										if e==char_list[c]:	#NAME ALREADY BEEN LOGGED
											already_there=True
									if not already_there:	#NAME NOT THERE, ADD
										temp_char_holder1.append(char_list[c].name)
				if len(x)>4:	#WEAPON SET HAS COMBOS
					for b in range(4, len(x)):	#GO THROUGH ALL ACCS COMBINATIONS
						combo_good=True
						curr_accs=x[b]
						for c in curr_accs:
							if c in used_items.armors:
								combo_good=False
								for d in char_list:
									for e in char_list[d].equipped:
										if c==e:
											already_there=False
											for f in temp_char_holder2:
												if char_list[d].name==f:
													already_there=True
											if not already_there:
												temp_char_holder2.append(char_list[d].name)
						if combo_good:
							good_combos[a].append(curr_accs)
			##SINGLE WEAPON
			else:
				temp_char_holder1=[]	#list holder for char_name conflicts with weapons
				temp_char_holder2=[]
				any_found=False
				if x[0] in used_items.weapons:	#Weapon is in use already
					weapon_in_use=True
					for b in char_list:	#go through characters and store who has item
						for c in char_list[b].equipped:
							if c==x[0]:
								already_there=False
								for d in temp_char_holder1: #if name is already in list, skip
									if d==char_list[b].name:
										already_there=True
								if not already_there:
									temp_char_holder1.append(char_list[b].name)
				if len(x)>4:	#WEAPON SET HAS COMBOS
					for b in range(4, len(x)):	#GO THROUGH ALL ACCS COMBINATIONS
						combo_good=True
						curr_accs=x[b]
						for c in curr_accs:
							if c in used_items.armors:
								combo_good=False
								for d in char_list:
									for e in char_list[d].equipped:
										if c==e:
											already_there=False
											for f in temp_char_holder2:
												if char_list[d].name==f:
													already_there=True
											if not already_there:
												temp_char_holder2.append(char_list[d].name)
						if combo_good:
							good_combos[a].append(curr_accs)
			#CHECK IF ANY WEAPONS ARE USED AND IF THERE ARE ANY GOOD ACCS COMBOS
			if weapon_in_use:
				occupied_weaps.append(a)
				occupied_char_weaps.append(temp_char_holder1)
				if len(x)>4:
					if len(good_combos[a])==0:
						occupied_char_accs.append(temp_char_holder2)
					else:
						occupied_char_accs.append([])
			#NO weapon in use but there are accessory combinations
			elif len(x)>4 and len(good_combos[a])==0:
				occupied_weaps.append(a)
				occupied_char_accs.append(temp_char_holder2)
				occupied_char_weaps.append([])
		if len(occupied_weaps)!=0:	#there are conflict items
			print("There are conflcits.")
			#find the length until first conflict free item
			seq_count=0
			continue_weaps=False
			for a in range(0,len(occupied_weaps)):
				if a==occupied_weaps[a]:
					seq_count+=1
			#print(seq_count)
			if seq_count==0:	#best weapon set has no conflicts, equipit
				#print(good_combos[a])
				curr_set=weaps[0]
				if len(curr_set)>4:	#Set has accessory combinations
					for a in good_combos[0][0]:	#equip first accesory combination
						char.equipit(True, a)
				if type(curr_set[0])==list:
					for a in curr_set[0]:
						char.equipit(False, a)
				else:
					char.equipit(False, curr_set[0])
			elif seq_count!=len(weaps):	#Haven't reached end of list
				print("There are "+str(seq_count)+" weapon sets that have conflicts "+
					"with other characters' equipemnt, "+
						"before the first weapon set with out a conflict.")
				print("The damage difference between the highest weapon set and the first "+
					"conflict free set is: "+str(weaps[0][1][len(weaps[0][1])-1]-
						weaps[seq_count][1][len(weaps[seq_count][1])-1]))
				print("Would you like to go to the conflict free weapon?")
				if 'y'==yes_or_no():	#Go to conflict free set and equip
					curr_set=weaps[seq_count]
					if len(curr_set)>4:	#Set has accessory combinations
						for a in good_combos[seq_count][0]:	#equip first accesory combination
							char.equipit(True, a)
					if type(curr_set[0])==list:
						for a in curr_set[0]:
							char.equipit(False, a)
					else:
						char.equipit(False, curr_set[0])
					
				else:	#Want to continue through conflict weapons
					continue_weaps=True
			else:
				print("Reached end of weapon sets and there are none without a conflict with other characters' equipemnt.")
				print("Would you like to try to equip a set anyway?")
				if 'y'==yes_or_no():
					continue_weaps=True
			if continue_weaps:	#GO THROUGH CONFLICT SETS
				##BE SURE TO ASK FOR EVERY CONFLICT TO SEE IF WE SHOULD EQUIP ANYWAYS
				weapons_equipped=False
				a=0
				while not weapons_equipped and a!=len(weaps)-1:
					if a in occupied_weaps:	#Set has conflicts
						print("Set has conflicts with the following characters' equipment:")
						for b in range(0,len(occupied_weaps)):
							if occupied_weaps[b]==a:
								for c in occupied_char_weaps[b]:
									already_there=False
									for d in occupied_char_accs[b]:
										if c==d:
											already_there=True
									if not already_there:
										print(c)
								for c in occupied_char_accs[b]:
									print(c)
							print("Would you like to continue with equipping the set or go to the next set?")
							if 'y'==yes_or_no():
								for c in occupied_char_weaps[b]:
									for d in char_list:
										if char_list[d].name==c:
											char_list[d].clear_equipment()
								for c in occupied_char_accs[b]:
									for d in char_list:
										if char_list[d].name==c:
											char_list[d].clear_equipment()
								curr_set=weaps[a]
								
								if len(curr_set)>4:	#Set has accessory combinations
									for c in good_combos[a][0]:	#equip first accesory combination
										char.equipit(True, c)
								if type(curr_set[0])==list:
									for c in curr_set[0]:
										char.equipit(False, c)
								else:
									char.equipit(False, curr_set[0])
								weapons_equipped=True
					else:	#Set has no conflicts
						curr_set=weaps[a]
						if len(curr_set)>4:	#Set has accessory combinations
							for c in good_combos[a][0]:	#equip first accesory combination
								char.equipit(True, c)
						weapons_equipped=True
						if type(curr_set[0])==list:
							for c in curr_set[0]:
								char.equipit(False, c)
						else:
							char.equipit(False, curr_set[0])
					a+=1
		else:	#NO CONFLICTS IN LIST
			print("No conflicts.")
			#print(good_combos[0])
			curr_set=weaps[0]
			if len(curr_set)>4:	#Set has accessory combinations
				print(good_combos[0][0])	#DELETE LATER
				for c in good_combos[0][0]:	#equip first accesory combination
					#print(c)	#DELETE LATER
					char.equipit(True, c)	
			if type(curr_set[0])==list:
				for c in curr_set[0]:
					char.equipit(False, c)
			else:
				char.equipit(False, curr_set[0])			
	else:	#Physical type damage weapon
		for a in range(0, len(weaps)):	#begin going through entire list
			good_combos[a]=[]
			x=weaps[a]
			weapon_in_use=False	#Variable to mark if weapon in set is in conflict
			good_accessories=False	#variable to mark if any single accessory combo is not in conflict
			##DUAL WIELD COMBO
			if type(x[0])==list:
				temp_char_holder1=[]	#list holder for char_name conflicts with weapons
				temp_char_holder2=[]
				for b in x[0]:
					if b in used_items.weapons and not weapon_in_use:
						#occupied_weaps.append(a)
						weapon_in_use=True
					if b in used_items.weapons:
						#ITEM IS IN USE, LOG NAME OF CHARACTERS IT CONFLICTS WITH
						for c in char_list:
							already_there=False
							for d in char_list[c].equipped:
								if b == d:
									for e in temp_char_holder1:
										if e==char_list[c]:	#NAME ALREADY BEEN LOGGED
											already_there=True
									if not already_there:	#NAME NOT THERE, ADD
										temp_char_holder1.append(char_list[c].name)
				if len(x)>6:	#WEAPON SET HAS COMBOS
					for b in range(6, len(x)):	#GO THROUGH ALL ACCS COMBINATIONS
						combo_good=True
						curr_accs=x[b]
						for c in curr_accs:
							if c in used_items.armors:
								combo_good=False
								for d in char_list:
									for e in char_list[d].equipped:
										if c==e:
											already_there=False
											for f in temp_char_holder2:
												if char_list[d].name==f:
													already_there=True
											if not already_there:
												temp_char_holder2.append(char_list[d].name)
						if combo_good:
							good_combos[a].append(curr_accs)
			##SINGLE WEAPON
			else:
				temp_char_holder1=[]	#list holder for char_name conflicts with weapons
				temp_char_holder2=[]
				any_found=False
				if x[0] in used_items.weapons:	#Weapon is in use already
					weapon_in_use=True
					for b in char_list:	#go through characters and store who has item
						for c in char_list[b].equipped:
							if c==x[0]:
								already_there=False
								for d in temp_char_holder1: #if name is already in list, skip
									if d==char_list[b].name:
										already_there=True
								if not already_there:
									temp_char_holder1.append(char_list[b].name)
				if len(x)>6:	#WEAPON SET HAS COMBOS
					for b in range(6, len(x)):	#GO THROUGH ALL ACCS COMBINATIONS
						combo_good=True
						curr_accs=x[b]
						for c in curr_accs:
							if c in used_items.armors:
								combo_good=False
								for d in char_list:
									for e in char_list[d].equipped:
										if c==e:
											already_there=False
											for f in temp_char_holder2:
												if char_list[d].name==f:
													already_there=True
											if not already_there:
												temp_char_holder2.append(char_list[d].name)
						if combo_good:
							good_combos[a].append(curr_accs)
			#CHECK IF ANY WEAPONS ARE USED AND IF THERE ARE ANY GOOD ACCS COMBOS
			if weapon_in_use:
				occupied_weaps.append(a)
				occupied_char_weaps.append(temp_char_holder1)
				if len(x)>6:
					if len(good_combos[a])==0:
						occupied_char_accs.append(temp_char_holder2)
					else:
						occupied_char_accs.append([])
			#NO weapon in use but there are accessory combinations
			elif len(x)>6 and len(good_combos[a])==0:
				occupied_weaps.append(a)
				occupied_char_accs.append(temp_char_holder2)
				occupied_char_weaps.append([])
		if len(occupied_weaps)!=0:	#there are conflict items
			#find the length until first conflict free item
			seq_count=0
			continue_weaps=False
			for a in range(0,len(occupied_weaps)):
				if a==occupied_weaps[a]:
					seq_count+=1
			if seq_count==0:	#best weapon set has no conflicts, equipit
				curr_set=weaps[0]
				if len(curr_set)>6:	#Set has accessory combinations
					for a in good_combos[0][0]:	#equip first accesory combination
						char.equipit(True, a)
				if type(curr_set[0])==list:	#weapons are a set
					for a in curr_set[0]:
						char.equipit(False, a)
				else:	#Single weapon to be equipped
					char.equipit(False, curr_set[0])
			elif seq_count!=len(weaps)-1:	#Haven't reached end of list
				print("There are "+str(seq_count)+" weapon sets that have conflicts "+
					"with other characters' equipemnt, "+
						"before the first weapon set with out a conflict.")
				print("The damage difference between the highest weapon set and the first "+
					"conflict free set is: "+str(weaps[0][2]-weaps[seq_count][2]))
				print("Would you like to go to the conflict free weapon?")
				if 'y'==yes_or_no():	#Go to conflict free set and equip
					curr_set=weaps[seq_count]
					
					if len(curr_set)>6:	#Set has accessory combinations
						for a in good_combos[seq_count][0]:	#equip first accesory combination
							char.equipit(True, a)
					if type(curr_set[0])==list:
						for a in curr_set[0]:
							char.equipit(False, a)
					else:
						char.equipit(False, curr_set[0])
				else:	#Want to continue through conflict weapons
					continue_weaps=True
			else:
				print("Reached end of weapon sets and there are none without a conflict with other characters' equipemnt.")
				print("Would you like to try to equip a set anyway?")
				if 'y'==yes_or_no():
					continue_weaps=True
			if continue_weaps:	#GO THROUGH CONFLICT SETS
				##BE SURE TO ASK FOR EVERY CONFLICT TO SEE IF WE SHOULD EQUIP ANYWAYS
				weapons_equipped=False
				a=0
				while not weapons_equipped and a!=len(weaps)-1:
					if a in occupied_weaps:	#Set has conflicts
						print("Set has conflicts with the following characters' equipment:")
						for b in range(0,len(occupied_weaps)):
							if occupied_weaps[b]==a:
								for c in occupied_char_weaps[b]:
									already_there=False
									for d in occupied_char_accs[b]:
										if c==d:
											already_there=True
									if not already_there:
										print(c)
								for c in occupied_char_accs[b]:
									print(c)
							print("Would you like to continue with equipping the set or go to the next set?")
							if 'y'==yes_or_no():
								for c in occupied_char_weaps[b]:
									for d in char_list:
										if char_list[d].name==c:
											char_list[d].clear_equipment()
								for c in occupied_char_accs[b]:
									for d in char_list:
										if char_list[d].name==c:
											char_list[d].clear_equipment()
								curr_set=weaps[a]
								if len(curr_set)>6:	#Set has accessory combinations
									for c in good_combos[a][0]:	#equip first accesory combination
										char.equipit(True, c)
								if type(curr_set[0])==list:
									for c in curr_set[0]:
										char.equipit(False, c)
								else:
									char.equipit(False, curr_set[0])
								weapons_equipped=True
					else:	#Set has no conflicts
						curr_set=weaps[a]
						if len(curr_set)>6:	#Set has accessory combinations
							for c in good_combos[a][0]:	#equip first accesory combination
								char.equipit(True, c)
						if type(curr_set[0])==list:
							for c in curr_set[0]:
								char.equipit(False, c)
						else:
							char.equipit(False, curr_set[0])
						weapons_equipped=True
					a+=1
		else:	#NO CONFLICTS IN LIST
			curr_set=weaps[0]
			
			if len(curr_set)>6:	#Set has accessory combinations
				for c in good_combos[0][0]:	#equip first accesory combination
					char.equipit(True, c)	
			if type(curr_set[0])==list:
				for c in curr_set[0]:
					char.equipit(False, c)
			else:
				char.equipit(False, curr_set[0])				

#
#sort armor set to be equipped in a way that the items that provide attributes buffs
#are equipped first allowing the armors with higher levels to be equipped by the character
def armor_equip_order(equip_list, char):
	temp_holder=[]
	i=0
	for a in armor_headers:
		if bool(re.search('req',armor_headers[a], re.IGNORECASE)):
			req_col=a
	for a in equip_list:
		if a!=0:
			req_str=armor[a][req_col]
			if req_str!='N/A':
				req_attr=req_str[0:3]
				req_lvl=int(req_str[4:len(req_str)])
			else:
				req_attr='none'
				req_lvl=0
				req_pos=1
			for b in attr_headers:
				if bool(re.search(req_attr, attr_headers[b], re.IGNORECASE)):
					req_pos=b
			if char.attr[req_pos]>=req_lvl:
				temp_holder.append(a)
	##sort and add remainder
	temp_holder2=[]
	for a in equip_list:
		if a not in temp_holder and a!=0:
			temp_holder2.append(a)
	highest_req_lvl=0
	for x in range(0,len(temp_holder2)):
		a=temp_holder2[x]
		req_lvla=int(armor[a][req_col][4:len(armor[a][req_col])])
		for y in range(x+1, len(temp_holder2)):
			b=temp_holder2[y]
			req_lvlb=int(armor[b][req_col][4:len(armor[b][req_col])])
			if req_lvla>req_lvlb:
				i=a
				temp_holder2[x]=b
				temp_holder2[y]=a
	for a in temp_holder2:
		temp_holder.append(a)
	return temp_holder
	
#
#Interface for viewing the database		
def view_database_interface():
	#view_inventory(True, unq_ident_armor)
	print("Choose an action.")
	print('1. View Weapons Database \n2. View Armors Database')
	if number_select(2)==1:
		db_items=sorting_order(False, 1)
		armor_picked=False
	else:
		db_items=sorting_order(True, 1)
		armor_picked=True
	##interface loop
	database_view=True
	while database_view:
		view_inventory(armor_picked, db_items)
		print("Choose an action.")
		print('1. Equip an item'+'\n'+'2. Re-sort by column'+'\n'+'3. Exit')
		database_select=number_select(3)
		if database_select==1:
			print('Enter the number of the item to equip.')
			print('*Please not the item requirements when equipping to a character.')
			item_select=db_items[number_select(len(db_items))-1]
			if armor_picked:
				print(armor[item_select][0]+" has been selected.")
			else:
				print(weapons[item_select][0]+" has been selected.")
			print("Please select the character you would like to equip the item to:")
			for a in char_list:
				print(str(a)+': '+char_list[a].name)
			item_char_select=number_select(len(char_list))
			char_list[item_char_select].equipit(armor_picked, item_select)
		elif database_select==2:
			print("Pick from the list below:")
			if armor_picked:
				header_selection=armor_headers
			else:
				header_selection=weapon_headers
			for a in header_selection:
				print(str(a+1)+': '+header_selection[a])
			header_select=number_select(len(header_selection))
			db_items=sorting_order(armor_picked, header_select-1)
		elif database_select==3:
			print("Are you sure you want to stop viewing the database?")
			really_exit=yes_or_no()
			if really_exit=='y':
				database_view=False
		input("Press enter to continue.")
	
#
#get a number input and return it as an integer value									
def number_select(limit):
	num_pick_wait=True
	while num_pick_wait:
		choice=input("Please enter only the number: ")
		num_loc=re.search('[0-9]+', choice)
		if bool(num_loc):
			choice=int(choice[num_loc.start():num_loc.end()])
			if choice<=limit and choice!=0:	
				num_pick_wait=False
			else:
				print("Invalid entry. Try again.")
		else:
			print("Invalid entry. Try again.")
	return choice

#
#get a 'y' or 'n; input and return that input		
def yes_or_no():
	picked=True
	while picked:
		k=input("y/n: ")
		if k=='y' or k=='n':
			picked=False
		else:
			print('Invaid entry, please enter only "y" or "n".')
	return k
					
class player:
	def __init__(self, name, row):
		self.name = name
		self.row = row
		self.attr_raw=attributes[row]
		self.attr = [0]*len(attributes[row])
		for x in range(0,len(self.attr)):
			if x!=0:
				b=self.attr_raw[x]
				self.attr[x]=int(b)
			else:
				b=self.attr_raw[x]
				self.attr[x]=b
		self.abil_raw=abilities[row]
		self.abil = [0]*len(abilities[row])
		for x in range(0, len(self.abil)):
			if x!=0:
				b=self.abil_raw[x]
				self.abil[x]=int(b)
			else:
				b=self.abil_raw[x]
				self.abil[x]=b
		self.equipped = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.ratings = [0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.resistance = [0, 0, 0, 0, 0, 0]
		self.dual_wielding=False
		self.has_shield=False
		
	def equipit(self, is_armor, item):
		#print(str(table)+' '+str(item))
		if item!=0:
			#equip a weapon, hands spaces are 6 an 7 in equipped list
			if not is_armor:
				##CHECK REQS OF ITEM
				can_equip=False
				for a in weapon_headers:
					if bool(re.match('Requirement', weapon_headers[a], re.IGNORECASE)):
						if weapons[item][a]!='N/A':
							item_req=weapons[item][a][0:3]
							item_lvl=int(weapons[item][a][4:len(weapons[item][a])])
							for b in attr_headers:
								if bool(re.search(item_req, attr_headers[b], re.IGNORECASE)):
									if self.attr[b]>=item_lvl:
										can_equip=True
						else:	#THERE IS NO ITEM REQUIREMENT
							can_equip=True
				##IF ITEM IS EQUIPABLE BY CHARACTER
				if can_equip:
					for x in weapon_headers:
						i=bool(re.match('Type', weapon_headers[x], re.IGNORECASE))
						j=bool(re.match('Hands', weapon_headers[x], re.IGNORECASE))
						if i:
							type_col = x
						if j:
							hands_col = x
					item_type = weapons[item][type_col]
					hands_req = int(weapons[item][hands_col])
					if hands_req == 2:
						for x in [6,7]:
							if self.equipped[x]!=0:
								self.unequip(self.equipped[x], x)
						self.equipped[6] = item
						self.equipped[7] = item
						print(str(self.name) + ' equipped ' + str(weapons[item][0]) + '!')
						used_items.add(item, False)
					##ITEM ONLY REQUIRES 1 HAND
					else:
						##BOTH HANDS FULL
						if self.equipped[6]!=0 and self.equipped[7]!=0:
							print("Weapons already equipped, remove and equip new item?")
							if 'y'==yes_or_no():
								print("Pick which you would like to unequip")
								print("1: "+weapons[self.equipped[6]][0])
								if self.has_shield:
									print("2: "+armor[self.equipped[7]][0])
								else:
									print("2: "+weapons[self.equipped[7]][0])
								if number_select(2)==1:
									self.unequip(self.equipped[6],6)
									self.equipped[6]=int(item)
								else:
									self.unequip(self.equipped[7],7)
									self.equipped[7]=int(item)
								if self.equipped[6]!=0 and self.equipped[7]!=0 and not self.has_shield and \
								self.equipped[6]!=self.equipped[7]:
										self.dual_wielding=True
							print(str(self.name) + ' equipped ' + str(weapons[item][0]) + '!')
							used_items.add(item, False)
						##MAIN HAND FULL, SIDE HAND OPEN	
						elif self.equipped[6]!=0 and self.equipped[7]==0:
							self.equipped[7] = item
							self.dual_wielding=True
							print(str(self.name) + ' equipped ' + str(weapons[item][0]) + '!')
							used_items.add(item, False)
						##MAIN HAND OPEN
						else:
							self.equipped[6]=int(item)
							print(str(self.name) + ' equipped ' + str(weapons[item][0]) + '!')
							used_items.add(item, False)
				else:
					print(weapons[item][0]+"'s requirements are too high for "+self.name)
			#Equip armor items
			if is_armor:
				##CHECK REQS OF ITEM
				can_equip=False
				for a in armor_headers:
					if bool(re.match('Requirement', armor_headers[a], re.IGNORECASE)):
						if armor[item][a]!='N/A':
							item_req=armor[item][a][0:3]
							item_lvl=int(armor[item][a][4:len(armor[item][a])])
							for b in attr_headers:
								if bool(re.search(item_req, attr_headers[b], re.IGNORECASE)):
									if self.attr[b]>=item_lvl:
										can_equip=True
						else: ##ITEM HAS NO REQUIREMENTS
							can_equip=True
				##IF ITEM IS EQUIPABLE
				if can_equip:
					#find the type col in the armor table
					for x in armor_headers:
						i=bool(re.match('Type', armor_headers[x], re.IGNORECASE))
						if i:
							type_col = x
					item_type = armor[item][type_col]
					if item_type == 'Helmet':
						equip_slot = 0
					elif item_type == 'Chest':
						equip_slot = 1
					elif item_type == 'Undergarment':
						equip_slot = 2
					elif item_type == 'Waist':
						equip_slot = 3
					elif item_type == 'Boots':
						equip_slot = 4
					elif item_type == 'Gloves':
						equip_slot = 5
					elif item_type == 'Shield':
						self.has_shield=True
						equip_slot = 7
					elif item_type == 'Amulet':
						equip_slot = 8
					elif item_type == 'Accessory':
						if self.equipped[9]!=0 and self.equipped[10]==0:
							equip_slot = 10
						elif self.equipped[9]==0:
							equip_slot = 9
						else:
							print("Both accesory slots filled.")
							print("Pick which you would like to replace:")
							print("1. "+armor[self.equipped[9]][0]+'\n'+
								"2. "+armor[self.equipped[10]][0])
							equip_slot=int(number_select(2)+8)
					else:
						print('None found')
						print(item_type)
						print(armor[item])
					if self.equipped[equip_slot]!=0:
						self.unequip(self.equipped[equip_slot], equip_slot)
					self.equipped[equip_slot] = item
					print(str(self.name) + ' equipped the ' + item_type + ', ' + str(armor[item][0]) + '!')
					used_items.add(item, True)
				else:
					print(armor[item][0]+"'s requirements are too high for "+self.name)
			self.calc_ratings()
			
	def unequip(self, item, slot):
		if slot!=6 and slot!=7:
			used_items.remove(item, True)
			self.equipped[slot]=0
			print(self.name+" removed "+armor[item][0])
		else:
			if self.equipped[6]==self.equipped[7] and self.equipped[6]!=0:
				self.equipped[6]=0
				self.equipped[7]=0
				used_items.remove(item, False)
				print(self.name+" removed "+weapons[item][0])
			elif slot==6:
				self.equipped[6]=0
				used_items.remove(item, False)
				print(self.name+" removed "+weapons[item][0])
				#MOVE OFF HAND ITEM TO MAIN HAND
				if self.equipped[7]!=0 and not self.has_shield:
					self.equipped[6]=self.equipped[7]
					self.equipped[7]=0
			elif slot==7:
				self.equipped[7]=0
				if self.has_shield:
					self.has_shield==False
					used_items.remove(item, True)
					print(self.name+" removed "+armor[item][0])
				else:
					used_items.remove(item, False)
					print(self.name+" removed "+weapons[item][0])
		self.calc_ratings()
	
	def calc_ratings(self):
		##ADD SPECIALS
		specials_holder=[[0]*len(self.attr),[0]*len(self.abil),[0]*len(self.resistance)]
		two_handed_done=False
		for x in range(0,len(self.equipped)):
			if self.equipped[x]!=0:
				if x!=6 and x!=7:
					temp_specials=find_specials(self.equipped[x], 'armor')
					#print(armor[self.equipped[x]][0])
				else:
					if self.equipped[6]==self.equipped[7] and self.equipped[6]!=0 and not self.has_shield:
						if not two_handed_done:
							temp_specials=find_specials(self.equipped[6], 'weapon')
							#print(weapons[self.equipped[x]][0])
					elif x==7:
						if self.has_shield:
							temp_specials=find_specials(self.equipped[7], 'armor')
							#print(armor[self.equipped[x]][0])
						else:
							temp_specials=find_specials(self.equipped[7], 'weapon')
							#print(weapons[self.equipped[x]][0])
					elif x==6:
						temp_specials=find_specials(self.equipped[6], 'weapon')
						#print(weapons[self.equipped[x]][0])
				'''for a in temp_specials:
					print(a)'''
				for y in range(0,len(temp_specials)):
					for z in range(0,len(specials_holder[y])):
						specials_holder[y][z]+=temp_specials[y][z]
		for x in range(0,len(specials_holder)):	#Add specials for character
			for y in range(0,len(specials_holder[x])):
				if x==0:
					if y!=0:
						#print(attr_headers[y]+' '+str(self.attr_raw[y])+'+'+str(specials_holder[x][y]))
						self.attr[y]=int(self.attr_raw[y])+specials_holder[x][y]
						#print(attr_headers[y]+' '+str(self.attr[y]))
				elif x==1:
					if y!=0:
						self.abil[y]=int(self.abil_raw[y])+specials_holder[x][y]
				elif x==2:
					if y==0:
						self.resistance=[0, 0, 0, 0, 0, 0]
						self.resistance[y]+=specials_holder[x][y]
					else:
						self.resistance[y]+=specials_holder[x][y]
		#Equip headers: Helmet, Chest, Under, waist, Boots, Gloves, 
		#Hand 1, Hand 2, Amulet, Access. 1, Access. 2
		#WEAPON CALCS
		self.ratings[3]=0
		if self.equipped[6]!=0 or (self.equipped[7]!=0 and not self.has_shield):
			phys_types=['Piercing', 'Slashing', 'Crushing']
			##PLACEHOLDER SOLUTION UNTIL ELEMENTAL DAMAGE SOLUTIONS ARE ADDED
			dmg_lo=0
			dmg_hi=0
			#store name and damage values
			#dmg value = dmg weapons + single/two handed or crossbow/bow buff + special buffs
			if self.equipped[6]==self.equipped[7] and not self.has_shield:	#ITEM IS TWO HANDED
				#Check if item is a bow of some kind
				eq_weap = self.equipped[6]
				eq_name = weapons[eq_weap][0]
				if weapons[eq_weap][1] in phys_types:
					dmg_hi = dmg_hilo(eq_weap, 'physical', 'hi')
					dmg_lo = dmg_hilo(eq_weap, 'physical', 'lo')
					is_crossbow = bool(re.search('crossbow', eq_name, re.IGNORECASE))
					is_arbalest = bool(re.search('arbalest', eq_name, re.IGNORECASE))
					isbow = bool(re.search('bow', eq_name, re.IGNORECASE))
					#IS CROSSBOW, APPLY BOOSTS
					if is_crossbow or is_arbalest:
						crossbow_pts = 0
						for y in abil_headers:
							i = abil_headers[y]
							if i == 'Crossbow':
								crossbow_pts = int(self.abil[y])
						crossbow_pts_exceptions=[0,5,6]
						if crossbow_pts not in crossbow_pts_exceptions:
							self.ratings[3]=10+(crossbow_pts-1)*4
						elif crossbow_pts==5:
							self.ratings[3]=10+((crossbow_pts-2)*4)+3
						elif crossbow_pts==6:
							self.ratings[3]=27
					#IS BOW, APPLY BOOSTS
					if isbow and not is_crossbow:
						bow_pts = 0
						for y in abil_headers:
							i = abil_headers[y]
							if i == 'Bow':
								bow_pts = int(self.abil[y])
						dmg_hi=dmg_hi*(1+(.1*bow_pts))
						dmg_lo=dmg_lo*(1+(.1*bow_pts))
					#2 HANDED, PHYS DAMAGE ITEM, APPLY BOOSTS
					else:
						twohands_pts = 0
						for y in abil_headers:
							i = abil_headers[y]
							if i == 'Two-handed':
								twohands_pts = int(self.abil[y])
						twohands_pts_exceptions=[0,5,6]
						if twohands_pts not in twohands_pts_exceptions:
							self.ratings[3]=10+(twohands_pts-1)*4
						elif twohands_pts==5:
							self.ratings[3]=10+((twohands_pts-2)*4)+3
						elif twohands_pts==6:
							self.ratings[3]=27
			elif self.equipped[6]!=0 and self.equipped[7]!=0 and self.dual_wielding:
				weap1=self.equipped[6]
				weap2=self.equipped[7]
				weap1_type=weapons[weap1][1]
				weap2_type=weapons[weap2][1]
				#BOTH ITEMS ARE PHYSICAL DAMAGE TYPE
				if (weap1_type in phys_types) and (weap2_type in phys_types):	
					weap1_dmglo=dmg_hilo(weap1, 'physical', 'lo')
					weap2_dmglo=dmg_hilo(weap2, 'physical', 'lo')
					weap1_dmghi=dmg_hilo(weap1, 'physical', 'hi')
					weap2_dmghi=dmg_hilo(weap2, 'physical', 'hi')
					dmg_lo=weap1_dmglo+weap2_dmglo
					dmg_hi=weap1_dmghi+weap2_dmghi
					dual_wield_abil=self.abil[3]
					if dual_wield_abil==0:
						dmg_lo*=.7
						dmg_hi*=.7
					elif dual_wield_abil==1 or dual_wield_abil==2:
						dmg_lo*=.8
						dmg_hi*=.8
					elif dual_wield_combos==3:
						dmg_lo*=.9
						dmg_hi*=.9
					elif dual_wield_combos==4 or dual_wield_combos==5:
						dmg_lo*=1
						dmg_hi*=1
					elif dual_wield_combos==6:
						dmg_lo*=1.05
						dmg_hi*=1.05
				#ONLY ONE WEAPON HAS PHYS DAMAGE
				elif (weap1_type in phys_types) or (weap2_type in phys_types):
					if weap1_type in phys_types:
						#Find Single-handed ability
						dmg_lo=dmg_hilo(weap1, 'physical', 'lo')
						dmg_hi=dmg_hilo(weap1, 'physical', 'hi')
						onehand_pts = 0
						for y in abil_headers:
							i = abil_headers[y]
							if i == 'Single-handed':
								onehand_pts = int(self.abil[y])
						#add buff
						dmg_hi=dmg_hi*(1+(.1*onehand_pts))
						dmg_lo=dmg_lo*(1+(.1*onehand_pts))	
					else:
						weap1=weap2
						#Find Single-handed ability
						dmg_lo=dmg_hilo(weap1, 'physical', 'lo')
						dmg_hi=dmg_hilo(weap1, 'physical', 'hi')
						onehand_pts = 0
						for y in abil_headers:
							i = abil_headers[y]
							if i == 'Single-handed':
								onehand_pts = int(self.abil[y])
						#add buff
						dmg_hi=dmg_hi*(1+(.1*onehand_pts))
						dmg_lo=dmg_lo*(1+(.1*onehand_pts))
			else:
				if self.equipped[6]!=0:
					weap1=self.equipped[6]
					weap1_type=weapons[weap1][1]
					if weap1_type in phys_types:
						#Find Single-handed ability
						dmg_lo=dmg_hilo(weap1, 'physical', 'lo')
						dmg_hi=dmg_hilo(weap1, 'physical', 'hi')
						onehand_pts = 0
						for y in abil_headers:
							i = abil_headers[y]
							if i == 'Single-handed':
								onehand_pts = int(self.abil[y])
						#add buff
						dmg_hi=dmg_hi*(1+(.1*onehand_pts))
						dmg_lo=dmg_lo*(1+(.1*onehand_pts))
					else:	#Weapon is elemental damage
						dmg_lo=0
						dmg_hi=0
				elif self.equipped[7]!=0 and not self.has_shield:
					weap1=self.equipped[7]
					weap1_type=weapons[weap1][1]
					if weap1_type in phys_types:
						#Find Single-handed ability
						dmg_lo=dmg_hilo(weap1, 'physical', 'lo')
						dmg_hi=dmg_hilo(weap1, 'physical', 'hi')
						onehand_pts = 0
						for y in abil_headers:
							i = abil_headers[y]
							if i == 'Single-handed':
								onehand_pts = int(self.abil[y])
						#add buff
						dmg_hi=dmg_hi*(1+(.1*onehand_pts))
						dmg_lo=dmg_lo*(1+(.1*onehand_pts))
					else:	#Weapon is elemental damage
						dmg_lo=0
						dmg_hi=0
			#ROUND VALUES, CHANGE DAMAGE RATING
			dmg_lo=round(dmg_lo, 3)
			dmg_hi=round(dmg_hi, 3)
			#Store formatted dmg values into player ratings list
			self.ratings[0]=str(dmg_lo)+'-'+str(dmg_hi)
		crit_chance_added=False
		if self.ratings[3]!=0:
			crit_chance_added=True
	#Begin armor calculations
		armor_pieces=[0, 1, 4, 5]
		armor_ratings=[]	#make a list to hold all the armor values
		for x in armor_pieces:
			if self.equipped[x]!=0:
				armor_item = self.equipped[x]
				armor_rating = int(armor[armor_item][2])
				armor_ratings.append(armor_rating)
		#add all stored armor ratings
		total_armor_rating=0
		for x in armor_ratings:
			total_armor_rating = total_armor_rating+x
		#Look for armor rating buffs
		for x in abil_headers:
			if abil_headers[x]=='Armour Specialist':
				arm_spc=int(self.abil[x])
		#adjust final armor_rating
		total_armor_rating = int(total_armor_rating)*(1+(.05*arm_spc))
		self.ratings[1]=round(total_armor_rating, 6)
	#Blocking Chance Calculations
		if self.has_shield:
			shield_item = self.equipped[7]
			#Check if it is a shield
			for x in shields:
				shields_num=shields[x]
				is_shield=bool(armor[shields_num][0]==
						armor[shield_item][0])
				#print(armor[shield_item][0]+' '+armor[shields_num][0])
				if is_shield:
					#If it is a shield, extract blocking percentage
					blocking_per=armor[shield_item][3]
					per_sym=re.search('%',blocking_per)
					blocking_per=float(blocking_per[0:per_sym.start()])/100
					#Get the shield specialist buffs
					for y in abil_headers:
						if abil_headers[y]=='Shield Specialist':
							shield_buff=float(self.abil[y])
					blocking_per=blocking_per+(.05*shield_buff)
					blocking_per=round(blocking_per*100,2)
					self.ratings[2]=blocking_per
	#Critical Chance Calculations
		##Perception values added
		if int(self.attr[7])>5:
			perc_val=int(self.attr[7])
			crit_chn=(perc_val-5)*.01
		else:
			crit_chn=0
		if crit_chance_added:
			self.ratings[3]+=round(crit_chn*100, 3)
		else:
			self.ratings[3]=round(crit_chn*100, 3)
		##Add critical chance value from weapon
		if self.equipped[6]!=0 or (self.equipped[7]!=0 and not self.has_shield):
			if self.equipped[6]==self.equipped[7] and not self.has_shield:
				weap_crit_chn=weapons[self.equipped[6]][4]
				if bool(re.search('[0-9]+',weap_crit_chn)):
					weap_crit_chn=int(weap_crit_chn[0:len(weap_crit_chn)-1])
					self.ratings[3]+=weap_crit_chn
			else:
				if self.equipped[6]!=0:
					weap_crit_chn=weapons[self.equipped[6]][4]
					if bool(re.search('[0-9]+',weap_crit_chn)):
						weap_crit_chn=int(weap_crit_chn[0:len(weap_crit_chn)-1])
						self.ratings[3]+=weap_crit_chn
				if self.equipped[7]!=0 and not self.has_shield:
					weap_crit_chn=weapons[self.equipped[7]][4]
					if bool(re.search('[0-9]+',weap_crit_chn)):
						weap_crit_chn=int(weap_crit_chn[0:len(weap_crit_chn)-1])
						self.ratings[3]+=weap_crit_chn
	#Offense rating calculations
		'''off_rating=0
		two_handed=bool(self.equipped[6]==self.equipped[7] and self.equipped[6]!=0)
		for x in [6,7]:
			hand_equip=self.equipped[x]
			#make sure item is not a shield
			#if their is an item and is not a shield
			if x==6:
				#get weapon requirement
				weap_req = weapons[hand_equip][12][0:3]
				#Find matching requiremnt lvl from player
				for y in attr_headers:
					attr_abrv=attr_headers[y][0:3]
					if attr_abrv==weap_req:
						#if matches apply necs. offense rating
						off_rating=(int(self.attr[y])*6)+off_rating
		if two_handed:
			hand_equip=self.equipped[6]
			if hand_equip!=0:
				#get weapon requirement
				weap_req = weapons[hand_equip][12][0:3]
				#Find matching requiremnt lvl from player
				for y in attr_headers:
					attr_abrv=attr_headers[y][0:3]
					if attr_abrv==weap_req:
						#if matches apply necs. offense rating
						off_rating=(int(self.attr[y])*6)
		self.ratings[4]=round(off_rating, 2)
	#Defense rating calculations
		#check if dexterity of character is above 5
		if int(self.attr[3])>5:
			def_rating=8+(int(self.attr[3])-5)*2
		else:
			def_rating=0
		self.ratings[5]=def_rating'''
		
	def clear_equipment(self):
		for a in range(0,len(self.equipped)):
			if self.equipped[a]!=0:
				self.unequip(self.equipped[a], a)		
													
class equipped_items:
	def __init__(self):
		self.armors=[]
		self.weapons=[]
	
	def remove(self, item, armor):
		if item!=0:
			if armor:
				if len(self.armors)>0:
					remove_slot=0
					for x in range(0,len(self.armors)):
						if self.armors[x]==item:
							remove_slot=x
					self.armors.pop(x)
				else:
					print("No armour items are currently being used.")
			else:
				if len(self.weapons)>0:
					remove_slot=0
					for x in range(0,len(self.weapons)):
						if self.weapons[x]==item:
							remove_slot=x
					self.weapons.pop(x)
				else:
					print("No weapons are currently being used.")
	
	def add(self, item, armor):
		if armor:
			if item not in self.armors:
				self.armors.append(item)
			else:
				print("Armour is alread being used.")
		else:
			if item not in self.weapons:
				self.weapons.append(item)
			else:
				print("Weapon is already being used.")
				
#####################################
##AUTO OPEN
weapons_path=''
abilities_path=''
attributes_path=''
armors_path=''
csv_paths=[weapons_path, abilities_path, attributes_path, armors_path]
for a in range(0,len(csv_paths)):
	b=csv_paths[a]
	b=''
csv_files={}
print("Curent Directory: "+abspath(curdir))
no_files=True
while no_files:
	csv_count=1
	#Search for csv's in curdir
	for a in os.listdir(curdir):
		if bool(re.search('.csv', a, re.IGNORECASE)):
			csv_files[csv_count]=abspath(curdir)+'\\'+a
			#print(csv_files[csv_count])
			csv_count+=1
	if len(csv_files)==0:
		print("No .csv files were found.")
		print("Please place your .csv files into the current dir."+
			'\n'+abspath(curdir))
		input("Press ENTER to continue.")
	else:
		#ADD A BLANK SLOT FOR SKIPPING OPTIONS
		csv_files[csv_count]='None'
		for a in csv_files:
			for b in ['weapon','abilit','attribute','armor']:
				#print(b)
				if bool(re.search(b,csv_files[a],re.IGNORECASE)):
					if b=='weapon':
						weapons_path=csv_files[a]
						print("Weapons file: "+weapons_path)
					elif b=='abilit':
						abilities_path=csv_files[a]
						print("Abilities file: "+abilities_path)
					elif b=='attribute':
						attributes_path=csv_files[a]
						print("Attributes file: "+attributes_path)
					elif b=='armor':
						armors_path=csv_files[a]
						print("Armors file: "+armors_path)
		csv_paths=[weapons_path, abilities_path, attributes_path, armors_path]
		for a in range(0,len(csv_paths)):
			b=csv_paths[a]
			if b=='':
				if a==0:
					print("No file found for Weapons.")
					print("Select a file from the list below.")
					for c in csv_files:
						print(str(c)+": "+csv_files[c])
					file_select=number_select(len(csv_files))
					if file_select<len(csv_files):
						weapons_path=csv_files[file_select]
						print("File path stored.")
				elif a==1:
					print("No file found for Abilities.")
					print("Select a file from the list below.")
					for c in csv_files:
						print(str(c)+": "+csv_files[c])
					file_select=number_select(len(csv_files))
					if file_select<len(csv_files):
						abilities_path=csv_files[file_select]
						print("File path stored.")	
				elif a==2:
					print("No file found for Attributes.")
					print("Select a file from the list below.")
					for c in csv_files:
						print(str(c)+": "+csv_files[c])
					file_select=number_select(len(csv_files))
					if file_select<len(csv_files):
						attributes_path=csv_files[file_select]
						print("File path stored.")
				elif a==3:
					print("No file found for Armors.")
					print("Select a file from the list below.")
					for c in csv_files:
						print(str(c)+": "+csv_files[c])
					file_select=number_select(len(csv_files))
					if file_select<len(csv_files):
						armors_path=csv_files[file_select]
						print("File path stored.")
		print("All file paths found/entered. \nWould you like to change them?")
		if 'y'==yes_or_no():
			for a in range(0,len(csv_paths)):
				b=csv_paths[a]
				if a==0:
					print("Weapons file found.")
					print(b)
					print("Is this correct?")
					if 'n'==yes_or_no():
						print("Select a file from the list below.")
						for c in csv_files:
							print(str(c)+": "+csv_files[c])
						file_select=number_select(len(csv_files))
						if file_select<len(csv_files):
							weapons_path=csv_files[file_select]
							print("File path stored.")
						else:
							weapons_path=''
				elif a==1:
					print("Abilities file found.")
					print(b)
					print("Is this correct?")
					if 'n'==yes_or_no():
						print("Select a file from the list below.")
						for c in csv_files:
							print(str(c)+": "+csv_files[c])
						file_select=number_select(len(csv_files))
						if file_select<len(csv_files):
							abilities_path=csv_files[file_select]
							print("File path stored.")
						else:
							abilities_path=''
				elif a==2:
					print("Attributes file found.")
					print(b)
					print("Is this correct?")
					if 'n'==yes_or_no():
						print("Select a file from the list below.")
						for c in csv_files:
							print(str(c)+": "+csv_files[c])
						file_select=number_select(len(csv_files))
						if file_select<len(csv_files):
							attributes_path=csv_files[file_select]
							print("File path stored.")
						else:
							attributes_path=''
				elif a==3:
					print("Armors file found.")
					print(b)
					print("Is this correct?")
					if 'n'==yes_or_no():
						print("Select a file from the list below.")
						for c in csv_files:
							print(str(c)+": "+csv_files[c])
						file_select=number_select(len(csv_files))
						if file_select<len(csv_files):
							armors_path=csv_files[file_select]
							print("File path stored.")
						else:
							armors_path=''
	csv_paths=[weapons_path, abilities_path, attributes_path, armors_path]
	none_blank=True
	for a in csv_paths:
		if a=='':
			none_blank=False
	if none_blank:
		no_files=False
	else:
		print("1 or more files missing a path. \nTake this time to add files to directory.")
		input("Press ENTER to continue.")
weapon_file = open(weapons_path)
Abilities_file = open(abilities_path)
Attributes_file = open(attributes_path)
Armour_file = open(armors_path)
##Read CSV files
weapon_lines = csv.reader(weapon_file)
Abil_lines = csv.reader(Abilities_file)
Attr_lines = csv.reader(Attributes_file)
Armor_lines = csv.reader(Armour_file)
##Make lists from tables
armor = list(Armor_lines)
weapons = list(weapon_lines)
attributes = list(Attr_lines)
abilities = list(Abil_lines)
##Close files
weapon_file.close()
Abilities_file.close()
Attributes_file.close()
Armour_file.close()
######################################
##start by generating unique identifiers 
##for the weapons inventory and
##make a list skipping the first
unq_ident_weapons = list(range(1, len(weapons)))
unq_ident_armor = list(range(1, len(armor)))
used_items=equipped_items()
######################################
get_table_headers('weapons')
get_table_headers('armor')
get_table_headers('attributes')
get_table_headers('abilities')
get_characters()
store_armor_types()
######################################
char_list={}
for x in chars:
	if x == 1:
		char1 = player(chars[x], x)
		char_list[x]=char1
	elif x == 2:
		char2 =player(chars[x], x)
		char_list[x]=char2
	elif x == 3:
		char3 = player(chars[x], x)
		char_list[x]=char3
	elif x == 4:
		char4 = player(chars[x], x)
		char_list[x]=char4
###################################### END OF NECESSARY LINES
#print_table('char', 'none')
total_armor_count = len(helmets) + len(chest) + len(undergar) \
					+ len(waist) + len(boots) + len(gloves) + \
					len(amulets) + len(shields) + len(accessories)
print('Stored armor items: ' + str(total_armor_count) +
		'\n' + 'Total armor items: ' + str(len(unq_ident_armor)))
##########################

##########################
continue_program=True
while continue_program:
	continue_program=interface()
	print('\n')
#char1.calc_ratings()
#max_phys_damage(char1, 'slashing')
#max_elem_damage(char1, 'air')
#special_builds()
#print(weapon_headers)
#print(armor_headers)
#print(abil_headers)
#print(attr_headers)
