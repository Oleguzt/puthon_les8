def show_data():
    '''Эта функция показывает содержимое справочника'''
    with open('data.txt', 'r', encoding='utf-8') as data:
        return data.read().split('\n')


def new_data():
    '''добавляет новую информацию в справочник'''
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите данные: ') + '\n')


def find_data():
    '''Эта функция ищет информацию в справочнике'''
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input()
        for i in book:
            if temp in i:
                print(i)

def delete():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input(('Введите данные: ') + '\n')
        for i in book:
            if temp in i:
                # print(i)
                print("Вы хотите удалить контакт %s (Да/Нет)?: " % i )
                name_del = input('> ')
                if name_del == 'Да':
                    book.remove(i)
                    print("Вы удалили контакт %s " % i)

def edit_сontact():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        file.write(input('Введите данные: ') + '\n')
        for i in book:
            if i in book:
                book.remove(i)
                file.write(input('Введите новые данные: ') + '\n')
        print("Контакт изменен")


while True:
    mode = input('Выберите режим работы справочника:\
                \n 1. Вывести содержимое\
                \n 2. Добавление новой информации\
                \n 3. Поиск информации\
                \n 4. Удаление записи\
                \n 5. Редактор записи\
                \n')
    if mode == '1':
        print(show_data())
    elif mode == '2':
        new_data()
    elif mode == '3':
        find_data()
    elif mode == '4':
        delete()
    elif mode == '5':
        edit_сontact()

    elif mode == '0':
        break
    else:
        print('No mode')