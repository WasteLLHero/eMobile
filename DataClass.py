from faker import Faker
import pandas as pd


class Data:
    def __init__(self, dataFrame = pd.DataFrame() ):
        self.dataFrame = dataFrame
    def readDataFrame(self):
        return self.dataFrame
    def createInfo(self, path = 'info.csv', Delimiter = ','):
        dataFrame = pd.read_csv(path, delimiter=Delimiter)
        fake = Faker()
        dataFrame['Имя организации'] = [fake.company() for _ in range(len(dataFrame))]
        print(dataFrame)
        return dataFrame
    def readData(self, path, Delimiter = ','):
        dataFrame = pd.read_csv(path, delimiter=Delimiter)
        return dataFrame
    def write_to_dataframe(self, mobile_directory):
        df = pd.DataFrame(mobile_directory.getInfoAboutPersons()).transpose()
        df.columns = [col.replace(': ', '') for col in df.columns]
        self.dataFrame = df
    def save_to_csv(self, path = 'info.csv'):
        self.dataFrame.to_csv(path, index=False)