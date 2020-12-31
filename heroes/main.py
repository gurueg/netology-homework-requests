import requests


def main():
    token = '2619421814940190'
    url_base = f'https://www.superheroapi.com/api.php/{token}/'

    names = ['Hulk', 'Captain America', 'Thanos']
    max_name = ''
    max_int = 0

    for name in names:
        resp = requests.get(url_base + 'search/' + name).json()

        if resp['response'] == 'success':
            current_id = resp['results'][0]['id']

            current_int = requests.get(url_base + current_id + '/powerstats').json()['intelligence']
            current_int = int(current_int)

            if current_int > max_int:
                max_int = current_int
                max_name = name

    print(f'The smartest hero is {max_name} with intelligence value equals {max_int}')


if __name__ == "__main__":
    main()
