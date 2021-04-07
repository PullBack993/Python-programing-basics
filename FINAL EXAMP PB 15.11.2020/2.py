import math

counter_processor = int(input())
worker = int(input())
day_work = int(input())

total_time = worker * day_work * 8
processor = math.floor(total_time / 3)

if counter_processor <= processor:
    print(f'Profit: -> {abs(processor - counter_processor) * 110.10:.2f} BGN')
else:
    print(f'Losses: -> {abs(processor - counter_processor) * 110.10:.2f} BGN')