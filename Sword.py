import random,heavy

class Sword(heavy.Heavy):
        def __init__(self):
                super().__init__("Sword")
                
                self.swordAttributes = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])
                
                self.sword = random.choice(["Raze-Lighter","Dark-Drinker","The Young Wolfs Howl","Worldline Zero"])

        def __str__(self):
                return super().__str__()+"\nsword: "+str(self.sword)+"\nattributes: "+str(self.swordAttributes)+"\n"
