import massMethods
import volumeMethods

userinput = 0 # User input for menu 1
conversion = 0 #orginal number of units in userinput
orginal_unit_name ='' # orginal unit type
new_unit_name = '' #unit type being converted to
end_unit = 0 #value of unit type  being converted too calculated using massMethod or volumeMethods
#ask user what orginal measurement value is:

while userinput == 0 or userinput > 8:
  print('Enter 1 for oz.')
  print('Enter 2 for lb.')
  print('Enter 3 for cups.')
  print('Enter 4 for pint.')
  print('Enter 5 for quart.')
  print('Enter 6 for gallon.')
  print('Enter 7 for tablespoon.')
  print('Enter 8 for teaspoon.')
  userinput = int(input('Please your starting unit of measurement type.'))
  #might break if it is a letter
#get user input for unit type

if userinput == 1 or userinput == 2:
  print('Enter 1 for grams') #create methods
  print('Enter 2 for kilograms') #create methods
  #enter metric converstions
  userinput2= int(input('Please select your desired unit to convert to.'))

if userinput >2:
 # enter metric conversion
  userinput2= int(input('Please select your desired unit to conver to.'))
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
   end_unit=(inputmass.lb_to_oz())
if userinput == 3:
   end_unit= (inputvol.cups_to_ml())
if userinput == 4:
   end_unit= (inputvol.pints_to_ml())
if userinput == 5:
   end_unit= (inputvol.quart_to_liters())
if userinput == 6:
   end_unit= (inputvol.gallon_to_liters())
if userinput == 7:
   end_unit= (inputvol.tbsp_to_mL())
if userinput == 8:
  end_unit= (inputvol.tsp_to_mL())
#comment: how do i round numbers?


print('You converted ' + str(conversion) + ' ' + orginal_unit_name + ' to ' end_unit + new_unit_name + '.'')