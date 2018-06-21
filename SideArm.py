import random, secondary

class Sidearm(secondary.Secondary):
        def __init__(self):
                super().__init__("Sidearm")

                self.sidearmList = []
                        
                self.sidearmAttributes = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])

                
                for i in range (0,3):  
                        self.sidearmList.append(random.choice(['Battle Runner','crowd control','full auto','outlaw','quick draw','perfect balance','oiled frame','Send It','Single Point Sling']))

                self.sidearm = random.choice(["Wormwood","Tresspasser","Havoc Pigeon","Last Hope","The Last Dance","Rat King"])

        def __str__(self):
                return super().__str__()+"\nsidearm: "+str(self.sidearm)+"\nattributes: "+str(self.sidearmAttributes)+"\nperks: "+str(self.sidearmList)+"\n"
