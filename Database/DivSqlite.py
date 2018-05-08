#import necessary libraries
import sys
import os.path
import sqlite3
import re

class divsqlite():

    def __init__(self, database):
        failed = True
        try:
            self.conn = sqlite3.connect(database)
            failed = False
        except:
            print("Error connecting to database")
        if not failed:
            self.curr = self.conn.cursor()
            print("Database connected!")

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
        self.armor_set_name()

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
        #list_frequency = no_combos
        self.curr.execute("DELETE FROM armor_builds")
        self.curr.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME=\'armor_builds\'")
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

    #physical weapon builder
    def weapon_build(self, weap_type, character):
        reqs_get="SELECT requirement_name FROM weapon_main WHERE type=\'%s\' GROUP BY requirement_name" % weap_type
        print(reqs_get)    #DEBUG LINE
        self.curr.execute(reqs_get)
        weap_reqs = self.curr.fetchall()
        #GET CHAR equipement
        #weapons=[]
        self.curr.execute("DELETE FROM weapon_builds")
        self.curr.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME=\'weapon_builds\'")
        for a in weap_reqs:
            char_lvl_get="(SELECT %s FROM attributes WHERE name=\'%s\')" % (a[0], character)
            weap_get="SELECT weapon_id, hands FROM weapon_main WHERE type=\'%s\' AND requirement_name=\'%s\' AND requirement_level<=%s" % (weap_type, a[0], char_lvl_get)
            print(weap_get)    #DEBUG LINE
            self.curr.execute(weap_get)
            temp=self.curr.fetchall()
            for b in temp:
                insert_query="INSERT INTO weapon_builds (weapon) VALUES(\'%s\')" % b[0]
                print(insert_query)    #Debug line
                self.curr.execute(insert_query)
        self.conn.commit()

    #build permutations of accessories
    def accessory_builder(self):
        #get accessories
        self.curr.execute("SELECT accs_id FROM accessory_main WHERE type=\'Accessory\'")
        accs = self.curr.fetchall()
        #create temp table hold
        accs_singles=[]     #individual values
        for a in accs:
            accs_singles.append({"name": a[0], "Strength": 0, "Dexterity": 0, "Intelligence": 0})
        accs_perms = []     #combined values
        #get special values
        for a in range(0,len(accs_singles)):
            id = accs_singles[a]["name"]
            self.curr.execute("SELECT {0}1, {0}2, {0}3, {0}4 FROM accessory_specials where accs_id = '{1}'".format("special", id))
            specials = self.curr.fetchall()
            specials = specials[0]
            searches = ["Strength","Dexterity","Intelligence"]
            for b in specials:
                if b is not None:
                    for c in searches:
                        if bool(re.search(c, b, re.IGNORECASE)):
                            #find the plus symbol
                            plus_loc = re.search("\+", b)
                            attr = b[plus_loc.end()+1:]
                            lvl = int(b[:plus_loc.start()])
                            accs_singles[a][attr] += lvl
            print(accs_singles[a])    #debugline
        #make permutations
        for a in range(0,len(accs_singles)):
            print(accs_singles[a])
            for b in range(a+1,len(accs_singles)):
                #combine ids and buffs
                combo = [accs_singles[a]["name"], accs_singles[b]["name"]]
                new_str = accs_singles[a]["Strength"] + accs_singles[b]["Strength"]
                new_dex = accs_singles[a]["Dexterity"] + accs_singles[b]["Dexterity"]
                new_int = accs_singles[a]["Intelligence"] + accs_singles[b]["Intelligence"]
                accs_perms.append({"name": combo, "Strength": new_str, "Dexterity": new_dex, "Intelligence": new_int})
                print(accs_singles[b])
                print(accs_perms[len(accs_perms)-1])
        return accs_perms

    def armor_set_name(self):
        #prepare armor builds named table
        self.curr.execute("DROP TABLE IF EXISTS armor_builds_named")
        self.curr.execute("CREATE TABLE armor_builds_named AS SELECT * from armor_builds")

        #get sections
        self.curr.execute("PRAGMA table_info(armor_builds)")
        items = self.curr.fetchall()

        #go through the items
        for a in range(1,10):
            sel_str = "SELECT {0} FROM armor_builds GROUP BY {0}".format(items[a][1])
            self.curr.execute(sel_str)
            items_grouped = self.curr.fetchall()
            #go through the items
            for b in items_grouped:
                if b[0] == None:
                    break
                get_str = "SELECT name FROM armor_main WHERE armor_id = \'{0}\'".format(b[0])
                self.curr.execute(get_str)
                item_name = self.curr.fetchall()
                update_str = "UPDATE armor_builds_named SET {2} = \'{0}\' WHERE {2} = \'{1}\'".format(item_name[0][0],b[0],items[a][1])
                self.curr.execute(update_str)
        self.conn.commit()

    #build accessory builds
    def get_boosts(self):
            #get accs_ids for all
            self.curr.execute("SELECT accs_id FROM accessory_main WHERE type != \"Accessory\"")
            accs = self.curr.fetchall()
            #restructure into a dictionary
            for a in range(0,len(accs)):
                accs[a]={"name": accs[a][0], "Strength": 0, "Dexterity": 0, "Intelligence": 0}
            #get special values
            for a in range(0,len(accs)):
                #print(accs[a])     #debug line
                id = accs[a]["name"]
                self.curr.execute("SELECT {0}1, {0}2, {0}3, {0}4 FROM accessory_specials where accs_id = '{1}'".format("special", id))
                specials = self.curr.fetchall()
                specials = specials[0]
                searches = ["Strength","Dexterity","Intelligence"]
                for b in specials:
                    if b is not None:
                        for c in searches:
                            if bool(re.search(c, b, re.IGNORECASE)):
                                #find the plus symbol
                                plus_loc = re.search("\+", b)
                                attr = b[plus_loc.end()+1:]
                                lvl = int(b[:plus_loc.start()])
                                accs[a][attr] += lvl
            #make type holders
            waists = []
            under_gars = []
            amulets = []
            for a in accs:
                self.curr.execute("SELECT type FROM accessory_main WHERE accs_id = \"{0}\"".format(a["name"]))
                item_type = self.curr.fetchall()[0][0]
                #print(item_type)    #debug line
                if item_type == "Amulet":
                    amulets.append(a)
                elif item_type == "Undergarment":
                    under_gars.append(a)
                elif item_type == "Waist":
                    waists.append(a)
            #clear accessory builds table
            self.curr.execute("DELETE FROM accessory_builds")
            self.curr.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME=\'accessory_builds\'")
            #get accesorry permutations
            accs_list = self.accessory_builder()
            #make combos
            for a in waists:
                for b in under_gars:
                    for c in amulets:
                        for d in accs_list:
                            str_val = a["Strength"] + b["Strength"] + c["Strength"] + d["Strength"]
                            dex_val = a["Dexterity"] + b["Dexterity"] + c["Dexterity"] + d["Dexterity"]
                            int_val = a["Intelligence"]+b["Intelligence"]+c["Intelligence"]+d["Intelligence"]
                            insert_str = "INSERT INTO accessory_builds (waist, undergarment, amulet, accs_1, accs_2, strength, dexterity, intelligence) "
                            insert_str += "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(a["name"],b["name"],c["name"],d["name"][0],d["name"][1],str_val,dex_val,int_val)
                            #print(insert_str)   #Debug line
                            self.curr.execute(insert_str)
            self.conn.commit()

    #physical weapon builder
    def new_weapon_build(self, weap_type, character):
        #get the requirement name for the weapon type, typically only one required
        reqs_get="SELECT requirement_name FROM weapon_main WHERE type=\'%s\' GROUP BY requirement_name" % weap_type
        print(reqs_get)    #DEBUG LINE
        self.curr.execute(reqs_get)
        weap_reqs = self.curr.fetchall()
        weap_reqs2 = weap_reqs[0][0]
        #GET CHAR equipement
        #weapons=[]
        self.curr.execute("DELETE FROM weapon_builds")
        self.curr.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME=\'weapon_builds\'")
        char_lvl_get="(SELECT %s FROM attributes WHERE name=\'%s\')" % (weap_reqs[0][0], character)    #get the req level from the character
        #build weapon sets that don't require buffs to character attributes
        for a in weap_reqs:
            weap_get="SELECT weapon_id, hands FROM weapon_main WHERE type=\'%s\' AND requirement_name=\'%s\' AND requirement_level<=%s" % (weap_type, a[0], char_lvl_get)
            print(weap_get)
            self.curr.execute(weap_get)
            temp=self.curr.fetchall()
            for b in temp:
                insert_query="INSERT INTO weapon_builds (weapon) VALUES(\'%s\')" % b[0]
                print(insert_query)    #Debug line
                self.curr.execute(insert_query)
        #build accessory combos for attribute buffs
        self.get_boosts()
        #get weapons that need boosts
        sel_string = "SELECT weapon_id FROM weapon_main WHERE type = \"{0}\" AND requirement_level>{1}".format(weap_type,char_lvl_get)
        self.curr.execute(sel_string)
        buff_weaps = self.curr.fetchall()
        #weapon stat containers
        weap_deets = []
        for a in buff_weaps:
            current_weap = a[0]
            get_deets = "SELECT requirement_name, requirement_level FROM weapon_main WHERE weapon_id = \'{0}\'".\
                format(current_weap)
            print(get_deets)
            self.curr.execute(get_deets)
            deets = self.curr.fetchall()
            print(deets)
            curr_dict = {"name":current_weap, "req_name":deets[0][0], "req_level":deets[0][1]}
            print(curr_dict)
        self.conn.commit()  #save data

    #fetch data for armor table
    def get_armors(self):
        #GET TABLE INFO
        self.curr.execute("PRAGMA table_info(armor_builds)")
        rawInfo = self.curr.fetchall()
        columnNames=[]
        #GET COLUMN NAMES
        for a in rawInfo:
            columnNames.append(a[1])
        #order should be: set_id, helmet, chest, gloves, boots, waist
        #undergarment, amulet, accs1, accs2, armor_rating
        #FORMAT QUERY STRING
        queryString = ""
        for a in columnNames[1:]:
            if a == columnNames[len(columnNames)-1]:
                temp = "armor_builds.{0} ".format(a)
                queryString+=temp
            else:
                temp = "armor_builds.{0}, armor_builds_named.{0}, ".format(a)
                queryString+=temp
        queryString = "SELECT armor_builds.set_id, "+queryString
        queryString+="FROM armor_builds INNER JOIN armor_builds_named "
        queryString+="ON armor_builds.set_id = armor_builds_named.set_id "
        queryString+="ORDER BY armor_builds.armor_rating DESC"
        #print(queryString) #debugline
        #GET JOINED DATA
        self.curr.execute(queryString)
        allBuilds = self.curr.fetchall()
        #FORMAT INTO JSON/DICTIONARY
        fTable = []
        for a in allBuilds:
            temp ={}
            spots = [0,1,3,5,7,9,11,13,15,17,19]
            for b in range(0,len(columnNames)):
                if b!=0 and b!=10:
                    temp[columnNames[b]]={"id":a[spots[b]],"name":a[spots[b]+1]}
                else:
                    temp[columnNames[b]]=a[spots[b]]
            fTable.append(temp)
        #print(fTable[0])                #DEBUG LINE
        #print(fTable[len(fTable)-1])    #DEBUG LINE
        return fTable

    #equip a provided set
    def equip(self, set, character):   #set order should be [armors],[weapons],[accessories],[shields]
        for a in set:
            if len(a)>0:
                updateString = "UPDATE equipped SET %s=\"%s\""
                for b in a:
                    if b == a[0]:
                        updateString = updateString %(b["type"],b["id"])
                    elif b == a[len(a)-1]:
                        updateString += ", %s=\"%s\" " % (b["type"],b["id"])
                    else:
                        updateString += ", %s=\"%s\"" % (b["type"],b["id"])
                updateString += "WHERE Name=\"%s\"" % (character)
                self.curr.execute(updateString)
        self.conn.commit()

    #unequip everything from a character
    def unequip_all(self, character):
        self.curr.execute("PRAGMA table_info(equipped)")
        rawData = self.curr.fetchall()
        columns = []
        for a in rawData[1:]:
            columns.append(a[1])
        removeString = "UPDATE equipped SET "
        for a in columns:
            if a != columns[len(columns)-1]:
                removeString+="{0}={1}, ".format(a, "NULL")
            else:
                removeString+="{0}={1}".format(a, "NULL")
        removeString += " WHERE Name=\"%s\"" % (character)
        self.curr.execute(removeString)
        self.conn.commit()




#x = divsqlite("..\\python3_scripts\\divos\\Database\\Divinity.db")
#x.get_armors()
