import PulseRifle as pr, HandCannonBackUp as hc, AutoRifle as ar, ScoutRifle as scr, SMG as smg, Sword as sw, Grenade as gr, Rocket as ro, Machine as ma, Sniper as sr, SideArm as sa,ShotGun as sg,Fusion as fr



weaponList = []


weaponList.append(pr.PulseRifle ())
print("pulse rifle info:")
print(weaponList[0].pulseRifle, weaponList[0].pulseRifleAttributes,weaponList[0].pulseRifleList)
weaponList.append(hc.HandCannon ())
print("Handcannon info:")
print(weaponList[1].handCannon, weaponList[1].hcAttributes,weaponList[1].hcList)
weaponList.append(ar.AutoRifle ())
weaponList.append(scr.ScoutRifle ())
weaponList.append(smg.SMG ())
weaponList.append(sw.Sword ())
weaponList.append(gr.Grenade ())
weaponList.append(ro.Rocket())
weaponList.append(ma.Machine())
weaponList.append(sr.Sniper ())
weaponList.append(sa.Sidearm ())
weaponList.append(sg.Shotgun ())
weaponList.append(fr.Fusion ())


#print ("This is your List: ",weaponList)


