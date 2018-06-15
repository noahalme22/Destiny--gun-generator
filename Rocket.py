import random,heavy

class Rocket(heavy.Heavy):
        def __init__(self,rocketLauncherList = "",rocketLauncherAttributes = "", rocket = ""):
                super().__init__()

                self.rocket = rocket
                self.rocketLauncherAttributes = rocketLauncherAttributes
                self.rockerLauncherList = rocketLauncherList


                rocketLauncherList = []
                if rocketLauncherAttributes == "": 
                        rocket = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])



                if rocketLauncherList == "":
                        for i in range (0,3):
                                rocketLauncherList = random.choice(['Vacuum','Tripod','Third Eye','Surplus','Snapshot','Smart Drift Control','Single Point Sling','Quickdraw','Perfect Balence','Linear Compensator','Hard Launch','Flared Magwell','Fitted Stock','Field Scout','Army of One','Aggressive Launch'])
                if rocket == "":
                        rocket = random.choice(["Gjallarhorn","Dragons Breath","Suros JLB-47","Curtain Call","Warcliff coil","Sins Of The Past"])

        def __str__(self):
                return super().__str__()+"\nrocket: "+str(self.rocket)+"\nattributes: "+str(self.rocketLaucherAttributes)+"\nlist: "+str(self.rocketLauncherList)+"\n"
