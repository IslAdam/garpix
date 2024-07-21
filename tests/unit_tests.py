import unittest
import json
from app import find_unique_identifiers, main

class TestUniqueIdentifiers(unittest.TestCase):
    def test_find_unique_identifiers(self):
        data = [
            {"фамилия": "Иванов", "имя": "Иван", "отчество": "Иванович", "класс": "5"},
            {"фамилия": "Петров", "имя": "Петр", "отчество": "Петрович", "класс": "5"},
            {"фамилия": "Сидоров", "имя": "Сидор", "отчество": "Сидорович", "класс": "6"},
        ]
        result = find_unique_identifiers(data)
        self.assertIn("фамилия", result)
        self.assertEqual(len(result), 1)

    def test_main(self):
        json_str = '[{"фамилия": "Иванов", "имя": "Иван", "отчество": "Иванович", "класс": "5"}, {"фамилия": "Петров", "имя": "Петр", "отчество": "Петрович", "класс": "5"}, {"фамилия": "Сидоров", "имя": "Сидор", "отчество": "Сидорович", "класс": "6"}]'
        result_csv = main(json_str)
        expected_csv = "Attributes\nфамилия\n"
        self.assertEqual(result_csv.replace('\r\n', '\n').strip(), expected_csv.replace('\r\n', '\n').strip())

if __name__ == "__main__":
    unittest.main()
