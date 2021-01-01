import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""

        file_name = file_path.split('\\')[-1]

        resp = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources/upload',
            params={
                'path': file_name,
                'fields': ['href'],
                'overwrite': True
            },
            headers={
                'Authorization': f'OAuth {self.token}'
            })

        resp.raise_for_status()

        upload_href = resp.json()['href']
        with open(file_path, 'rb') as f:
            upload_resp = requests.put(upload_href, files={'file': f})

        upload_resp.raise_for_status()
        return True


if __name__ == '__main__':
    uploader = YaUploader('')

    path = os.path.join(os.getcwd(), 'file.jpg')

    result = uploader.upload(path)
