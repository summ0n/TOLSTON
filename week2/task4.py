
dict01 = {"как дела?": "Все относительно, если сравнивать с больными голодающими детьми Африки, то сравнительно неплохо.", "что делаешь?": "Отвечаю на твои вопросы"}

def check_question(q, a):
    return dict01.get(q, 'Ответ на твой вопрос 42.')

def ask_user(a):
    while True:
        user_say = input('Спроси меня о чем-нибудь: ')
        if user_say.lower() == 'пока':
            print('Hasta la vista, baby!')
            break
        normalise_answer = user_say.lower()
        answer = check_question(normalise_answer,dict01)
        print(answer)

ask_user(dict01)

