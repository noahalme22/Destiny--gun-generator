import random,primary

class SMG(primary.primary):

        def __init__(self,smg == "",smgAttributes == "",smgList == ""):
        super().__init__():
        self.smg = smg
        self.smgAttributes = smgAttributes
        self.smgList = smgList

	if smg == "":
                smg = random.choice(["Antiope-D","Adjudicator","Risk Runner"])

        if smgAttributes == "":
                smgAttributes = random.choice(['precision frame','Lightweight Frame','Aggresive Frame','Adaptive Frame','High-Impact Frame','Rapid-Fire Frame'])

        smgList = []
        
        if smgList == "":
                for i in range (0,3):
                        smgRan = random.choice(['Army of One','Crowd Control','Hand loaded','Icarus','Lightweight','Quickdraw','Rangefinder','Return to Sender','Send it','Smallbore','Snapshot'])

        def __str__(self):
                return super().__str__()+"\nsmg: "+str(self.smg)+"\nsmgAttributes : "+str(self.smgAttributes)+"\nsmgList: "+str(self.smgList)+"\n"
