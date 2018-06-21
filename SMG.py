import random,primary

class SMG(primary.Primary):

        def __init__(self):
                super().__init__("SMG")

                
                self.smg = random.choice(["Antiope-D","Adjudicator","Risk Runner"])

                
                self.smgAttributes = random.choice(['precision frame','Lightweight Frame','Aggresive Frame','Adaptive Frame','High-Impact Frame','Rapid-Fire Frame'])

                self.smgList = []
                
                
                for i in range (0,3):
                        self.smgList.append(random.choice(['Army of One','Crowd Control','Hand loaded','Icarus','Lightweight','Quickdraw','Rangefinder','Return to Sender','Send it','Smallbore','Snapshot']))

        def __str__(self):
                return super().__str__()+"\nsmg: "+str(self.smg)+"\nAttributes : "+str(self.smgAttributes)+"\nperks: "+str(self.smgList)+"\n"
