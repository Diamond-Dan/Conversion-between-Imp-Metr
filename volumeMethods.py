class Volume:
  def __init__(self, volume):
    self._volume = volume
    # self.cups = cups
    # self.gallon = gallon
    # self.quarts = quarts
    # self.pints = pints

  def tsp_to_mL(self):
    return self._volume * 4.92892
  def cups_to_ml(self):
    return self._volume * 240
  def tbsp_to_mL(self):
    return self._volume * 14.7868
#  def gallon_to_liters(self):
#    return self._volume * 3.785
  def gallon_to_ml(self):
    return self._volume * 3785.4119997685
#  def quart_to_liters(self):
#    return self._volume * 0.946353 
  def quart_to_ml(self):
    return self._volume * 946.35299994212493857
  def pints_to_ml(self):
    return self._volume * 473.176249991928


  # Volume 
  # TSP float= (teaspoon) *5ml
  # TBSP (tablespoon)*15ml
  # Cups (cups)*250ml 
  # Gallon (gallon)*4.5L
  # Quart (quart)*1.1L
  # Pints (pint)*473.2ml 

#comment: these conversions probably aren't as accurate a google, might be better to use the google conversion
