import random, secondary

class Sniper(secondary.Secondary):
        def __init__(self,sniperList = "",sniperAttributes = "",sniper = ""):
                super().__init__()


                self.sniper = sniper
                self.sniperAttributes = sniperAttributes
                self.sniperList = sniperList 

                sniperList = []
                if sniperAttributes == "":

                      sniper = random.choice(['precision frame','LightWeight','Aggressive Frame','Adept Frame','High-Impact Frame','Rapid-Fire Frame'])               



                if sniperList == "":
                    for i in range (0,3):
                        sniperList = random.choice(['Third Eye','Take a Knee','Tacsys SLS15','Sightsys SLS20','Snapshot','Surplus','Spray and play','Rodeo','Replenish','Perfect Balence','Quickdraw','Outlaw','Mulligan','Lightweight','Injection Mold','Hidden Hand','Hand-Laid Stock','Hammer Forged','Flared Magwell','Final Round','Fitted Stock','Casket Mag','Braced Frame','Armor Piercing Rounds'])



                if sniper == "":
                      sniper = random.choice(["Ice Breaker","Longbow Synthesis","LDR 5001","D.A.R.C.I","Aachen-LR2","Borealis"])


        def __str__(self):
                return super().__str__()+"\nsniper: "+str(self.sniper)+"\nattributes: "+str(self.sniperAttributes)+"\nlist: "+str(self.sniperList)+"\n"
