import random,prototype
class primary(prototype.prototype):
  '''secondary weapon generator'''

  def __init__(self,gunType = ""):
    self.gun = gunType
    
    if gunType == "":
      
      self.gun = random.choice(["autoRifle","scoutRifle","handCannon","smg"])		
