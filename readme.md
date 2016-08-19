#Welcome to my Divinity Original Sin Inventory Manager and Armor Builder!

###Main Purpose:
This is a python project I started as a way to view and sort my equipable items in my Divinity Original Sin game. I was getting kinda frustrated by just equipping the newest items I got and having to jump from character to character to make sure they had the most optimal gear. So I combined my frustration with my desire to get better at coding and started working on a Python script that would read my excel spreadsheet of items and display them in a relational database format. I then soon realized that I could take my characters' attributes and abilities and write a code that would find the best armor combinations automatically. It's kinda grown from there.

###Key Features:
#####Displaying all your characters' info.
- example of character info display:
```
--------------------------------------------------------------
Wolgraff Attributes                    Abilities              Equipment
         Level                    12   Bow               0    Helmet: Item Name
         Strength                 7    Crossbow          0    Chest: Item Name
         Dexterity                7    Dual Wielding     2    Under: Item Name
         Intelligence             6    Single-handed     0    Waist: Item Name
         Constitution             6    Two-handed        0    Boots: Item Name
         Speed                    9    Wand              1    Gloves: Item Name
         Perception               7    Armour Specialist 1    Hand 1: Item Name
         ------------------------------Body Building     1    Hand 2: Item Name
         Ratings                       Shield Specialist 1    Amulet: Item Name
         Damage          0             Willpower         0    Access. 1: Item Name
         Armor Rating    0             Aerotheurge       0    Access. 2: Item Name
         Blocking        0             Expert Marksman   0
         Critical Chance 0             Geomancer         0
         Offense Rating  0             Hydrophist        1
         Defense Rating  0             Man-at-Arms       1
         Vitality        0             Pyrokinetic       0
         Action Points   0             Scoundrel         2
         Movement        0             Witchcraft        1
         ------------------------------Bartering         0
         Resistances                   Charisma          0
         Fire Res.             0%      Leadership        0
         Water Res.            0%      Lucky Charm       0
         Earth Res.            0%      Blacksmithing     0
         Air Res.              0%      Crafting          0
         Tenebrium Res.        0%      Loremaster        0
         Poison Res.           0%      Telekinesis       1
                                       Lockpicking       2
                                       Pickpocketing     2
--------------------------------------------------------------
```
- The information displayed should be familiar to anyone who's played **Divinity Original Sin**. The main interface of the program will display all character's information entered into your Attributes and Abilities CSV files here.
- Currently the program only supports the first 4 characters. It should be able to handle more fine but I've been testing it with my main party so I haven't tested the program with more than 4 characters at once. I'm not sure how many, if any, bugs would pop up from adding more.
- That being said it should be easy to fix and I will probably update it soon to allow a higher maximum characters displayed at once.
- After every action is completed, all characters' ratings will be calculated, or re-calculated depending on the action, and a new display will be printed with their updated values.
- As for the ratings information, right now only *Damage through Critical Chance* is actually calculated and updated.
  -The math behind some of D:OS's attributes was actually hard to find (ie Vitality, Offense/Defense Ratings, and Elemental Damage) so I opted to leave them out rather than give inaccurate data. *Apologies in advance if some of the values that are calculated don't match up with the actual game values.*
  
#####Armor Builds:
- One of the longest parts of the program in terms of calculating time.
- It shouldn't take more than a minute or 2 at worst, but it can essentially lock up if you're not careful.
  - When building an armor set with the highest possible **Armour Rating** for a selected character, the program takes all the armor pieces that have **Armour Rating** values and generates every possible unique configuration possible from them. (From the files provided there are 964,689 combinations from 168 total armor items.)
  - After every combination is generated, the program will assign and sort each set by the total **Armour Rating** of the armor set.
  - Then each set is checked to see if it can be equipped due to the item requirements and the character's attributes.
  - Sets that have requirements too high for the character are marked and the program will search for armor items that don't have **Armour Rating** values for any buffs to the selected character's attributes that might allow the set to be equipped.
  - Every unique combination of extra items is saved to the armor set
  - Sets that are equipable after this process are returned.
- As you can see from the process above it requires a lot of searching and data generation to find the best armor solutions for a character. If you choose too high a number of sets to pick from when prompted you can start a process that will take too long to compute and seem like the program is frozen.
  - Granted the amount of CPU and memory used in this program is minuscule compared to even your browser operation. So don't worry about your computer freezing. Just close the program and try again.
- Because this process can take a lot of time, there will be several prompts that can make the process shorter and insure an armor set is found matching your criteria.
- Note building an entire party's armor sets will be harder the more equipment that is in use. Since many combinations will only differ by a single item, the original amount of armor sets you chose to solve from in the beginning will decrease significantly if you don't want any conflicts with any items currently in use.

