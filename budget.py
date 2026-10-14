ticket = 1200
hotel = 2500
food = 800
transport = 400




def count_price(ticket, hotel, food, transport):
    print("Стоимость поездки:", ticket + hotel + food + transport)
    print("Стоимость поездки на двоих:", 2* (ticket + hotel + food + transport))