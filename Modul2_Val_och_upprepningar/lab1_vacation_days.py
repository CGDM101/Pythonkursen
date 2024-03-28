# TASK 1 - CALCULATE THE NUMBER OF VACATION WEEKS AND DAYS  

# Write a python program that takes as input the number of vacation days and returns the number of 
# full weeks and days of the vacation time. The program should take into account following: 
# if the vacation time covers less than one week - no number of full weeks should be printed; 
# if the vacation time covers a number of full weeks without any remaining days - no number of remaining days should be printed; 
# if the number of full weeks or remaining days is 1, the prompt should take that into account 
# and use a singular form as shown in the examples.


vacation_days = int(input('Enter the number of vacation days: '))

if vacation_days >= 7:
    veckor = vacation_days // 7
    rest = vacation_days % veckor
else:
    veckor = 0
    rest = vacation_days


if veckor > 1:
    print(f'{veckor} weeks')
else:
    print(f'{veckor} week')
if rest > 1 or veckor <= 7:
    print(f'{rest} days')
else:
    print(f'{rest} day')



# Enter the number of vacation days: 9
# 1 week
# 2 days
    
# Enter the number of vacation days: 21
# 3 weeks

# Enter the number of vacation days: 15
# 2 weeks
# 1 day

# Enter the number of vacation days: 31
# 4 weeks
# 3 day2