#####Maximize Damage:
- In the same way armor sets are built to maximize a character's **Armour Rating**, weapon sets can be built to get the weapon with the highest damage from selection made by the user for a specific Character.
- Weapon sets can be built for the 3 Physical damage types *(Crushing, Piercing and Slashing)* or the multiple Elemental types.
  - Physical sets can be filtered to remove or exclusively contain Bows, Crossbows, or Dual wielding combinations. 
- Elemental type damage weapons will have similar options but the main information page won't display the damage expected from the character for that weapon.

#####View Inventory:
- The instigator of this whole mess.
- You can view the full details of a single character's equipment, view all items currently in use by characters or view your inventory item in a table format.
- The table format will launch an interface just for viewing your inventory.
  - You must select whether you want to view your armor or weapons database.
    - Unfortunately I felt it would be too complicated to try and sort and display both the databases at once.
    - You may also notice the last for rows of data aren't in alignment. The special attributes of items can often be long and cause lines to continue to the next row breaking up the organization of the table. I opted to leave it unforamtted to save space since they are the least uniform data from item to item.
  - From there you can sort by any of the columns of the data base and chose to try and equip an item to a character.
    - I say try since the program does check a character's attributes and the requirements of an item before *equipping* it to a character. If the item's requirements are too high it won't be equipped.
  - You can also choose when you want to exit and go back to the main character info.

#####Inventory Searching
- You can search either your weapons or armor items for any search term you enter and opt to equip the results to any character you wish, barring requirements again.
- If you enter a term that matches an attribute, ability or resistance you will be prompted if you'd like to generate combinations from your items to maximize that particular value for a character.
- This is also an option under armor builds.
  - From there you'll be able to choose a build from scratch or from your character's open equipment slots.
  - This can help you take advantage of open equipment slots to squeeze the most out of your inventory.

#####Saving and Loading
- Lastly you can save your current party's equipment to a **.SAV** format or load from one.
- Please make sure to observe proper file naming conventions as there is no check in the program for invalid file names.
- Since this is my first time at tackling a Python script of any real consequence there may be some lingering bugs that cause the system to close out.
- If you are in the middle of an equipment build that's going well it's highly advisable to save it in case the program closes and you'll have to start from scratch.
- All save files are stored in the same folder of the program, and are loaded from there. So place any save files you have there or the program won't know they exist.


##DATA ENTRY
- The crux of this program lives and dies on how you enter your inventory into the .CSV files. 
  - If you aren't familiar with CSV formatting just open the Excel spreadsheet provided and overwrite the information there with your own. 
  - The biggest things to remember are **Keep the formatting of the cells as similar to mine as possible** to avoid any errors on reading the data. 
  - **_Apostrophe_**'s are a big No-go for the item names. 
    - Python can't print them out and you'll get errors when it tries to display them, so avoid at all costs. 
  - **USE "N/A" WHEN THERE IS NO VALUE FOR AN ITEM IN A PARTICULAR CATEGORY!**
    - The program looks for "N/A" (in caps too) to know that an item has no value there and adjusts accordingly during calculations
  - Keep capitalization in the item **Type** category.
    - Several functions in the program search for exact matches of item types so Capitalization and spelling count.
  - Another thing to look out for is Excel trying to convert the damage values to a date format.
    - The program specifically looks for the "-" to get the high and low damage values of a weapon.
  - For special buffs always start with the number value and then a *+/-* to signify if it adds or subtracts from a character's value.
    - ie "1+ Shield Specialist" "11% Poison Resistance" or "0.5- Movement"
- The simplest way to enter your inventory would be to add your items to the already filled out spreadsheet and let the spreadsheet program you use auto-fill when applicable and use those entries (ie Damage types, Armor Types, Special Buffs etc.)
- Once you have as many of your items in as you want, delete my inventory and leave only your items.
- Once you've done that for **Armor**, **Weapons**, **Character Attributes**, and **Character Abilities** you can save each sheet as a **.CSV** file and place it in the folder of the program.
- As long as you have "weapon", "armor", "attributes" and "abilities" in the file names, the program will be able to automatically find them.
  - The program will prompt you if you see the wrong file associated with each database however and you can add the proper files in at any time in which case the system will reload and search again before going into the main program.
- As you play the game you can keep track of inventory and character changes in the spreadsheet and save a new **.CSV** as necessary to update your database.

##Thanks
If you use the program I'd love any feed back. If the program closes out without you prompting it to, you probably encountered an error. Feel free to leave an issues you have here and if I have some free time I'll be sure to look into a possible fix for it. And if you are some one familiar with coding yourself, feel free to branch this git and adjust it to your liking. Thanks and have fun Source Hunters.
