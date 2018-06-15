import heavy,random

class Grenade(heavy.Heavy):
        def __init__(self,grenadeLauncherList = "",grenadeLauncherAttributes = "", grenade = ""):
                super().__init__()



                self.grenade = grenade
                self.grenadeLauncherAttributes = grenadeLauncherAttributes
                self.grenadeLauncherList = grenadeLauncherList



                grenadeLauncherList = []
                if grenadeLauncherAttributes == "":
                        grenadeLauncherAttributes = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])

                if grenadeLauncherList == "":
                        for i in range (0,3):
                      
                                grenadeLauncherList = random.choice(['Vacuum','Tripod','Third Eye','Surplus','Snapshot','Smart Drift Control','Single Point Sling','Quickdraw','Perfect Balence','Linear Compensator','Hard Launch','Flared Magwell','Fitted Stock','Field Scout','Army of One','Aggressive Launch'])

                if grenade == "":
                          grenade = random.choice(["Play of the game","the colony","I Am Alive"])


          
        def __str__(self):
                return super().__str__()+"\ngrenade: "+str(self.grenade)+"\nattributes: "+str(self.grenadeLaucherAttributes)+"\nlist: "+str(self.grenadeLauncherList)+"\n"
