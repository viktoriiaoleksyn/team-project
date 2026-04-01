contacts = {}

while True:
    print("\n --- Меню ---")
    print("1 - Додати контакт")
    print("2 - Показати контакти")
    print("3 - Видалити контакт")
    print("4 - Вийти")

    choice = input("Вибір: ")
    if choice == "1":
        name = input("Введи ПІБ: ")
        number = input("Введи номер: ")
        contacts[name] = number

    elif choice == "2":
        if len(contacts) == 0:
            print("Список контактів пустий")
        else:
            print("\n Список контактів: ")
        for name, number in contacts.items():
            print(name,"-", number)
    elif choice == "3":
        name = input("Введи ПІБ контакту якого хочеш видалити: ")
        if name in contacts:
            del contacts[name]
            print("КОнтакт видалено")
        else:
            print("Такого контакту немає")

    elif choice == "4":
        print("Вихід з програми")
        break

    else:
        print("Неправильний вибір")

