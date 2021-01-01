import requests
import datetime
from pprint import pprint


def main():
    # Проверок на правильность ввода не делаем((
    tags = input('Введите теги через запятую: ').split(',')
    days_count = int(input('Введите количество дней, за которые показать вопросы: '))

    now = datetime.datetime.now()
    two_days_delta = datetime.timedelta(days=days_count)
    two_days_ago = now - two_days_delta

    answer = requests.get(
        'https://api.stackexchange.com/2.2/questions',
        params={
            'fromdate': str(two_days_ago.timestamp()).split('.')[0],
            'todate': str(now.timestamp()).split('.')[0],
            'tagged': ';'.join(tags),
            'site': 'stackoverflow',
            'sort': 'creation',
            'order': 'desc'
        }
    )

    answer.raise_for_status()
    pprint(answer.json()['items'])


if __name__ == '__main__':
    main()
