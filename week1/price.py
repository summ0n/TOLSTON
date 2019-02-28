def get_summ(one, two, delimiter='&'):
    result = one + delimiter + two
    print(result.upper())
get_summ("Learn", "Python")

def format_price(price):
    price = int(price)
    print(f"Цена: {price} руб.")

format_price(56.24)