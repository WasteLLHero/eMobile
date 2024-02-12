import pandas as pd

# Создаем пример DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank'],
        'Age': [25, 30, 35, 40, 45, 50],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia']}

df = pd.DataFrame(data)

# Функция для получения страницы из DataFrame
def get_page(dataframe, page_number, page_size):
    start_idx = (page_number-1) * page_size
    end_idx = start_idx + page_size
    page = dataframe.iloc[start_idx:end_idx]
    return page

# Номер страницы, который хотите получить
page_number = 2
# Размер страницы
page_size = 4

# Получаем страницу из DataFrame
result_page = get_page(df, page_number, page_size)
print(result_page)
print(df)
