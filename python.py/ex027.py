#type the full name ,the program will say your first name and your last name
name = str(input('type your full name: '))
print('nice to meet you {}'.format(name))
separate = name.split()
print('your first name {}'.format(separate[0]))
print('the last name is {}'.format(separate[len(separate)-1]))
