books = {}

while True:
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Remove Book")
    print("7. Out of Stock Books")
    print("8. Total Books Available")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = input("Enter Book ID: ")

        if book_id in books:
            print("Book Already Exists.")
        else:
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            quantity = int(input("Enter Quantity: "))

            books[book_id] = {
                "Title": title,
                "Author": author,
                "Quantity": quantity
            }

            print("Book Added Successfully.")

    elif choice == 2:
        if len(books) == 0:
            print("No Books Available.")
        else:
            for bid, data in books.items():
                print("----------------------------------")
                print("Book ID:", bid)
                print("Title:", data["Title"])
                print("Author:", data["Author"])
                print("Quantity:", data["Quantity"])

    elif choice == 3:
        key = input("Enter Book ID or Title: ")

        found = False

        for bid, data in books.items():
            if bid == key or data["Title"].lower() == key.lower():
                print("----------------------------------")
                print("Book ID:", bid)
                print("Title:", data["Title"])
                print("Author:", data["Author"])
                print("Quantity:", data["Quantity"])
                found = True

        if not found:
            print("Book Not Found.")

    elif choice == 4:
        bid = input("Enter Book ID: ")

        if bid in books:
            if books[bid]["Quantity"] > 0:
                books[bid]["Quantity"] -= 1
                print("Book Issued Successfully.")
            else:
                print("Book Out of Stock.")
        else:
            print("Book Not Found.")

    elif choice == 5:
        bid = input("Enter Book ID: ")

        if bid in books:
            books[bid]["Quantity"] += 1
            print("Book Returned Successfully.")
        else:
            print("Book Not Found.")

    elif choice == 6:
        bid = input("Enter Book ID: ")

        if bid in books:
            del books[bid]
            print("Book Removed Successfully.")
        else:
            print("Book Not Found.")

    elif choice == 7:
        print("Out of Stock Books")

        found = False

        for bid, data in books.items():
            if data["Quantity"] == 0:
                print(data["Title"])
                found = True

        if not found:
            print("No Out of Stock Books.")

    elif choice == 8:
        total = 0

        for data in books.values():
            total += data["Quantity"]

        print("Total Books Available:", total)

    elif choice == 9:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")