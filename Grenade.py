import heavy,random

class GrandeLauncher(heavy.Heavy):
        def __init__(self,grenadeLauncherList = "",grenadeLaucherAttributes = "", grenade = ""):
                super().__init__()



                self.grenade = grenade
                self.grenadeLauncherAttributes = grenadeLaucherAttributes
                self.grenadeLauncherList = grenadeLauncherList



                grenadeLauncherList = []
                if grenadeLaucherAttributes == "":
                        grenadeLaucherAttributes == random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])

                if grenadeLaucherList == "":
                        for i in range (0,3):
                      
                                grenadeLaucherList = random.choice(['Vacuum','Tripod','Third Eye','Surplus','Snapshot','Smart Drift Control','Single Point Sling','Quickdraw','Perfect Balence','Linear Compensator','Hard Launch','Flared Magwell','Fitted Stock','Field Scout','Army of One','Aggressive Launch'])

                if grenade == "":
                          grenade = random.choice(["Play of the game","the colony","I Am Alive"])


          
        def __str__(self):
                return super().__str__()+"\ngrenade: "+str(self.grenade)+"\nattributes: "+str(self.grenadeLaucherAttributes)+"\nlist: "+str(self.grenadeLauncherList)+"\n"
