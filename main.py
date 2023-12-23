import massMethods
import volumeMethods

userinput = 0 # User input for menu 1
userinput2 =0 #second user input
orginal_value = 0#orginal number of units in userinput
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


if userinput == 1 or userinput == 2: #only includes mass mesurements
  print('Enter 1 for grams') #create methods
  print('Enter 2 for kilograms') #create methods
  #enter metric converstions
  userinput2= int(input('Please select your desired unit to convert to.'))

if userinput >2: #volume measurements
 # enter metric conversion
  print('Enter 1 for liters') 
  print('Enter 2 for mililiters') 
  userinput2= int(input('Please select your desired unit to convert to.'))
#NOTES: method for each converstion

# Convert unit type into grams if mass
while isinstance(orginal_value, float) == False:
  try:
    orginal_value = float(
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
inputmass = masscalc(orginal_value)
inputvol = volcalc(orginal_value)

if userinput == 1:
  orginal_unit_name = 'oz'
  end_unit = (inputmass.oz_to_grams())
  new_unit_name= 'grams'
  if(userinput2 == 2):
    end_unit = end_unit/10
    new_unit_name='Kilograms'
    
if userinput == 2:
   orginal_unit_name = 'lbs'
   end_unit=(inputmass.lb_to_oz())
   new_unit_name= 'grams'
   if(userinput2 == 2):
    end_unit = end_unit/10
    new_unit_name='Kilograms'
    
if userinput == 3:
   orginal_unit_name = 'cups'
   end_unit= (inputvol.cups_to_ml())
   new_unit_name= 'mililiter'
   if(userinput2 == 1):
     end_unit = end_unit/1000
     new_unit_name='liters'

if userinput == 4:
   orginal_unit_name = 'pints'
   end_unit= (inputvol.pints_to_ml())
   new_unit_name= 'mililiter'
   if(userinput2 == 1):
     end_unit = end_unit/1000
     new_unit_name='liters'

if userinput == 5:
   end_unit= (inputvol.quart_to_ml())
   orginal_unit_name = 'quarts'
   new_unit_name= 'mililiter'
   if(userinput2 == 1):
     end_unit = end_unit/1000
     new_unit_name='liters'

if userinput == 6:
   end_unit= (inputvol.gallon_to_ml())
   orginal_unit_name = 'gallon'
   new_unit_name= 'mililiter'
   print(end_unit)
   if(userinput2 == 1):
     end_unit = end_unit/1000
     new_unit_name='liters'

if userinput == 7:
   end_unit= (inputvol.tbsp_to_mL())
   orginal_unit_name = 'tbsp'
   new_unit_name= 'mililiter'
   if(userinput2 == 1):
     end_unit = end_unit/1000
     new_unit_name='liters'

if userinput == 8:
  end_unit= (inputvol.tsp_to_mL())
  orginal_unit_name = 'tsp'
  new_unit_name= 'mililiter'
  if(userinput2 == 1):
    end_unit = end_unit/1000
    new_unit_name='liters'

#comment: how do i round numbers?


print('You converted ' + str(orginal_value) + ' ' + 
      orginal_unit_name + ' to ' + str(end_unit) +' '+ new_unit_name + '.')