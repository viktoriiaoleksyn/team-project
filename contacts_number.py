contacts = []

while True:
    print("\n1 - Додати контакт")
    print("2 - Показати контакти")
    print("3 - Вийти")

    choice = input("Вибір: ")
    if choice == "1":
        number = input("Введи номер: ")
        contacts.append(number)

    elif choice == "2":
        for contact in contacts:
            print(contact)
    elif choice == "3":
            break