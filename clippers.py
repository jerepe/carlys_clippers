# Carly's Clippper haircuts, prices, and number of times they've been sold each variables declaration:
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# let's calculate the total price we can capitalise on:
total_price = 0

for price in prices:
    total_price += price

# average haircut price calculation:
average_price = total_price / len(prices)
print("Average Haircut Price:\n $" + str(average_price))

# Let's reduce the price of each haircut by $5::
new_prices = [price - 5 for price in prices]

# You can also use the loop created under those comments
# Iroduces the same output at the list comprehension just above
# If you uncomment the lines below, comment out the new_prices list above.

#for price in prices:
#    new_prices.append(price - 5)
#print(new_prices)

# Total revenue for the last week calculation:
total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue:\n $" + str(total_revenue))

# Average daily revenue calculation:
average_daily_revenue = total_revenue / 7
print("Average daily revenue:\n $" + str(average_daily_revenue))

# Making advertise for haircuts under $30:
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

# You can uncomment the loop below if you don't want to use the cuts_under_30 list above.
# If you uncomment the lines below, you need to empty the list above like such: cuts_under_30 = []

#for i in range(len(hairstyles)):
#    if new_prices[i] < 30:
#        cuts_under_30.append(hairstyles[i])

# Prints our advertise:
print("Haircuts under $30:\n " + str(cuts_under_30))

