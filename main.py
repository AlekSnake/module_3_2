# 1 пункт Задачи. Создаем функцию send_email, которая принимает 2 обычных аргумента: сообщение (message) и получатель
# (recipient) и 1 обязательно именованный аргумент со значением по умолчанию - отправитель (sender).
def send_email(message, recipient, sender="university.help@gmail.com"):
    # Логика 1. Проверка на корректность e-mail отправителя и получателя.
    # 2 пункт Задачи. Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
    # то выводится на экран (в консоль) строка: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>."
    if '@' not in recipient or not recipient.endswith(
            ('.com', '.ru', '.net')) or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")

    # Логика 2. Проверка на отправку самому себе.
    # 3 пункт Задачи. Если же sender и recipient совпадают, то выводится "Нельзя отправить письмо самому себе!"
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")

    # Логика 3. Проверка на отправителя по умолчанию.
    # 4 пункт Задачи. Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение:
    # "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    # 5 пункт Задачи. В противном случае вывести сообщение:
    # "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")