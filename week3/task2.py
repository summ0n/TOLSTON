from datetime import datetime, date, timedelta
###в venv установил python-dateutil чтобы правильно считалась дата "- месяц"
from dateutil.relativedelta import relativedelta
import locale

locale.setlocale(locale.LC_ALL, "russian")

def get_date(a):
    return datetime.strptime(a, '%d/%m/%y %H:%M:%S.%f')



now = datetime.now()

print('Вчера: {}'.format(now - timedelta(days=1)))
print('Сегодня: {}'.format(now))
print('Завтра: {}'.format(now + timedelta(days=1)))
print('Месяц назад: {}'.format(now - relativedelta(months=1)))

dt = '01/01/17 12:10:03.234567'
print(get_date(dt))

