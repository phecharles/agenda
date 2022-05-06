with open('database.csv', 'r') as agenda:
    for contato in agenda.readlines():
        print(type(contato))