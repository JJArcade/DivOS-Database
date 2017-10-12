#import necessary libraries
import sys
import os.path
import sqlite3
import re

class divsqlite():
    
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
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
    
    #build accessory builds
    def get_boosts(self, accs_list):
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
                            print(insert_str)   #Debug line
                            self.curr.execute(insert_str)
            self.conn.commit()
        