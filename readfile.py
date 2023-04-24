def show_all():
    file1 = open('spravochnik.txt', 'r', encoding='UTF-8')
    data1 = file1.readlines()
    for i in data1:
        print(i)
    file1.close()

def add_contact():
    file2 = open('spravochnik.txt', 'a', encoding='UTF-8')
    data2 = input('Введите ФИО, телефон и комментарий (с разделителем ;): ')
    file2.write(data2)
    file2.close()

def edit_contact():
    find_parameter = input('Введите что нужно найти: ') 
    edit_parameter = input('Введите на что заменить: ')
    file3 = open('spravochnik.txt', 'r', encoding='UTF-8')
    data3 = file3.readlines()
    data_new = []
    for data_str in data3:
        if find_parameter in data_str:
                print("найдено совпадение:", data_str)
                data_new.append(edit_parameter) 
        else:
            data_new.append(data_str) 
    file3.close()

def find_contact():
    find_parameter = input('Введите параметр, который нужно найти: ')
    file4 = open('spravochnik.txt', 'r', encoding='UTF-8')
    data4 = file4.readlines()
    for data_str in data4:
        if find_parameter in data_str:
                print("найдено совпадение:", data_str)
    file4.close()

def delete_contact():
    find_parameter = input('Введите контакт, который нужно удалить: ')
    file5 = open('spravochnik.txt', 'r', encoding='UTF-8')
    data5 = file5.readlines()
    print(data5)
    data_new = []
    for data_str in data5:
        if find_parameter in data_str:
            data_new.pop(find_parameter) 
    file5.close()
    print(data_new)