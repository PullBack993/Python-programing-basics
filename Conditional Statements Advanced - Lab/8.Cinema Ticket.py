# Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
# 12	    12	      14	      14	       12	    16	      16

day = input()

if day == 'Monday'or day == 'Tuesday' or day == 'Friday':
    print('12')
elif day == 'Wednesday' or day == 'Thursday':
    print('14')
elif day == 'Saturday' or day == 'Sunday':
    print('16')
