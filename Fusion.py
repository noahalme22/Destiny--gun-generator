import random, secondary

class Fusion(secondary.Secondary):
        def __init__(self, fusionRifleList = "",fusionRifleAttributes = "",fusion = ""):
                super().__init__()

                self.fusion = fusion
                self.fusionRifleAttributes = fusionRifleAttributes
                self.fusionRifleList = fusionRifleList



                fusionRifleList = []
                
                if fusionRifleAttributes == "":
                        fusionRifleAttributes = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])

                if fusionRifleList == "":
                        for i in range (0,3):
                                fusionRifleList = random.choice(['Accelerated Coils','Braced Frame','Cascade','Extended Mag','Hip Fire','Quickdraw IS','Red Dot-OAS','Red Dot-ORES','Red Dot-ORS','Spray and play','Sureshot IS','Snapshot','TrueSight IS','Vacuum'])

                if fusion == "":
                        fusion  = random.choice(["Telesto","Merciless","Plan C","Saladins Vigil","Tarantula","Main Ingredient"])


        def __str__(self):
                return super().__str__()+"\nfusion: "+str(self.fusion)+"\nattributes: "+str(self.fusionRifleAttributes)+"\nlist: "+str(self.fusionRifleList)+"\n"
