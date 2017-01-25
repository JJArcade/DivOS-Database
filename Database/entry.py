Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> sqlite3.connect("D:\\GitHub\\MyRepos\\DivOS-Database\\Database\\Divinity.db")
<sqlite3.Connection object at 0x0000000002D74730>
>>> conn = sqlite3.connect("D:\\GitHub\\MyRepos\\DivOS-Database\\Database\\Divinity.db")
>>> curr = conn.cursor()
>>> import csv
\
>>> weapons_file = "D:\\GitHub\\MyRepos\\DivOS-Database\\Database\\just_weapons.csv"
>>> weapons_path=weapons_path
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    weapons_path=weapons_path
NameError: name 'weapons_path' is not defined
>>> weapons_path=weapons_file
>>> weapons_file=open(weapons_path)
>>> weapons_csv=csv.reader(weapons_file)
>>> weapons=list(weapons_csv)
>>> weapons[0]
['w1', '53', '68', '220', '0', '0', '0', '0', 'Outdated Executioners Sword', 'Slashing', '2', '0', '0', '0', 'Common', '117', 'Str 7', '4', '4', '0', '0', '0', '0', '0']
>>> fields=curr.execute("PRAGMA table_info(table_name)")
>>> fields
<sqlite3.Cursor object at 0x000000000394A570>
>>> fields=curr.fetchall()
>>> fields
[]
>>> fields=curr.execute("PRAGMA table_info(Weapons)")
>>> fields
<sqlite3.Cursor object at 0x000000000394A570>
>>> fields=curr.fetchall()
>>> fields
[(0, 'weapon_id', 'TEXT', 1, None, 1), (1, 'DamageLo', 'INTEGER', 0, None, 0), (2, 'DamageHi', 'INTEGER', 0, None, 0), (3, 'CriticalDamage', 'INTEGER', 0, None, 0), (4, 'Element1DamageLo', 'INTEGER', 0, None, 0), (5, 'Element1DamageHi', 'INTEGER', 0, None, 0), (6, 'Element2DamageLo', 'INTEGER', 0, None, 0), (7, 'Element2DamageHi', 'INTEGER', 0, None, 0), (8, 'ItemName', 'TEXT', 1, None, 0), (9, 'Type', 'TEXT', 0, None, 0), (10, 'Hands', 'INTEGER', 1, None, 0), (11, 'CriticalChance', 'INTEGER', 0, None, 0), (12, 'Element1', 'TEXT', 0, None, 0), (13, 'Element2', 'TEXT', 0, None, 0), (14, 'Rarity', 'INTEGER', 1, None, 0), (15, 'Value', 'INTEGER', 1, None, 0), (16, 'Requirements', 'TEXT', 0, None, 0), (17, 'Level', 'INTEGER', 1, None, 0), (18, 'Range', 'REAL', 0, None, 0), (19, 'Special1', 'TEXT', 0, None, 0), (20, 'Special2', 'TEXT', 0, None, 0), (21, 'Special3', 'TEXT', 0, None, 0), (22, 'Special4', 'TEXT', 0, None, 0)]
>>> fields[0]
(0, 'weapon_id', 'TEXT', 1, None, 1)
>>> fields_raw=fields
>>> for x in fields_raw:
	print(x[1])

	
