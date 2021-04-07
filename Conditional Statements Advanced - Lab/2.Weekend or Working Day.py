#1	Monday
#2	Tuesday
#3	Wednesday
#4	Thursday
#5	Friday
#6	Saturday
#7	Sunday

day = input()

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    print('Working day')
elif day == 'Saturday' or day == 'Sunday':
    print('Weekend')
else:
    print('Error')