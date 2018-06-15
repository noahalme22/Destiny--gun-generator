import random,primary


class ScoutRifle(primary.Primary):


        def __init__(self,scoutRifle = "",scoutList = "",scoutRifleAttributes = ""):
                super().__init__()
                self.scoutRifle = scoutRifle
                self.scoutRifleList = scoutRifleList
                self.scoutRifleAttributes = scoutRifleAttributes

                scoutRilfeList = []
                
                if scoutRilfeList == "":
                        for i in range (0,3):
                                scoutRifleRan = random.choice(['Armor Piercing Rounds','Army of One','Battle Runner','Braced Frame','Cascade','Crowd Control','Extended Mag','Fitted Stock','Field Scout','Focused Fire','Hand Loaded','Hammer Forged','Hand-Laid Stock','Hidden Hand','Hip Fire','Hot Swap','Injection Mold','Icarus','Lightweight','Outlaw','Quickdraw','Perfect Balence','Persistance','Rangefinder','Replenish','Single Point Sling','Smallbore','Spray and play','Snapshot','Third Eye'])

                        
                if scoutRifleAttributes == "":
                        autoRifleAttributes = random.choice(['precision frame','Lightweight Frame','Aggresive Frame','Adaptive Frame','High-Impact Frame','Rapid-Fire Frame'])         

                if scoutRifle == "":
                        scoutRifle = random.choice(["Mida Multi tool","Nameless Midnight","Jade Rabbit","the burning eye","BrayTech RWP MK. II","((CHAOS DOGMA~))"])

        def __str__(self):
                return super().__str__()+"\nscoutRifle: "+str(self.scoutRifle)+"\nscoutRifleAttributes : "+str(self.scoutRifleAttributes)+"\nscoutRifleList: "+str(self.autoRifleList)+"\n"
              