weapon_id
DamageLo
DamageHi
CriticalDamage
Element1DamageLo
Element1DamageHi
Element2DamageLo
Element2DamageHi
ItemName
Type
Hands
CriticalChance
Element1
Element2
Rarity
Value
Requirements
Level
Range
Special1
Special2
Special3
Special4
>>> type(fields_raw[0][1])
<class 'str'>
>>> fields=[]
>>> fields_raw
[(0, 'weapon_id', 'TEXT', 1, None, 1), (1, 'DamageLo', 'INTEGER', 0, None, 0), (2, 'DamageHi', 'INTEGER', 0, None, 0), (3, 'CriticalDamage', 'INTEGER', 0, None, 0), (4, 'Element1DamageLo', 'INTEGER', 0, None, 0), (5, 'Element1DamageHi', 'INTEGER', 0, None, 0), (6, 'Element2DamageLo', 'INTEGER', 0, None, 0), (7, 'Element2DamageHi', 'INTEGER', 0, None, 0), (8, 'ItemName', 'TEXT', 1, None, 0), (9, 'Type', 'TEXT', 0, None, 0), (10, 'Hands', 'INTEGER', 1, None, 0), (11, 'CriticalChance', 'INTEGER', 0, None, 0), (12, 'Element1', 'TEXT', 0, None, 0), (13, 'Element2', 'TEXT', 0, None, 0), (14, 'Rarity', 'INTEGER', 1, None, 0), (15, 'Value', 'INTEGER', 1, None, 0), (16, 'Requirements', 'TEXT', 0, None, 0), (17, 'Level', 'INTEGER', 1, None, 0), (18, 'Range', 'REAL', 0, None, 0), (19, 'Special1', 'TEXT', 0, None, 0), (20, 'Special2', 'TEXT', 0, None, 0), (21, 'Special3', 'TEXT', 0, None, 0), (22, 'Special4', 'TEXT', 0, None, 0)]
>>> for x in fields_raw:
	fields.append(x[1])

	
>>> fields
['weapon_id', 'DamageLo', 'DamageHi', 'CriticalDamage', 'Element1DamageLo', 'Element1DamageHi', 'Element2DamageLo', 'Element2DamageHi', 'ItemName', 'Type', 'Hands', 'CriticalChance', 'Element1', 'Element2', 'Rarity', 'Value', 'Requirements', 'Level', 'Range', 'Special1', 'Special2', 'Special3', 'Special4']
>>> fields[0]
'weapon_id'
>>> insert_pt1=""
>>> inset_pt1="Insert into weapons("
>>> for x in fields:
	if x!="Special4":
		inset_pt1+=x+','
	else:
		inset_pt1+=x+')'

		
>>> insert_pt1=inset_pt1
>>> insert_pt1
'Insert into weapons(weapon_id,DamageLo,DamageHi,CriticalDamage,Element1DamageLo,Element1DamageHi,Element2DamageLo,Element2DamageHi,ItemName,Type,Hands,CriticalChance,Element1,Element2,Rarity,Value,Requirements,Level,Range,Special1,Special2,Special3,Special4)'
>>> insert_pt2 = " Values("
>>> fields_test=fields_raw[0]
>>> fields_test
(0, 'weapon_id', 'TEXT', 1, None, 1)
>>> weapon_test=weapons[0]
>>> weapon_test
['w1', '53', '68', '220', '0', '0', '0', '0', 'Outdated Executioners Sword', 'Slashing', '2', '0', '0', '0', 'Common', '117', 'Str 7', '4', '4', '0', '0', '0', '0', '0']
>>> fields_type=[]
>>> for x in fields_raw:
	fields_type.append(x[2])

	
>>> fields_type
['TEXT', 'INTEGER', 'INTEGER', 'INTEGER', 'INTEGER', 'INTEGER', 'INTEGER', 'INTEGER', 'TEXT', 'TEXT', 'INTEGER', 'INTEGER', 'TEXT', 'TEXT', 'INTEGER', 'INTEGER', 'TEXT', 'INTEGER', 'REAL', 'TEXT', 'TEXT', 'TEXT', 'TEXT']
>>> for a in range(0,len(fields)):
	if fields_type[a]=='TEXT':
		if weapon_test[a]!=0:
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+="',"
			else:
				insert_pt2+="')"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
	else:
		if weapon_test[a]!=0:
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"

				
>>> insert_pt2
" Values('w1','53,'68,'220,'0,'0,'0,'0,'Outdated Executioners Sword','Slashing','2,'0,'0','0','Common,'117,'Str 7','4,'4,'0','0','0','0')"
>>> inset_pt1="Insert into weapons("
>>> insert_pt2 = " Values("
>>> insert_pt1
'Insert into weapons(weapon_id,DamageLo,DamageHi,CriticalDamage,Element1DamageLo,Element1DamageHi,Element2DamageLo,Element2DamageHi,ItemName,Type,Hands,CriticalChance,Element1,Element2,Rarity,Value,Requirements,Level,Range,Special1,Special2,Special3,Special4)'
>>> for a in range(0,len(fields)):
	if fields_type[a]=='TEXT':
		if weapon_test[a]!=0:
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+="',"
			else:
				insert_pt2+="')"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
	else:
		if weapon_test[a]!=0:
			insert_pt2+=weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"

				
