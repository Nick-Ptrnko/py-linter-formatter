'''
                ПРИКЛАД КОДУ З if-else ДЛЯ СЛОВНИКІВ
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

#                   ФУНКЦІЯ №1 З ЗАВДАННЯ
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








def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass


