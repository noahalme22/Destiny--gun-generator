import random,heavy

class swords(heavy.Heavy):
        def __init__(self,swordList = "", swordAttributes = "", sword = ""):
                super().__init__()


                self.sword = sword
                self.swordAttributes = swordAttributes
                self.swordList = swordList



                swordList = []
                if swordList == "":
                        swordList = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])

                if sword == "":
                        sword = random.choice(["Raze-Lighter","Dark-Drinker","The Young Wolfs Howl","Worldline Zero"])

        def __str__(self):
                return super().__str__()+"\nsword: "+str(self.sword)+"\nattributes: "+str(self.swordAttributes)+"\nlist: "+str(self.swordList)+"\n"
