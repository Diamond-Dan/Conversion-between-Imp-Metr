import massMethods
import volumeMethods

userinput = 0
conversion = 0
#ask user what orginal measurement value is:

while userinput == 0 or userinput > 6:
  print('Enter 1 for oz.')
  print('Enter 2 for lb.')
  print('Enter 3 for cups.')
  print('Enter 4 for pint.')
  print('Enter 5 for quart.')
  print('Enter 6 for gallon.')
  #print('Enter 7 for tablespoon.')
  #print('Enter 8 for teaspoon.')
  userinput = int(input('Please enter a unit type.'))
  #might break if it is a letter
#get user input for unit type

#NOTES: method for each converstion

# Convert unit type into grams if mass
while isinstance(conversion, float) == False:
  try:
    conversion = float(
        input(
            "Please enter your amount of substance you have as an integer or float: "
        ))
  except:
    print("Please enter a valid input.")

# def is_integer(n):
#   try:
#       float(n)
#   except ValueError:
#       return False
#   else:
#       return float(n).is_integer()


#send grams to mass, and return desired unit type
masscalc = massMethods.mass
volcalc =  volumeMethods.Volume
inputmass = masscalc(conversion)
inputvol = volcalc(conversion)

#if userinput == 1:
if userinput == 2:
  print(inputmass.lb_to_oz())
#if userinput == 3:
if userinput == 4:
  print(inputvol.pints_to_ml())
if userinput == 5:
  print(inputvol.quart_to_liters())
if userinput == 6:
  print(inputvol.gallon_to_liters())
#if userinput == 7:
#if userinput == 8:


