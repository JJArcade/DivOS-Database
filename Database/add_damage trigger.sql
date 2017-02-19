CREATE TRIGGER add_damagelo AFTER INSERT ON temp_weapons
BEGIN
UPDATE temp_weapons set Damagelo=(SELECT Damagelo from Weapon_damages where weapon_id=new.weapon) where weapon=new.weapon;
UPDATE temp_weapons set Element1=(SELECT Element1 from Weapon_damages where weapon_id=new.weapon) where weapon=new.weapon;
UPDATE temp_weapons set Element1DamageLo=(SELECT Element1Damagelo from Weapon_damages where weapon_id=new.weapon) where weapon=new.weapon;
UPDATE temp_weapons set Element2=(SELECT Element2 from Weapon_damages where weapon_id=new.weapon) where weapon=new.weapon;
UPDATE temp_weapons set Element2DamageLo=(SELECT Element2Damagelo from Weapon_damages where weapon_id=new.weapon) where weapon=new.weapon;
END;