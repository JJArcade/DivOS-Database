CREATE TRIGGER add_damages AFTER INSERT ON weapon_builds
BEGIN
UPDATE weapon_builds set Damagelo=(SELECT Damagelo from Weapon_damages where weapon_id=new.weapon) where weapon=new.weapon;
UPDATE weapon_builds set Element1=(SELECT Element1 from Weapon_damages where weapon_id=new.weapon) where weapon=new.weapon;
UPDATE weapon_builds set Element1DamageLo=(SELECT Element1Damagelo from Weapon_damages where weapon_id=new.weapon) where weapon=new.weapon;
UPDATE weapon_builds set Element2=(SELECT Element2 from Weapon_damages where weapon_id=new.weapon) where weapon=new.weapon;
UPDATE weapon_builds set Element2DamageLo=(SELECT Element2Damagelo from Weapon_damages where weapon_id=new.weapon) where weapon=new.weapon;
END;