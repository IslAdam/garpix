import json
import pandas as pd


def find_minimal_identifiers(data):
    df = pd.DataFrame(data)
    columns = df.columns.tolist()
    selected_columns = []

    while True:
        best_column = None
        best_uniq_count = 0

        for column in columns:
            if column in selected_columns:
                continue

            current_columns = selected_columns + [column]
            uniq_count = df[current_columns].drop_duplicates().shape[0]

            if uniq_count > best_uniq_count:
                best_column = column
                best_uniq_count = uniq_count

            if best_uniq_count == df.shape[0]:
                break

        if best_column is not None:
            selected_columns.append(best_column)

        if best_uniq_count == df.shape[0]:
            break

    return selected_columns


def main(json_str):
    data = json.loads(json_str)
    minimal_identifiers = find_minimal_identifiers(data)

    result_df = pd.DataFrame(minimal_identifiers, columns=["Признаки"])
    csv_result = result_df.to_csv(index=False, encoding='utf-8')

    return csv_result


if __name__ == "__main__":
    file_path = 'data1.json'  # Укажите путь к вашему файлу JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        json_str = file.read()
    print(main(json_str))
