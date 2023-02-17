def stock_availability(*availability):
    stock = list(availability[0])
    action = availability[1]
    if len(availability) > 2:
        for i in range(2, len(availability)):
            if action == "delivery":
                stock.append(availability[i])

            elif action == "sell":
                if str(availability[i]).isalpha():
                    if availability[i] in stock:
                        stock = [x for x in stock if x != availability[i]]
                else:
                    if len(stock) >= int(availability[i]):
                        for _ in range(int(availability[i])):
                            stock.pop(0)

    elif action == "sell":
        stock.pop(0)

    return stock


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 0))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 1))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 2))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
