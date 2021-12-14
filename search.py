
# def search(data, ask, noname):
#     """
#     Поиск записи в телефонной книге по имени
#     """
#     search = input(ask)
#     if search.capitalize() not in data:
#         print(noname)
#     else:
#         print(data[search.capitalize()])

def search(data, ask, no_name, file):
    """
    Поиск записи в телефонной книге по имени
    """
    search = input(ask)

    while search.isalpha() is False:
        search = input(ask)

    with open(file, 'r') as f:
        phonebook = f.readlines()
        new_phonebook = []
        for note in phonebook:
            new_note = note[:-1]
            new_phonebook.append(new_note.split(' '))
        data = (dict(new_phonebook))
        if search.capitalize() in data:
            print(data[search.capitalize()])
        else:
            print(no_name)



        # if name.capitalize() in f.read():
        #     print(bad_name)
        # else:
        #     with open(file, 'a') as f:
        #         phone_number = input(add_number)
        #         data[name.capitalize()] = phone_number
        #         for name in data:
        #             f.write(name + ' ' + data[name] + '\n')
        #     print(ok)


