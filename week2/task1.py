AGE = None
def get_age():
    AGE = None
    while not type(AGE) == int:
        try:
            AGE = int(input("Введите ваш возраст(используйте числа!!!):"))
        except ValueError:
            print("ИСПОЛЬЗУЙ ТОЛЬКО ЧИСЛА")


    return AGE

def age_counter():
    AGE = get_age()
    while AGE < 0:
        print("Возраст не может быть отрицательным")
        AGE = get_age()
    if AGE :
        if AGE > 0 and AGE < 7:
            print("Привет малыш, собирайся в детский сад")

age_counter()        