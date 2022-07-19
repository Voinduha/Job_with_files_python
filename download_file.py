import os.path

import requests
from requests import Response

# Скачиваем файл из интернета
r: Response = requests.get('https://media.ethicalads.io/media/images/2020/01/sticker-wtd-colors-240-180_b9300nU.png')

f = open('selene.png', 'wb')
f.write(r.content)
f.close()

# Проверяем длинну файла
print(os.path.getsize('selene.png'))