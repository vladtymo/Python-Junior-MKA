# create new list
prices = [120, 33.5, 450, 1200, 99, 1389, 240]
# index: 0, 1, 2, 4...

# show list elements
print(prices)

# add new item
prices.append(777)

# reverse elements
prices.reverse()
print(prices)

# sort elements
prices.sort()

# list elements count
print(len(prices)) # 8

# show last element
print(prices[len(prices) - 1]) # 7
print(prices[-1])

# show elements from 2 to 5
print(prices[2:5]) # 450, 1200, 99

if prices[len(prices) - 1] == prices[-1]:
    print("Elements are equals!")
else:
    print("Elements are different!")

# calculate element summ
print(sum(prices))
print(sum(prices) / len(prices))

print(f"First: {prices[0]}, Last: {prices[-1]}")

# check is element exist
if 777 in prices:
    print("777 is in the list")