>>> insert_pt2
" Values('w1',53,68,220,0,0,0,0,'Outdated Executioners Sword','Slashing',2,0,'0','0',Common,117,'Str 7',4,4,'0','0','0','0')"
>>> insert_pt2 = " Values("
>>> for a in range(0,len(fields)):
	if fields_type[a]=='TEXT':
		if weapon_test[a]!='0':
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+="',"
			else:
				insert_pt2+="')"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
	else:
		if weapon_test[a]!=0:
			insert_pt2+=weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"

				
>>> insert_pt2
" Values('w1',53,68,220,0,0,0,0,'Outdated Executioners Sword','Slashing',2,0,None,None,Common,117,'Str 7',4,4,None,None,None,None)"
>>> insert_pt2 = " Values("
>>> for a in range(0,len(fields)):
	if fields_type[a]=='TEXT':
		if weapon_test[a]!='0':
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+="',"
			else:
				insert_pt2+="')"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
	else:
		if weapon_test[a]!='0':
			insert_pt2+=weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"

				
>>> insert_pt2
" Values('w1',53,68,220,None,None,None,None,'Outdated Executioners Sword','Slashing',2,None,None,None,Common,117,'Str 7',4,4,None,None,None,None)"
>>> inert_pt1+insert_pt2
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    inert_pt1+insert_pt2
NameError: name 'inert_pt1' is not defined
>>> insert_pt1+insert_pt2
"Insert into weapons(weapon_id,DamageLo,DamageHi,CriticalDamage,Element1DamageLo,Element1DamageHi,Element2DamageLo,Element2DamageHi,ItemName,Type,Hands,CriticalChance,Element1,Element2,Rarity,Value,Requirements,Level,Range,Special1,Special2,Special3,Special4) Values('w1',53,68,220,None,None,None,None,'Outdated Executioners Sword','Slashing',2,None,None,None,Common,117,'Str 7',4,4,None,None,None,None)"
>>> curr.execute(insert_pt1+insert_pt2)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    curr.execute(insert_pt1+insert_pt2)
sqlite3.OperationalError: no such column: None
>>> insert_pt2 = " Values ("
>>> insert_pt1ALT="INSERT INTO Weapons"
>>> for a in range(0,len(fields)):
	if fields_type[a]=='TEXT':
		if weapon_test[a]!='0':
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+="',"
			else:
				insert_pt2+="')"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
	else:
		if weapon_test[a]!='0':
			insert_pt2+=weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"

				
>>> print(insert_pt2)
 Values ('w1',53,68,220,None,None,None,None,'Outdated Executioners Sword','Slashing',2,None,None,None,Common,117,'Str 7',4,4,None,None,None,None)
>>> curr.execute(insert_pt1ALT+insert_pt2)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    curr.execute(insert_pt1ALT+insert_pt2)
sqlite3.OperationalError: no such column: None
>>> insert_pt1ALT+insert_pt2
"INSERT INTO Weapons Values ('w1',53,68,220,None,None,None,None,'Outdated Executioners Sword','Slashing',2,None,None,None,Common,117,'Str 7',4,4,None,None,None,None)"
>>> insert_pt2 = " Values ("
>>> for a in range(0,len(fields)):
	if fields_type[a]=='TEXT':
		if weapon_test[a]!='0':
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+="',"
			else:
				insert_pt2+="')"
		else:
			insert_pt2+=None
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
	else:
		if weapon_test[a]!='0':
			insert_pt2+=weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
		else:
			insert_pt2+=None
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"

				
Traceback (most recent call last):
  File "<pyshell#95>", line 23, in <module>
    insert_pt2+=None
