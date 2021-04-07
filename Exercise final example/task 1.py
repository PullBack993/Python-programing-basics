movie_name = input()
count_days = int(input())
count_tickets = float(input())
price_tickets = float(input())
percent = int(input())

sum_tickets_day = count_tickets * price_tickets
sum_tickets_all = sum_tickets_day * count_days
sum_cinema = percent / 100 * sum_tickets_all
profit = sum_tickets_all - sum_cinema

print(f'The profit from the movie {movie_name} is {profit:.2f} lv.')