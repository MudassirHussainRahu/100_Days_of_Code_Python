print('Welcome to the tip calculator.')
total_bill  = float(input('What was the total bill? '))

tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

total_bill = total_bill + (total_bill*tip_percentage/100)

each_person_share = round(total_bill/people, 2)

each_person_share = '{:.2f}'.format(each_person_share)

print(f'Each person should pay: {each_person_share}')


