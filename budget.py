ticket = 1200
hotel = 2500
food = 800
transport = 400

print("Стоимость поездки на двоих:", 2* (ticket + hotel + food + transport))

def transport_tax_calculate(transport):
    return transport * 0.15

def food_tax_calculate(food):
    return food * 0.20

def count_price(ticket, hotel, food, transport):
    print("Стоимость поездки:", ticket + hotel + food + transport)
    print("Стоимость поездки на двоих:", 2* (ticket + hotel + food + transport))

