import sys

# Проверка на нужное колличество аргументов
if len(sys.argv) != 2:
    print("Укажи файл для анализа")
    sys.exit(1)


events = {
    "failed_password": [],
    "accepted_password": [],
    "accepted_key": [],
}
file = sys.argv[1]

with open(file, encoding="utf-8") as log_file:
    for line_number, line in enumerate(log_file, start=1):
        if "Failed password" in line: # неудачный вход
            events["failed_password"].append({f"line_number": line_number, "text": line.strip()})
        elif "Accepted password" in line: # удачный вход по паролю
            events["accepted_password"].append({f"line_number": line_number, "text": line.strip()})
        elif "Accepted publickey" in line: # удачный вход по ключу
            events["accepted_key"].append({f"line_number": line_number, "text": line.strip()})
        else:
            continue

# Вывод
print("-" * 100)
print(f"Краткий отчет:")
print(f"Неудачных входов: {len(events['failed_password'])}")
print(f"Успешных входов по паролю: {len(events['accepted_password'])}")
print(f"Успешных входов по ключу: {len(events['accepted_key'])}")
print("-" * 100)
