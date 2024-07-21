import json
import pandas as pd

# Функция для нахождения минимального набора признаков, уникально идентифицирующих каждую запись
def find_unique_identifiers(records):
    dataframe = pd.DataFrame(records)  # Преобразуем входные данные в DataFrame
    columns_list = dataframe.columns.tolist()  # Получаем список всех столбцов
    selected_columns = []  # Инициализируем список выбранных столбцов

    while True:
        optimal_column = None
        highest_unique_count = 0

        # Перебираем все столбцы, которые еще не были выбраны
        for column in columns_list:
            if column in selected_columns:
                continue

            # Текущая комбинация выбранных столбцов плюс текущий столбец
            current_columns = selected_columns + [column]
            # Считаем количество уникальных строк для текущей комбинации столбцов
            unique_count = dataframe[current_columns].drop_duplicates().shape[0]

            # Если количество уникальных строк больше, чем ранее найденное максимальное
            if unique_count > highest_unique_count:
                optimal_column = column  # Обновляем лучший столбец
                highest_unique_count = unique_count  # Обновляем максимальное количество уникальных строк

            # Если текущее количество уникальных строк равно общему числу строк в DataFrame, прерываем цикл
            if highest_unique_count == dataframe.shape[0]:
                break

        # Добавляем найденный лучший столбец к выбранным столбцам
        if optimal_column is not None:
            selected_columns.append(optimal_column)

        # Если текущее количество уникальных строк равно общему числу строк в DataFrame, прерываем цикл
        if highest_unique_count == dataframe.shape[0]:
            break

    return selected_columns  # Возвращаем список выбранных столбцов

# Основная функция, принимающая JSON-строку и возвращающая CSV-строку
def main(input_json):
    data = json.loads(input_json)  # Загружаем данные из JSON-строки
    unique_identifiers = find_unique_identifiers(data)  # Находим минимальный набор идентифицирующих признаков

    # Создаем DataFrame из найденных признаков
    result_dataframe = pd.DataFrame(unique_identifiers, columns=["Attributes"])
    # Преобразуем DataFrame в CSV-строку
    csv_output = result_dataframe.to_csv(index=False, encoding='utf-8')

    return csv_output  # Возвращаем CSV-строку

if __name__ == "__main__":
    file_path = 'data1.json'  # Укажите путь к вашему файлу JSON
    # Открываем файл и читаем его содержимое
    with open(file_path, 'r', encoding='utf-8') as file:
        json_content = file.read()
    # Вызываем основную функцию и печатаем результат
    print(main(json_content))