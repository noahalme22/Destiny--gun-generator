import random, heavy

class Machine(heavy.Heavy):
        def __init__(self):
                super().__init__("Machine Gun")

                self.machineGunList = []
                
                self.machineGunAttributes = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])
                
                for i in range(0,3):
                        self.machineGunList.append(random.choice(['Accurized Ballistics','Aggressive Ballistics','Armor Piercing Rounds','Crowd Control','CQB Ballistics','Feeding Frenzy','Fitted Stock','Field Choke','Field Scout','Focused Fire','Flared Magwell','Hand Loaded','Hammer Forged','Hand-Laid Stock','Hip Fire','Linear Compensator','Quickdraw','Perfect Balence','Persistance','Rangefinder','Rodeo','Smooth Ballistics','Single Point Sling','Smart Drift Control','Smallbore','Soft Ballistics','Spray and play','Surplus','Snapshot']))

                self.machine = random.choice(["ThunderLord","The Culling","Zombie Apocalypse WF47"])


        def __str__(self):
                return super().__str__()+"\nmachine gun: "+str(self.machine)+"\nattributes: "+str(self.machineGunAttributes)+"\nperks: "+str(self.machineGunList)+"\n"
