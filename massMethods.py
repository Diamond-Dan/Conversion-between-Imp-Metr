class mass:
    def __init__(self, mass):
        self.mass = mass

    def lb_to_oz(self):
      return(self.mass *16)


    def lb_to_grams(self):
      return(self.mass *453.592)