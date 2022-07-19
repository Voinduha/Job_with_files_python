import xlrd

book = xlrd.open_workbook('resources/file_example_XLS_10.xls')
# Посмотреть сколько листов в файле
print(book.nsheets)
# Узнать название Листа
print(book.sheet_names())
# Обратиться к листу по индексу
sheet = book.sheet_by_index(0)
# Посчитать количество столбцов
print(f'Количество столбцов {sheet.ncols}')
# Посчитать количество строк
print(f'Количество строк {sheet.nrows}')
# Обратиться к ячейке
print(f'Ячейка 9:3 = {sheet.cell_value(rowx=9, colx=2)}')
# Распечатать целиком всю таблицу
for rx in range(sheet.nrows):
    print(sheet.row(rx))