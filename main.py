import PulseRifle as pr, HandCannonBackUp as hc, AutoRifle as ar, ScoutRifle as scr, SMG as smg, Sword as sw, Grenade as gr, Rocket as ro, Machine as ma, Sniper as sr, SideArm as sa,ShotGun as sg,Fusion as fr

import random

weaponList = []

weaponList.append(pr.PulseRifle ())
##print("Pulse rifle info:")
##print(weaponList[0].pulseRifle, weaponList[0].pulseRifleAttributes,weaponList[0].pulseRifleList)

weaponList.append(hc.HandCannon ())
##print("Handcannon info:")
##print(weaponList[1].handCannon, weaponList[1].hcAttributes,weaponList[1].hcList)

weaponList.append(ar.AutoRifle ())
##print("Auto rifle info:")
##print(weaponList[2].autoRifle, weaponList[2].autoRifleAttributes,weaponList[2].autoRifleList)

weaponList.append(scr.ScoutRifle ())
##print("Scout rifle info:")
##print(weaponList[3].scoutRifle, weaponList[3].scoutRifleAttributes,weaponList[3].scoutRifleList)

weaponList.append(smg.SMG ())
##print("SMG info:")
##print(weaponList[4].smg, weaponList[4].smgAttributes,weaponList[4].smgList)

weaponList.append(sw.Sword ())
##print("Sword info:")
##print(weaponList[5].sword, weaponList[5].swordAttributes)

weaponList.append(gr.Grenade ())
##print("Grenade launcher info:")
##print(weaponList[6].grenade, weaponList[6].grenadeLauncherAttributes,weaponList[6].grenadeLauncherList)

weaponList.append(ro.Rocket())
##print("Rocket launcher info:")
##print(weaponList[7].rocket, weaponList[7].rocketAttributes,weaponList[7].rocketLauncherList)

weaponList.append(ma.Machine())
##print("Machine gun info:")
##print(weaponList[8].machine, weaponList[8].machineGunAttributes,weaponList[8].machineGunList)

weaponList.append(sr.Sniper ())
##print("Sniper info:")
##print(weaponList[9].sniper, weaponList[9].sniperAttributes,weaponList[9].sniperList)

weaponList.append(sa.Sidearm ())
##print("Sidearm info:")
##print(weaponList[10].sidearm, weaponList[10].sidearmAttributes,weaponList[10].sidearmList)

weaponList.append(sg.Shotgun ())
##print("Shotgun info:")
##print(weaponList[11].shotgun, weaponList[11].shotgunAttributes,weaponList[11].shotgunList)

weaponList.append(fr.Fusion ())
##print("Fusion rifle info:")
##print(weaponList[12].fusion, weaponList[12].fusionRifleAttributes,weaponList[12].fusionRifleList)

print ("There are ",len(weaponList),"different weapon types in the inventory.")
x = random.randint(0,len(weaponList)-1)
print ("Your chosen weapon is| "+"\n", weaponList[x])



