#analysing a string,
# .strip() will take off all space bfore and after
n = str(input('type your name: ')).strip()
# we can  change for upper inside of print
print('my name in upper is {}'.format(n.upper()))
print('my name in lower is {}'.format(n.lower()))
#check how many leters my name has
#we can use len for count,however this funcion count empty space as well,
#then we can use - n.count(' ') for count without space
print('my name has {} letters'.format(len(n) - n.count(' ')))
#we want know only the first name
#we can use n.find(' ')it is mean will localizated teh first empty space
#print('my first name has {}'.format(n.find(' ')))
# another way to find out the first name is ,if we separated all name
#we can create a variable to split
separate = n.split()
print('your first name is {},and it has {} letters'.format(separate[0],len(separate[0])))
