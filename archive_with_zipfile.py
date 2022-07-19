from zipfile import ZipFile

zip_ = ZipFile('resources/hello.zip')
# Смотрим, что у нас внутри архива
print(zip_.namelist())
# Распаковываем только файл Hello.txt в дирректорию tmp
zip_.extract('Hello.txt', 'tmp')
# Прочитаем и заасертим текст из заархивированного файла
# text = zip_.read('Hello World')
# print(text)
zip_.close()
# with ZipFile('resources/hello.zip') as myzip:
#     myzip.extract('Hello.txt')
# Распаковываем весь архив в папку tmp
# zip_.extractall('tmp')
