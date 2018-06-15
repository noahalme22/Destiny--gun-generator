import random,prototype
class Primary(prototype.Prototype):
  '''primary weapon generator'''

  def __init__(self,gunType = ""):
    super().__init__()
    self.gun = gunType
    
    if gunType == "": 
      self.gun = random.choice(["autoRifle","scoutRifle","handCannon","smg"])		

