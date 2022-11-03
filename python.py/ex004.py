#make a program that reads something by keyboard and shows its primitive type
n = input('type the value: ')
#check what kind of type ,if str = string,int = inteiro ,bool = bolleano , float = float numbers
print("the type is : ",type (n))
#check if the user typed space
print('there is space? ', n.isspace())
#check if what was typed is a number
print('is there a number? ',n.isnumeric())
#check that what was typed is an alphabet
print('is there alphabet? ',n.isalpha())
#check if what was typed is alphabetic and numeric
print('alphanumeric? ',n.isalnum())
#check if what you typed is in capital letters
print('it is in capital letters? ',n.isupper())
#check if what you typed is in lower case
print('it is in lowercase? ',n.islower())
#check if only the first letter is capitalized
print('is capitalized? ',n.istitle())
