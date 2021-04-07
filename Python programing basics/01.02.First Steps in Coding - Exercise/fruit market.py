strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberry_kg = float(input())
strawberries_kg = float(input())

raspberry_price = strawberries_price * 50 / 100
oranges_price = raspberry_price - (0.4 * raspberry_price)
bananas_price = raspberry_price - (0.8 * raspberry_price)

price_for_raspberry = raspberry_price * raspberry_kg
price_for_oranges = oranges_price * oranges_kg
price_for_bananas = bananas_price * bananas_kg
price_for_strawberries = strawberries_price * strawberries_kg

total_amount = price_for_raspberry + price_for_oranges + price_for_bananas + price_for_strawberries
print(total_amount)