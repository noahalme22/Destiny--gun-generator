import random,primary

class PulseRifle(primary.Primary):
        def __init__(self):
                super().__init__()

         
                
                

                self.pulseRifleAttributes = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])

                self.pulseRifle = random.choice(["Grasp of Malok","Blind Predicion","vigilance wing","nightshade","red death","Graviton Lance"])

                self.pulseRifleList = []

                for i in range (0,3):
                        self.pulseRifleList.append(random.choice(['Armor Piercing Rounds','Braced Frame','Custom Optics','Firefly','Full Auto','Headseeker','Hidden Hand','Lightweight','Quickdraw','Quickdraw IS','Perfect Balence','Ranged Lens RLS3','Ranged Lens RLS5','Rangefinder','Red Dot-OAS','Red Dot-ORES','Red Dot-ORS','Spray and play','Steady Hand IS']))



        def __str__(self):
                return super().__str__()+"\npulseRifle: "+str(self.pulseRifle)+"\npulseRifleAttributes : "+str(self.pulseRifleAttributes)+"\npulseRifleList: "+str(self.pulseRifleList)+"\n"
        


        
