import random, secondary

class Fusion(secondary.Secondary):
        def __init__(self):
                super().__init__("fusion")

                self.fusionRifleList = []
                
                self.fusionRifleAttributes = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])

                for i in range (0,3):
                        self.fusionRifleList.append(random.choice(['Accelerated Coils','Braced Frame','Cascade','Extended Mag','Hip Fire','Quickdraw IS','Red Dot-OAS','Red Dot-ORES','Red Dot-ORS','Spray and play',\
                                                                    'Sureshot IS','Snapshot','TrueSight IS','Vacuum']))
                        
                self.fusion  = random.choice(["Telesto","Merciless","Plan C","Saladins Vigil","Tarantula","Main Ingredient"])


        def __str__(self):
                return super().__str__()+"\nfusion rifle: "+str(self.fusion)+"\nattributes: "+str(self.fusionRifleAttributes)+"\nperks: "+str(self.fusionRifleList)+"\n"
