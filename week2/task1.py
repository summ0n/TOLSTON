def age_dist(age):
    try:
        age = float(age)
    except ValueError:
        print("Используй числа.")
        return True
    if age < 0:
        print("Не может быть отрицательным.")
        return True
    elif age > 0 and age <= 6:
        print("Ты должен идти в детский сад.")
        return False
    elif age > 6 and age <= 18:
        print("Ты должен идти в школу.")
        return False
    elif age > 18 and age <= 23:
        print("Ты должен идти в институт.")
        return False
    elif age > 23 and  age <= 60:
        print("Ты должен работать")
        return False
    elif age > 60:
        print("Ты на пенсии.")
        return False
    else:
        print("WTF (age)?")
        return False

while True:
    myage = input("Введите ваш возраст(используйте числа!!!):")
    print(myage)
    if myage == "/stop":
        break
    result = age_dist(myage)
    if result == False:
        break

