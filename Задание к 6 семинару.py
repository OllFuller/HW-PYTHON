# Домашнее задание Семинар 6
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.


def scan(data):
    # Просмотр всех записей справочника:
    for i in  data:
        print(i)
        
def search(data):
    # Поиск по справочнику.
    flag = 1
    name = input('имя > ')
    for line in data:
        if name in line:
            flag = 0
            print(line)
    if flag: print('no name given')
    
data = readfile('data.txt') # При запуске программы (скрипта), она должна считывать содержимое
dict_command = {'1' :  scan, '2' : search} # словарь команд, в значениях функции их исполняющие
 
print('''Введите номер действия:
       1 - Показать все записи
       2 - Найти запись по вхождению частей имени
       3 - Найти запись по телефону
       4 - Добавить новый контакт
       5 - Удалить контакт
       6 - Изменить номер телефона у контакта
       7 - Выход''')
 
while True:
    command = input('Команда: > ')
    if command in dict_command:
        dict_command[command](data)
    else:
        print(' command error!')