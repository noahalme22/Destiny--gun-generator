import random, secondary

class Sidearm(secondary.Secondary):
        def __init__(self, sidearmList = "",sidearmAttributes = "",sidearm = ""):
                super().__init__()
                self.sidearm = sidearm
                self.sidearmAttributes = sidearmAttributes
                self.sidearmList = sidearmList


                sidearmList = []
                
                if sidearmAttributes == "":
                        
                      sidearm = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])

                if sidearmList == "":
                    for i in range (0,3):  
                        sidearmList = random.choice(['Battle Runner','crowd control','full auto','outlaw',
                                                            'quick draw','perfect balance','oiled frame','Send It','Single Point Sling'])

                if sidearm == "":
                      sidearm  = random.choice(["Wormwood","Tresspasser","Havoc Pigeon","Last Hope","The Last Dance","Rat King"])

        def __str__(self):
                return super().__str__()+"\nsidearm: "+str(self.sidearm)+"\nattributes: "+str(self.sidearmAttributes)+"\nlist: "+str(self.sidearmList)+"\n"
