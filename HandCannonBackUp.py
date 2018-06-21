import random,primary


class HandCannon(primary.Primary):
        def __init__(self):
                super().__init__()
                
                
           
                self.handCannon = random.choice(["Crimson","Palindrome","Eyesluna","Last Word","Better Devils","Old Fashioned"])

                self.hcAttributes = random.choice(['precision frame','Lightweight Frame','Aggresive Frame','Adaptive Frame','High-Impact Frame','Rapid-Fire Frame'])

                self.hcList = []
                

                for i in range (0,3):
                        self.hcList.append(random.choice(['Army of One','Crowd Control','Field Scout','Final round','Firefly','Hand loaded','Hot Swap','Icarus','Lightweight',\
                                                     'Outlaw','Quickdraw','Perfect Balence','Luck in the Chamber','Rangefinder','Mulligan','Return to Sender','Send it',\
                                                     'Single Point Sling','Smallbore','Spray and play','Snapshot','Third Eye']))

        def __str__(self):
                return super().__str__()+"\nhandCannon: "+str(self.handCannon)+"\nhcAttributes : "+str(self.hcAttributes)+"\nhcList: "+str(self.hcList)+"\n"
