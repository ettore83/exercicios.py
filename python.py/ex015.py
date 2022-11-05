#make a program to read how many days was rented the car and read how much KM the car drive.and calculation how much the person need pay for the service.
#the price is 60 for days and 0,15 for km
days = float(input('how many days was rented: '))
km = float(input('how many km was drived: '))
diaria = days*60
percurso = km * 0.15
print('the price of service: {}'.format(diaria + percurso))