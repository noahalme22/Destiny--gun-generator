import random, secondary

class sidearm(secondary.secondary)
        def __init__(self, sidearmList = "",sidearmAttributes = "",sidearm = ""):
        super().__init__():

        self.sidearm = sidearm
        self.attributes = sidearmAttributes
        self.list = sidearmList


        sidearmList = []
        sidearmAttributes = []
        if sidearmAttributes = []
                
              sidearm = random.choice('precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame')

        if sidearmList = []
            for i in range (0,3):
              
                sidearmList = random.randint('Battle Runner','crowd control','full auto','outlaw',
                                                    'quick draw','perfect balance','oiled frame','Send It','Single Point Sling')

        if sidearm == "":
              sidearm  = random.choice(["Wormwood","Tresspasser","Havoc Pigeon","Last Hope","The Last Dance","Rat King"])

        def __str__(self):
                return super().__str__()+"\nsidearm: "+str(self.sidearm)+"\nattributes: "+str(self.sidearmAttributes)+"\nlist: "+str(self.sidearmList)+"\n"
