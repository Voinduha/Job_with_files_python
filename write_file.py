# Делаем файл и прописываем в нем строку

# f = open('example.txt', 'w')
# f.write('Hello world')
# f.close()


f = open('example.txt')
for row in f:
    print('Hello world')