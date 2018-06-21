import heavy,random

class Grenade(heavy.Heavy):
        def __init__(self):
                super().__init__("Grenade Launcher")

                self.grenadeLauncherList = []
                
                self.grenadeLauncherAttributes = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])

                for i in range (0,3):
                        self.grenadeLauncherList.append(random.choice(['Vacuum','Tripod','Third Eye','Surplus','Snapshot','Smart Drift Control','Single Point Sling','Quickdraw','Perfect Balence','Linear Compensator','Hard Launch','Flared Magwell','Fitted Stock','Field Scout','Army of One','Aggressive Launch']))

                self.grenade = random.choice(["Play of the game","the colony","I Am Alive","The wicked sister"])


          
        def __str__(self):
                return super().__str__()+"\ngrenade Launcher: "+str(self.grenade)+"\nattributes: "+str(self.grenadeLauncherAttributes)+"\nperks: "+str(self.grenadeLauncherList)+"\n"