TypeError: Can't convert 'NoneType' object to str implicitly
>>> field_names
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    field_names
NameError: name 'field_names' is not defined
>>> fields
['weapon_id', 'DamageLo', 'DamageHi', 'CriticalDamage', 'Element1DamageLo', 'Element1DamageHi', 'Element2DamageLo', 'Element2DamageHi', 'ItemName', 'Type', 'Hands', 'CriticalChance', 'Element1', 'Element2', 'Rarity', 'Value', 'Requirements', 'Level', 'Range', 'Special1', 'Special2', 'Special3', 'Special4']
>>> fields_raw
[(0, 'weapon_id', 'TEXT', 1, None, 1), (1, 'DamageLo', 'INTEGER', 0, None, 0), (2, 'DamageHi', 'INTEGER', 0, None, 0), (3, 'CriticalDamage', 'INTEGER', 0, None, 0), (4, 'Element1DamageLo', 'INTEGER', 0, None, 0), (5, 'Element1DamageHi', 'INTEGER', 0, None, 0), (6, 'Element2DamageLo', 'INTEGER', 0, None, 0), (7, 'Element2DamageHi', 'INTEGER', 0, None, 0), (8, 'ItemName', 'TEXT', 1, None, 0), (9, 'Type', 'TEXT', 0, None, 0), (10, 'Hands', 'INTEGER', 1, None, 0), (11, 'CriticalChance', 'INTEGER', 0, None, 0), (12, 'Element1', 'TEXT', 0, None, 0), (13, 'Element2', 'TEXT', 0, None, 0), (14, 'Rarity', 'INTEGER', 1, None, 0), (15, 'Value', 'INTEGER', 1, None, 0), (16, 'Requirements', 'TEXT', 0, None, 0), (17, 'Level', 'INTEGER', 1, None, 0), (18, 'Range', 'REAL', 0, None, 0), (19, 'Special1', 'TEXT', 0, None, 0), (20, 'Special2', 'TEXT', 0, None, 0), (21, 'Special3', 'TEXT', 0, None, 0), (22, 'Special4', 'TEXT', 0, None, 0)]
>>> for x in range(0,len(fields_raw)):
	if fields_raw[x][1]=="Rarity":
		print(x)

		
14
>>> fields[14]
'Rarity'
>>> fields_type[14]
'INTEGER'
>>> fields_type[14]='TEXT'
>>> fields_type[14]
'TEXT'
>>> insert_pt2 = " Values ("
>>> for a in range(0,len(fields)):
	if fields_type[a]=='TEXT':
		if weapon_test[a]!='0':
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+="',"
			else:
				insert_pt2+="')"
		else:
			insert_pt2+=None
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
	else:
		if weapon_test[a]!='0':
			insert_pt2+=weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
		else:
			insert_pt2+=None
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"

				
Traceback (most recent call last):
  File "<pyshell#109>", line 23, in <module>
    insert_pt2+=None
TypeError: Can't convert 'NoneType' object to str implicitly
>>> for a in range(0,len(fields)):
	if fields_type[a]=='TEXT':
		if weapon_test[a]!='0':
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+="',"
			else:
				insert_pt2+="')"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
	else:
		if weapon_test[a]!='0':
			insert_pt2+=weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
		else:
			insert_pt2+=str(None)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"

				
