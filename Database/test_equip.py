from DivSqlite import divsqlite

x = divsqlite("..\\python3_scripts\\divos\\Database\\Div2.db")
testEquip=[[{"type":"Boots","id":"a123"},{"type":"Chest","id":"a115"}]]
x.equip(testEquip, "Rosa")
input("Press enter to unequip")
x.unequip_all("Rosa")
