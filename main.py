import massMethods
import volumeMethods

userinput = 0
conversion=0
#ask user what orginal measurement value is:

while userinput == 0 or userinput > 5: 
  print('Enter 1 for oz.')
  print('Enter 2 for lb.')
  print('Enter 3 for cups.')
  print('Enter 4 for pint.')
  print('Enter 5 for quart.')
  userinput = int(input('Please enter a unit type.'))
  #might break if it is a letter 
#get user input for unit type

#NOTES: method for each converstion 

# Convert unit type into grams if mass
conversion = input("Please enter your amount of substance you have as an integer: ")
  
if conversion !=int:
  print("Please enter a valid integer.")
  conversion = int(input("Please enter your amount of substance you have as an integer: "))

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
if userinput == 2:
  print(inputmass.lb_to_oz())

# if userinput == 1:
