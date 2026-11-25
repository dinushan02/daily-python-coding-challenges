def max_profit(prices):
    if not prices:
        return 0

    index = 0
    minimum_price = prices[0]
    maximum_profit = 0

    while index < len(prices):
        if minimum_price > prices[index]:
            minimum_price = prices[index]

        possible_profit = prices[index] - minimum_price

        if possible_profit > maximum_profit:
            maximum_profit = possible_profit

        index += 1

    return maximum_profit


prices = [7, 1, 5, 3, 6, 4]
result = max_profit(prices)
print(result)