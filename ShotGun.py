import random, secondary

class Shotgun(secondary.Secondary):
    def __init__(self):
        super().__init__("Shotgun")

        self.shotgunList = []

        self.shotgunAttributes = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])

        for i in range (0,3):
            self.shotgunList.append(random.choice(['Spray and play','Soft Ballistics','Smallbore','Smart Drift Control','Single Point Sling','Smooth Ballistics','Send It','Return to Sender','Replenish','Rangefinder','Linear Compensator','Full Auto','Final Round','Field Scout','Field Choke','Feeding Frenzy','CQB Ballistics','Crowd Control','Cascade','Braced Frame','Battle Runner','Army of One','Accurized Ballistics']))

        self.shotgun = random.choice(["Matador 64","Party Crasher +1","Universal Remote","Hawthorne's Field-Forged Shotgun","Gunnora's Axe","Legend of Acrius"])

    def __str__(self):
                return super().__str__()+"\nshotgun: "+str(self.shotgun)+"\nattributes: "+str(self.shotgunAttributes)+"\nperks: "+str(self.shotgunList)+"\n"
