class Person:
    '''Инициализируем поля класса'''
    def __init__(self,  name: str, surname: str, patronymic: str, organization: str, WorkinPhoneNumber: int, PersonalPhoneNumber: int): 
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.organization = organization
        self.WorkinPhoneNumber = WorkinPhoneNumber
        self.PersonalPhoneNumber = PersonalPhoneNumber
    '''Метод по изменению поля name'''
    def editPersonName(self, newName: str):
        self.name = newName
    
    '''Метод по изменению поля surname'''        
    def editPersonSurname(self, newSurname: str):
        self.surname = newSurname
        
    '''Метод по изменению поля patronymic'''        
    def editPersonPatronymic(self, newPatronymic: str):
        self.patronymic = newPatronymic
        
    '''Метод по изменению поля organization'''
    def editPersonOrganization(self, newOrganization: str):
        self.organization = newOrganization
    
    '''Метод по изменению поля WorkinPhoneNumber'''      
    def editPersonWorkinPhoneNumber(self, newWorkinPhoneNumbe: str):
        self.WorkinPhoneNumber = newWorkinPhoneNumbe
        
    '''Метод по изменению поля PersonalPhoneNumber'''    
    def editPersonPersonalPhoneNumber(self, newPersonalPhoneNumber: str):
        self.PersonalPhoneNumber = newPersonalPhoneNumber
    '''Метод для вывода информации о Person (в виде словаря)'''
    def getAllinfo(self):
        return {
            'Имя: ': self.name, 
            'Фамилия: ': self.surname, 
            'Отчество: ': self.patronymic, 
            'Имя организации: ': self.organization, 
            'Рабочий телефон: ': self.WorkinPhoneNumber, 
            'Личный телефон: ': self.PersonalPhoneNumber
        }