>>> insert_pt2
" Values ('w1',53,68,220,'w1',53,68,220,None,None,None,None,'Outdated Executioners Sword','Slashing',2,None,None,None,'Common',117,'Str 7',4,4,None,None,None,None)"
>>> curr.execute("insert into weapons"+insert_pt2)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    curr.execute("insert into weapons"+insert_pt2)
sqlite3.OperationalError: no such column: None
>>> insert_pt2 = " Values ("
>>> for a in range(0,len(fields)):
	if fields_type[a]=='TEXT':
		if weapon_test[a]!='0':
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+="',"
			else:
				insert_pt2+="')"
		else:
			insert_pt2+=str(NULL)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
	else:
		if weapon_test[a]!='0':
			insert_pt2+=weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
		else:
			insert_pt2+=str(NULL)
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"

				
Traceback (most recent call last):
  File "<pyshell#116>", line 23, in <module>
    insert_pt2+=str(NULL)
NameError: name 'NULL' is not defined
>>> for a in range(0,len(fields)):
	if fields_type[a]=='TEXT':
		if weapon_test[a]!='0':
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+="',"
			else:
				insert_pt2+="')"
		else:
			insert_pt2+='NULL'
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
	else:
		if weapon_test[a]!='0':
			insert_pt2+=weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
		else:
			insert_pt2+='NULL'
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"

				
>>> insert_pt2 = " Values ("
>>> for a in range(0,len(fields)):
	if fields_type[a]=='TEXT':
		if weapon_test[a]!='0':
			insert_pt2+="'"+weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+="',"
			else:
				insert_pt2+="')"
		else:
			insert_pt2+='NULL'
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
	else:
		if weapon_test[a]!='0':
			insert_pt2+=weapon_test[a]
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"
		else:
			insert_pt2+='NULL'
			if a<len(fields)-1:
				insert_pt2+=","
			else:
				insert_pt2+=")"

				
>>> insert_pt2
" Values ('w1',53,68,220,NULL,NULL,NULL,NULL,'Outdated Executioners Sword','Slashing',2,NULL,NULL,NULL,'Common',117,'Str 7',4,4,NULL,NULL,NULL,NULL)"
>>> curr.execute("insert into weapons"+insert_pt2)
<sqlite3.Cursor object at 0x000000000394A570>
>>> curr.commit()
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    curr.commit()
AttributeError: 'sqlite3.Cursor' object has no attribute 'commit'
>>> conn.commit()
>>> for a in range(1,len(weapons)):
	print(weapons[a][0])

	
w2
w3
w4
w5
w6
w7
w8
w9
w10
w11
w12
w13
w14
w15
w16
w17
w18
w19
w20
w21
w22
w23
w24
w25
w26
w27
w28
w29
w30
w31
w32
w33
w34
w35
w36
w37
w38
w39
w40
w41
w42
w43
w44
w45
w46
w47
w48
w49
w50
w51
w52
w53
w54
w55
w56
w57
w58
w59
w60
w61
w62
w63
w64
w65
w66
w67
w68
w69
w70
w71
w72
w73
w74
w75
w76
w77
w78
w79
w80
w81
w82
w83
w84
w85
w86
w87
w88
w89
w90
w91
w92
w93
w94
w95
w96
w97
w98
w99
w100
>>> for x in range(1,len(weapons)):
	insert_pt2 = " Values ("
	for a in range(0,len(fields)):
		if fields_type[a]=='TEXT':
			if weapons[x][a]!='0':
				insert_pt2+="'"+weapons[x][a]
				if a<len(fields)-1:
					insert_pt2+="',"
				else:
					insert_pt2+="')"
			else:
				insert_pt2+='NULL'
				if a<len(fields)-1:
					insert_pt2+=","
				else:
					insert_pt2+=")"
		else:
			if weapons[x][a]!='0':
				insert_pt2+=weapons[x][a]
				if a<len(fields)-1:
					insert_pt2+=","
				else:
					insert_pt2+=")"
			else:
				insert_pt2+='NULL'
				if a<len(fields)-1:
					insert_pt2+=","
				else:
					insert_pt2+=")"
	curr.execute("insert into weapons"+insert_pt2)

	
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
<sqlite3.Cursor object at 0x000000000394A570>
>>> conn.commit()
>>> 
