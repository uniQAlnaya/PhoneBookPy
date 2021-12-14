import messages
import add
import search


friends = {}
data = friends



print(messages.all_text['head'])
for name in messages.all_text['list']:
    print(name, messages.all_text['list'][name])

while True:
    print()
    com = input(messages.all_text['command'])
    commands = com.strip( )

    if commands.lower() == 'add':
        add.add('phonebook.txt',
                data,
                messages.all_text['add_name'],
                messages.all_text['bad_name'],
                messages.all_text['add_number'],
                messages.all_text['ok'])
        # with open('phonebook.txt', 'r') as f:
        #     phonebook = f.readlines()
        #     new_phonebook = []
        #     for note in phonebook:
        #         new_note = note[:-1]
        #         new_phonebook.append(new_note.split(' '))
        #
        #     friends = (dict(new_phonebook))


    elif commands.lower() == 'search':

        search.search(friends,
                      messages.all_text['ask'],
                      messages.all_text['no_name'],
                      'phonebook.txt')


    elif commands.lower() == 'exit':
        print(messages.all_text['bye'])
        break


    else:
        print(messages.all_text['head'])
        for name in messages.all_text['list']:
            print(name, messages.all_text['list'][name])


