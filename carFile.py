class Car:

  def revTheEngine(self):
    print("Rev Rev Rev")
  
  def __init__(self,_colorInput,fuelType,_tireSize,_hasSpoilers,isConvertible):
    self.color = _colorInput
    self.fuelType = fuelType
    self.tireSize = _tireSize
    self.spoilers = _hasSpoilers
    self.convertible = isConvertible
    self.numOfTires = 4
    self.maxFuel = 30
    self.currentFuel = 15

  def explode(self):
    print("KaBOOM!")

  def backUp(self):
    print("Beep Beep")

  def drive(self):
    print("We're driving down the road!")

  def turn(self):
    print("We're turning now!")

  # Drive - Backwards, forwards
  # Turn - Left/Right
  # Explode
  # Speed Up/Slow Down - Every time we speed up, use 
  # Engine - Fuel