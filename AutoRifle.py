import random,primary


class AutoRifle(primary.Primary):


        def __init__(self,autoRifle = "",autoRifleList = "",autoRifleAttributes = ""):
                super().__init__()
                self.autoRifle = autoRifle
                self.autoRifleList = autoRifleList
                self.autoRifleAttributes = autoRifleAttributes

                autoRilfeList = []
                
                if autoRilfeList == "":
                        for i in range (0,3):
                                autoRifleRan = random.choice(['Armor Piercing Rounds','Army of One','Battle Runner','Braced Frame','Cascade','Crowd Control','Extended Mag','Fitted Stock','Field Scout','Focused Fire','Hand Loaded','Hammer Forged','Hand-Laid Stock','Hidden Hand','Hip Fire','Hot Swap','Injection Mold','Icarus','Lightweight','Outlaw','Quickdraw','Perfect Balence','Persistance','Rangefinder','Replenish','Single Point Sling','Smallbore','Spray and play','Snapshot','Third Eye'])

                        
                if autoRifleAttributes == "":
                        autoRifleAttributes = random.choice(['precision frame','Lightweight Frame','Aggresive Frame','Adaptive Frame','High-Impact Frame','Rapid-Fire Frame'])         

                if autoRifle == "":
                        autoRifle = random.choice(["Uriels Gift","doctrine of passing","Monte Carlo","origin Story","Zhalo Supercell","Kibou AR3"])

        def __str__(self):
                return super().__str__()+"\nautoRifle: "+str(self.autoRifle)+"\nautoRifleAttributes : "+str(self.autoRifleAttributes)+"\nautoRifleList: "+str(self.autoRifleList)+"\n"
