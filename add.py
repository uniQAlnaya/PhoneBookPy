
def add(file, data, add_name, bad_name, add_number, ok):

    """
    Добавление записи в телефонную книгу
    """
    name = input(add_name)
    while name.isdigit() or name.isalpha() is False:
        name = input(add_name)
    with open(file, 'r') as f:
        if name.capitalize() in f.read():
            print(bad_name)
        else:
            with open(file, 'a') as f:
                phone_number = input(add_number)
                while phone_number.isdigit() is False:
                    phone_number = input(add_number)
                data[name.capitalize()] = phone_number
                for name in data:
                    f.write(name + ' ' + data[name] + '\n')
            print(ok)