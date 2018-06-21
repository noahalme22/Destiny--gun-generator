import random,heavy

class Rocket(heavy.Heavy):
        def __init__(self):
                super().__init__("Rocket Launcher")

                self.rocketLauncherList = []
                 
                self.rocketAttributes = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])

                for i in range (0,3):
                        self.rocketLauncherList.append(random.choice(['Vacuum','Tripod','Third Eye','Surplus','Snapshot','Smart Drift Control','Single Point Sling','Quickdraw','Perfect Balence','Linear Compensator','Hard Launch','Flared Magwell','Fitted Stock','Field Scout','Army of One','Aggressive Launch']))
                
                self.rocket = random.choice(["Gjallarhorn","Dragons Breath","Suros JLB-47","Curtain Call","Warcliff coil","Sins Of The Past"])

        def __str__(self):
                return super().__str__()+"\nrocket launcher: "+str(self.rocket)+"\nattributes: "+str(self.rocketAttributes)+"\nperks: "+str(self.rocketLauncherList)+"\n"
