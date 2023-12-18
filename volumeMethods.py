class Volume:
  def __init__(self, volume):
    self._volume = volume
    # self.cups = cups
    # self.gallon = gallon
    # self.quarts = quarts
    # self.pints = pints

  def tsp_to_mL(self):
    return self._volume * 4.929
  def cups_to_ml(self):
    return(self._volume * 250)
  def tbsp_to_mL(self):
    


  # Volume 
  # TSP float= (teaspoon) *5ml
  # TBSP (tablespoon)*15ml
  # Cups (cups)*250ml 
  # Gallon (gallon)*4.5L
  # Quart (quart)*1.1L
  # Pints (pint)*473.2ml 
