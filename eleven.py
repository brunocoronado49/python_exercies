def calculate_food(amount, price):
    return amount * price

def calculate_drink(amount, price):
    return amount * price

def calculate_total(drink, food):
    return drink + food


food = calculate_food(5, 20)
drink = calculate_drink(2, 23)
print(food)
print(drink)
print(calculate_total(food, drink))


