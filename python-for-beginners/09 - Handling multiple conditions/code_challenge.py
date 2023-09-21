# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z
name = input('What is your name? ')

if name.capitalize().startswith('A') or name.capitalize().startswith('B'):
    print('Go to room AB')
elif name.capitalize().startswith('C'):
    print('Go to room CD')
else:
    lastName = input('What is your last name? ')
    if lastName.capitalize().startswith('Z'):
        print('Go to room Z')
    else:
        print('Go to room OTHER')
    
    