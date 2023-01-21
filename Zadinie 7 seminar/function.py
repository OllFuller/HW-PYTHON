def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result


def save_data_to_file(name, data_list):
    with open(name, 'w', encoding='utf8') as datafile:
        for rawdata in data_list:
            datafile.write(rawdata + '\n')


def print_bus():
    return read_data_from_file('bus.txt')


def add_bus():
    save_data_to_file('bus.txt', input("Введите параметры автобуса"))


def print_driver():
    return read_data_from_file('driver.txt')


def add_driver():
    save_data_to_file('driver.txt', input("Введите водителя"))


def print_route():
    return read_data_from_file('route.txt')

def print_route():
        return read_data_from_file('details.txt')

def exit():
            lambda: exit()


def add_route():
    save_data_to_file('route.txt', input("Введите маршрут "))
