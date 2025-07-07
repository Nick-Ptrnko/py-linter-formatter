'''
                ПРИКЛАД КОДУ з if-else ДЛЯ СЛОВНИКІВ
people = [
    {"name": "Ivan", "age": 18},
    {"name": "Mariia", "age":20},
    {"name": "Dariia", "age": 15}
]

def is_adult(age: int) -> str:
	if age >= 18:
		return  "Yes"
	else:
		return  "No"
adult = {person["name"]: is_adult(person["age"]) for person in people}
print(adult)
# {"Ivan"': "Yes", "Mariia": "Yes", "Dariia": "No"}
'''
'''
                ПРОСТІ ПРИКЛАДИ ПРАЦЮЮЧОГО КОДУ
def format_linter_error(error: dict) -> dict:
    return {key: value for key, value in error.items()}

    return {"name": value for key, value in error.items() if key == "code"}
'''
#       ФУНКЦІЯ ЗАМІНЯЄ ОДНЕ ЗНАЧЕННЯ КЛЮЧА НА ІНШЕ
#      ЯКЩО ЗНАЧЕННЯ ЯКЕ ПРИХОДИТЬ ВІДСУТНЄ, ВОНА ПОВЕРНЕ None
#     ПОТРІБНО ОБ'ЄДНАТИ ЦЮ ФУНКЦІЮ З ФУНКЦІЄЮ №1 З ЗАВДАННЯ ТА ЗРОБИТИ ЇЇ В ОДИН РЯДОК
def Changing_a_key(key:str) -> str:
    if key == "code":
        return "name"
    if key == "line_number":
        return "line"
    if key == "column_number":
        return "column"
    if key == "text":
        return "message"
    return None

#                   ФУНКЦІЯ №1 З ЗАВДАННЯ ЦЕ ОСТАННЄ ЩО ПОТРІБНО ЗРОБИТИ - ПЕРЕРОБИТИ ЇЇ
def format_linter_error(error: dict) -> dict:
    temp_data = {Changing_a_key(key): value
                 for key, value in error.items()
                 if Changing_a_key(key) is not None}
    # Розпаковуємо в потрібній послідовності
    return {
        "line": temp_data["line"],
        "column": temp_data["column"],
        "message": temp_data["message"],
        "name": temp_data["name"],
        "source": "flake8"  # Додаємо новий елемент
    }
#               Змінна для тестування першої функції
'''
error = {
    "code": "E501",
    "filename": "./source_code_2.py",
    "line_number": 18,
    "column_number": 80,
    "text": "line too long (99 > 79 characters)",
    "physical_line": '    return f"I like to filter, rounding, doubling, '
    "store and decorate numbers: {', '.join(items)}!\"",
}
print(format_linter_error(error=error))
'''

#           ФУНКЦІЯ №2 З ЗАВДАННЯ

def format_single_linter_file(file_path: str, errors: list) -> dict:
    if errors == []:
        status =  "passed"
    else:
        status = "failed"
    format_dict = {
        "errors": [format_linter_error(error) for error in errors],
        "path": file_path,
        "status": status,
    }
    return format_dict
'''
errors = [
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
         "text": "line too long (99 > 79 characters)",
        "physical_line": '    return f"I like to filter, rounding, doubling, ' 
        "store and decorate numbers: {', '.join(items)}!\"",
    },
    {
        "code": "W292",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 100,
        "text": "no newline at end of file",
        "physical_line": '    return f"I like to filter, rounding, doubling, '
        "store and decorate numbers: {', '.join(items)}!\"",
    },
]
errors = []

print(format_single_linter_file(file_path="./source_code_2.py", errors=errors))
'''
#           ФУНКЦІЯ №3 З ЗАВДАННЯ

def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(file_path, errors) for file_path, errors in linter_report.items()]

report_file = {
    "./test_source_code_2.py": [],
    "./source_code_2.py":
        [
            {
                "code": "E501",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 80,
                "text": "line too long (99 > 79 characters)",
                "physical_line": '    return f"I like to filter, rounding, doubling, '
                "store and decorate numbers: {', '.join(items)}!\"",
            },
            {
                "code": "W292",
                "filename": "./source_code_2.py",
                "line_number": 18,
                "column_number": 100,
                "text": "no newline at end of file",
                "physical_line": '    return f"I like to filter, rounding, doubling, '
                "store and decorate numbers: {', '.join(items)}!\"",
            },
        ]
}


print(format_linter_report(linter_report=report_file))

