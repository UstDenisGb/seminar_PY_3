# 1. Открыть файл
# 2. Сохранить файл
# 3. Просмотреть контакты
# 4. Создать контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

import readfile

print ('Главное меню')
print ('1. Открыть книгу и просмотреть контакты')
print ('2. Добавить контакт')
print ('3. Изменить контакт')
print ('4. Поиск контакта')
print ('5. Удалить контакт')

choose = int(input ('Введите пункт меню: '))
if choose == 1:
    readfile.show_all()
if choose == 2:
    readfile.add_contact()
if choose == 3:
    readfile.edit_contact()
if choose == 4:
    readfile.find_contact()
if choose == 5:
    readfile.remove_contact()