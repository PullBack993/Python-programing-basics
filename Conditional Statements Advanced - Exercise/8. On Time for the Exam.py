exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes

diff = arrival_time - exam_time

hh = abs(diff) // 60
mm = abs(diff) % 60


if diff < -30:
    print ('Early')
    if hh > 0:
        print (f'{hh}:{mm:02d} hours before the start')
    else:
        print(f'{mm} minutes before the start')
elif diff <= 0:
    print ('On time')
    if not diff == 0:
        if hh > 0:
            print(f'{hh}:{mm:02d} hours before the start')
        else:
            print(f'{mm} minutes before the start')

else:
    print('Late')
    if hh > 0:
        print (f'{hh}:{mm:02d} hours after the start')
    else:
        print(f'{mm} minutes after the start')

