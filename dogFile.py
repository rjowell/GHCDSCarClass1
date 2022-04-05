class Dog:

  def __init__(self,_furColor,_bodySize,_hasFloppyEars,_gender,_breed):
    self.furColor = _furColor
    self.bodySize = _bodySize
    self.floppyEars = _hasFloppyEars
    self.gender = _gender
    self.breed = _breed

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