import random,primary


class ScoutRifle(primary.Primary):
        def __init__(self):
                super().__init__("Scoutrifle")

                self.scoutRifleList = []
                             
                for i in range (0,3):
                        self.scoutRifleList.append(random.choice(['Armor Piercing Rounds','Army of One','Battle Runner','Braced Frame','Cascade','Crowd Control','Extended Mag','Fitted Stock','Field Scout','Focused Fire','Hand Loaded','Hammer Forged','Hand-Laid Stock','Hidden Hand','Hip Fire','Hot Swap','Injection Mold','Icarus','Lightweight','Outlaw','Quickdraw','Perfect Balence','Persistance','Rangefinder','Replenish','Single Point Sling','Smallbore','Spray and play','Snapshot','Third Eye']))
                     
                self.scoutRifleAttributes = random.choice(['precision frame','Lightweight Frame','Aggresive Frame','Adaptive Frame','High-Impact Frame','Rapid-Fire Frame'])         

                self.scoutRifle = random.choice(["Mida Multi tool","Nameless Midnight","Jade Rabbit","the burning eye","BrayTech RWP MK. II","((CHAOS DOGMA~))"])

        def __str__(self):
                return super().__str__()+"\nscoutRifle: "+str(self.scoutRifle)+"\nAttributes : "+str(self.scoutRifleAttributes)+"\nperks: "+str(self.scoutRifleList)+"\n"
