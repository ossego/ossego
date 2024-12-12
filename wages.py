#This program calculates hourly wages at tier levels.

user_input = int(input("Please enter the total number of hours you worked this past week: "))
hourly_rate1 = 8   #first 40 hours of work, $8/hour
hourly_rate2 = 9   #hours between 41 & 50, $9/hour
hourly_rate3 = 10  #hours worked above 50, $10/hour

if user_input < 0 or user_input > 168:
    print("INVALID")
elif user_input <= 40 :
    print('YOU MADE', (user_input*hourly_rate1) , 'DOLLARS THIS WEEK')
elif 41 <= user_input <= 50 :
    print('YOU MADE', ((40*hourly_rate1)+((user_input-40)*hourly_rate2)), 'DOLLARS THIS WEEK')
else:
    print('YOU MADE',(40*hourly_rate1)+(10*hourly_rate2)+((user_input-50)*hourly_rate3), 'DOLLARS THIS WEEK')
