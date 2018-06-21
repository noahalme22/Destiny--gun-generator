import random,primary


class AutoRifle(primary.Primary):
        def __init__(self):
                super().__init__("Autorifle")

                self.autoRifleList = []
                

                for i in range (0,3):
                        self.autoRifleList.append(random.choice(['Armor Piercing Rounds','Army of One','Battle Runner','Braced Frame','Cascade','Crowd Control','Extended Mag','Fitted Stock','Field Scout','Focused Fire','Hand Loaded','Hammer Forged','Hand-Laid Stock','Hidden Hand','Hip Fire','Hot Swap','Injection Mold',\
                                                                 'Icarus','Lightweight','Outlaw','Quickdraw','Perfect Balence','Persistance','Rangefinder','Replenish','Single Point Sling','Smallbore','Spray and play','Snapshot','Third Eye']))
                                
                        

                self.autoRifleAttributes = random.choice(['precision frame','Lightweight Frame','Aggresive Frame','Adaptive Frame','High-Impact Frame','Rapid-Fire Frame'])         
                       


                self.autoRifle = random.choice(["Uriels Gift","doctrine of passing","Monte Carlo","origin Story","Zhalo Supercell","Kibou AR3"])
                      


        def __str__(self):
                return super().__str__()+"\nautoRifle: "+str(self.autoRifle)+"\nAttributes : "+str(self.autoRifleAttributes)+"\nperks: "+str(self.autoRifleList)+"\n"
