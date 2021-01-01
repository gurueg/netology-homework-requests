import requests
import datetime
from pprint import pprint


def main():
    now = datetime.datetime.now()
    two_days_delta = datetime.timedelta(days=2)
    two_days_ago = now - two_days_delta

    print(now.timestamp())

    answer = requests.get(
        'https://api.stackexchange.com/2.2/questions',
        params={
            'fromdate': str(two_days_ago.timestamp()).split('.')[0],
            'todate': str(now.timestamp()).split('.')[0],
            'tagged': 'python',
            'site': 'stackoverflow',
            'sort': 'creation',
            'order': 'desc'
        }
    )

    answer.raise_for_status()
    pprint(answer.json()['items'])


if __name__ == '__main__':
    main()
