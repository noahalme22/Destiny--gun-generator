import random, heavy

class MachineGun(heavy.Heavy):
        def __init__(self,machineGunList = "",machineGunAttributes = "" ,machine = ""):
                super().__init__()

                self.machine = machine
                self.machineGunAttributes = machineGunAttributes
                self.machineGunList = machineGunList


                
                if machineGunAttributes == "":
                        machineGunAttributes = random.choice('precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'

                machineGunList = []
                if machineGunList == "":
                        for i in range(0,3):
                                machineGunList = random.randint('Accurized Ballistics','Aggressive Ballistics','Armor Piercing Rounds','Crowd Control','CQB Ballistics','Feeding Frenzy',
                                                'Fitted Stock','Field Choke','Field Scout','Focused Fire','Flared Magwell','Hand Loaded','Hammer Forged','Hand-Laid Stock',
                                                   'Hip Fire','Linear Compensator','Quickdraw','Perfect Balence','Persistance',
                                                'Rangefinder','Rodeo','Smooth Ballistics','Single Point Sling','Smart Drift Control',
                                                'Smallbore','Soft Ballistics','Spray and play','Surplus','Snapshot')



                if machine == "":
                        machinee = random.choice(["ThunderLord","The Culling","Zombie Apocalypse WF47"])


        def __str__(self):
                return super().__str__()+"\nmachine: "+str(self.machine)+"\nattributes: "+str(self.machineGunAttributes)+"\nlist: "+str(self.machineGunList)+"\n"
