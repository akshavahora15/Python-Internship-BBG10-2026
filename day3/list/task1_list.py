prices = [199, 499, 999, 1499, 299, 799, 1299, 349, 599, 899]
average = sum(prices) / len(prices)

above_avg = [p for p in prices if p > average]

print("Average:", average)
print("Prices above average:", above_avg)