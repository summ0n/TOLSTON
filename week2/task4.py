

def ask_user():
    while True:
        user_say = input('Как дела: ')
        if user_say.lower() == 'пока':
            print('Ну пока')
            break
        else:
            print('Сам ты {}'.format(user_say))

ask_user()

dict01 = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}

while True:
    inp = input('Задавай свой вопрос.\n')
    if inp.lower() == 'стоп':
        print('Опрос закончен')
        break
    elif inp in dict01:
        print(dict01[inp])
    else:
        print('Я не знаю ответа на твой вопрос')
