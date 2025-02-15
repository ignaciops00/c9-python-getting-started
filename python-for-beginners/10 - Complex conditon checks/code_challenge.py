# When you join a hockey team you get your name on the back of the jersey
# but the jersey may not be big enough to hold all the letters
# Ask the user for their first name

# Ask the user for their last name

# if first name is < 10 characters and last name is < 10 characters 
#       print first and last name on the jersey
# if first name >= 10 characters long and last name is < 10 characters
#       print first initial of first name and the entire last name
# if first name < 10 characters long and last name is >= 10 characters
#       print entire first name and first initial of last name
# if first name >= 10 characters long and last name is >= 10 characters
#       print last name only

# Test with the following values
# first name: Susan  last name: Ibach
# output: Susan Ibach
# first name: Susan  last name: ReallyLongLastName
# output: Susan R.
# first name: ReallyLongFirstName  last name: Ibach
# output: R. Ibach
# first name: ReallyLongFirstName  last name: ReallyLongLastName
# output: ReallyLongLastName

name = input('What is your name? ')
lastName = input('What is your last name? ')


if len(name)<10:
    nameLessTen = True
else:
    nameLessTen = False
    
if len(lastName)<10:
    lastNameLessTen = True
else:
    lastNameLessTen = False
        
if nameLessTen and lastNameLessTen:
    print(name + ' ' + lastName)
elif not nameLessTen and lastNameLessTen < 10:
    print(name[0:1] + '. '+lastName)
elif nameLessTen and not lastNameLessTen:
    print(name + ' '+lastName[0:1]+'.')
else: print(lastName)
