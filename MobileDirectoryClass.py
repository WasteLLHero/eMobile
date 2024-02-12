from PersonClass import Person

class MobileDirectory:
    '''Инициализруем класс, храниться все будет в словаре'''
    def __init__(self, Directory: dict = {}): 
        self.Directory = Directory
        
    '''Метод добавления одной персоны в словарь'''
    def addPersonToDirectory(self, person: Person):
        self.Directory[max(self.Directory.keys(), default=0) + 1] = person
        
    '''Метод добавления списка персон в словарь'''
    def addPersonsToDirectory(self, personsList: list[Person]) -> dict:
        # self.Directory.update({i + len(self.Directory): personsList[i] for i in range(len(personsList))})
        self.Directory.update({max(self.Directory.keys(), default=0) + i: personsList[i] for i in range(len(personsList))})
        
    '''Метод по удалению одного элемента'''
    def deleteOneElement(self, index):
        del self.Directory[index]
        
    '''Метод вывода информации о всех персонах хранящихся в классе'''
    def getInfoAboutPersons(self) -> dict:
        return {key: value.getAllinfo() for key, value in self.Directory.items()}    
    
    '''Метод вывода информации о персоне по индексу'''
    def getInfoAboutPerson(self, index: int) -> dict: 
        return self.Directory[index].getAllinfo()
    
    '''Метод для редактирования всех записей в справочнике'''
    def editAllInfo(self, index):
        newName = input('Введите новое имя: ')
        self.Directory[index].editPersonName(newName)
        newName = input('Введите новую фамилию: ')
        self.Directory[index].editPersonSurname(newName)
        newName = input('Введите новое отчество: ')
        self.Directory[index].editPersonPatronymic(newName)
        newName = input('Введите новую организацию: ')
        self.Directory[index].editPersonOrganization(newName)
        newName = input('Введите новый рабочий номер: ')
        self.Directory[index].editPersonWorkinPhoneNumber(newName)
        newName = input('Введите новый личный номер: ')
        self.Directory[index].editPersonPersonalPhoneNumber(newName)
        
    '''Поиск элементов по имени в справочнике'''
    def searchByName(self, name):
        return [key for key, value in self.Directory.items() if isinstance(value.name, str) and value.name == name]
    
    '''Поиск элементов по фамилии в справочнике'''
    def searchBySurname(self, name):
        return [key for key, value in self.Directory.items() if isinstance(value.surname, str) and value.surname == name]
    
    '''Поиск элементов по отчеству в справочнике'''
    def searchByPatronymic(self, name):
        return [key for key, value in self.Directory.items() if isinstance(value.patronymic, str) and value.patronymic == name]
    
    '''Поиск элементов по организации в справочнике'''
    def searchByOrganization(self, name):
        return [key for key, value in self.Directory.items() if isinstance(value.organization, str) and value.organization == name]
    
    '''Поиск элементов по рабочему телефону в справочнике'''
    def searchByWorkinPhoneNumber(self, name):
        return [key for key, value in self.Directory.items() if isinstance(value.WorkinPhoneNumber, str) and value.WorkinPhoneNumber == name]
    
    '''Поиск элементов по личному телефону в справочнике'''
    def searchByPersonalPhoneNumber(self, name):
        return [key for key, value in self.Directory.items() if isinstance(value.PersonalPhoneNumber, str) and value.PersonalPhoneNumber == name]
    
    '''Метод для редактирования записей в справочнике (на выбор)'''
    def editNote(self, index):
        print(f'Что желаете изменить?')
        print(f'Если желаете изменить Имя напишите - 1')
        print(f'Если желаете изменить Фамилию напишите - 2')
        print(f'Если желаете изменить отчество напишите - 3')
        print(f'Если желаете изменить организацию напишите - 4')
        print(f'Если желаете изменить рабочий номер напишите - 5')
        print(f'Если желаете изменить личный номер напишите - 6')
        print(f'Если желаете изменить всё напишите - 7')
        print(f'Если желаете отменить напишите - 0')
        choice = int(input())
        match choice:
            case 0:
                return f'Вы вышли из режима редактирования'
            case 1:
                newName = input('Введите новое имя: ')
                self.Directory[index].editPersonName(newName)
            case 2:
                newName = input('Введите новую фамилию: ')
                self.Directory[index].editPersonSurname(newName)
            case 3:
                newName = input('Введите новое отчество: ')
                self.Directory[index].editPersonPatronymic(newName)
            case 4:
                newName = input('Введите новую организацию: ')
                self.Directory[index].editPersonOrganization(newName)
            case 5:
                newName = input('Введите новый рабочий номер: ')
                self.Directory[index].editPersonWorkinPhoneNumber(newName)
            case 6:
                newName = input('Введите новый личный номер: ')
                self.Directory[index].editPersonPersonalPhoneNumber(newName)
            case 7:
                self.editAllInfo(index)
            
        
        
        
    