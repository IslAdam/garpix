import json
import itertools
import pandas as pd


def is_unique_combination(data, combination):
    seen = set()
    for entry in data:
        try:
            identifier = tuple(entry[key] for key in combination)
        except KeyError:
            return False
        if identifier in seen:
            return False
        seen.add(identifier)
    return True


def find_minimal_unique_combination(data):
    keys = list(data[0].keys())
    for r in range(1, len(keys) + 1):
        for combination in itertools.combinations(keys, r):
            if is_unique_combination(data, combination):
                return combination
    return keys


def main(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    minimal_combination = find_minimal_unique_combination(data)
    print(f"Minimal unique combination found: {minimal_combination}")
    df = pd.DataFrame(minimal_combination, columns=['Признак'])
    output_csv = df.to_csv(index=False, encoding='utf-8')

    # Save to file
    with open('output.csv', 'w', encoding='utf-8') as f:
        f.write(output_csv)

    return output_csv


if __name__ == "__main__":
    json_file_path = 'data.json'
    csv_output = main(json_file_path)
    print(csv_output)