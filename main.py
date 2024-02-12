import random
from PersonClass import Person
from MobileDirectoryClass import MobileDirectory
from DataClass import Data
from art import text2art
''' Данные хранятся в csv-формате, для генерации использовался сайт DataRandpmTools и библиотека faker (для генерации компаний).

    Файл PersonClass.py содержит класс Person для описания "Контакта". Поля - фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый). 
    Класс Person имеет методы изменения полей, а также метод по выводу данных (dict).

    Файл MobileDirectoryClass.py содержит класс MobileDirectory (описание записной книжки). 
    MobileDirectory хранит данные Person в словаре, где ключ - номер элемента, а значение - объект Person.
    Класс MobileDirectory содержит методы по добавлению "Контакта(ов)"  в записную книжку, методы по выводу "Контакта(ов)", методы по изменению "Контакта(ов)", а также методы поиска по всем полям класса Person
    
    Файл DataClass.py - содержит класс Data для работы с фалами .csv формата. Содержит методы по чтению, записи и формированию pandas.DataFrame. 
    Также содержит метод по добавлению организации в имеющийся .csv фал с остальными данными.
    
    Более подробную информацию можно узнать в файле с соответствующим классом.
    
    Список всех библиотек есть в файле requirements.txt.
'''
def get_page(df):
    page_size = 10
    print(f'Всего {len(df)//10} страниц\nВведите число от 1 до {len(df)//page_size}')
    page_number = int(input('Введите нужную: '))
    if(page_number <= 0 and page_number > len(df)//page_size):
        print('Неверная страница, попробуйте еще раз')
        get_page()
    else:
        start_idx = (page_number-1) * page_size
        end_idx = start_idx + page_size
        page = df.iloc[start_idx:end_idx]
    return page
def menu(df):
    try:
        menuChoice = int(input('Выберите режим: '))
        match menuChoice:
            case 0:
                return False
            case 1:
                print(get_page(df))
            case 2:
                new_dir.addPersonToDirectory(
                    Person(
                        input('Введите Имя: '),
                        input('Введите Фамилию: '),
                        input('Введите Отчество: '),
                        input('Введите Организацию: '),
                        input('Введите рабочий телефон: '),
                        input('Введите личный телефон: ')
                    )
                )
            case 3:
                deleteIndex = int(input('Введите индекс элемента, который хотите удалить: '))
                new_dir.deleteOneElement(deleteIndex)
            case 4:
                print('По какому полю желаете найти элемент?')    
                print(f'Если желаете найти по Имени напишите - a')
                print(f'Если желаете найти по Фамилию напишите - b')
                print(f'Если желаете найти по Отчеству напишите - c')
                print(f'Если желаете найти по Организации напишите - d')
                print(f'Если желаете найти по рабочему номеру напишите - e')
                print(f'Если желаете найти по личному номеру напишите - f')
                print(f'Если желаете отменить напишите - quit')
                searchMatch = input('Ваш выбор: ')
                match searchMatch:
                    case 'a':
                        print(f"Индексы найденных элементов -> {new_dir.searchByName(input('Введите имя для поиска: '))}")
                    case 'b':
                        print(f"Индексы найденных элементов -> {new_dir.searchBySurname(input('Введите фамилию для поиска: '))}" )
                    case 'c':
                        print(f"Индексы найденных элементов -> {new_dir.searchByPatronymic(input('Введите отчество для поиска: '))}")
                    case 'd':
                        print(f"Индексы найденных элементов -> {new_dir.searchByOrganization(input('Введите организацию для поиска: '))}")
                    case 'e':
                        print(f"Индексы найденных элементов -> {new_dir.searchByWorkinPhoneNumber(input('Введите рабочий телефон для поиска: '))}")
                    case 'f':
                        print(f"Индексы найденных элементов -> {new_dir.searchByPersonalPhoneNumber(input('Введите личный телефон для поиска: '))}")
                    case 'quit':
                        pass
            case 5:
                print('Введите индекс элемента, который хотите изменить')
                editNoteIndex = int(input())
                new_dir.editNote(editNoteIndex)
            
        return True
    except Exception as exp:
        print('Ошибка.... попробуйте еще раз ')
        menu()


art = text2art("Good day", font='block', chr_ignore=True)

print(art)


data = Data()


dataFrame = data.readData('info.csv', Delimiter=',')
new_dir = MobileDirectory()

for _, row in dataFrame.iterrows():
    new_dir.addPersonToDirectory(
        Person(
            row['Имя'], 
            row['Фамилия'], 
            row['Отчество'], 
            row['Имя организации'], 
            row['Рабочий телефон'], 
            row['Личный телефон']
        )
    )
    
data.write_to_dataframe(new_dir)



print('Перед вами меню навигации')

print('Вы можете добавлять, редактировать и удалять записи в справочнике')

args = True
while(args):
    print('Menu:\n0 - закрыть программу\n1 - Постраничный вывод\n2 - Добавить элемент\n3 - Удалить элемент\n4 - Найти элемент\n5 - Редактировать запись')
    args = menu(dataFrame)



data.write_to_dataframe(new_dir)

data.readDataFrame()

data.save_to_csv()