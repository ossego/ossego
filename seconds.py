#This program asks the user to enter a number of seconds as a positive integer n
#It then converts seconds into days, hours, minutes and seconds

#86400 seconds in 1 day
#3600 seconds in 1 hour
#60 seconds in 1 minute

user_input = int(input('enter any number of seconds: '))
n = user_input
years=    n//31536000
days=    (n-(years*31536000))//86400
hours=   (n-(years*31536000)-(days*86400))//3600
minutes= (n-(years*31536000)-(days*86400)-(hours*3600))//60
seconds= (n-(years*31536000)-(days*86400)-(hours*3600)-(minutes*60))
print(years,'years',days,'days',hours,'hours', minutes,'minutes',seconds,'seconds')





