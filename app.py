def show_menu():
    print("Show menu")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Quit")

def add_book(books):
    title = input("What's the title of the book?\n")
    genre = input ("What's the genre?\n")
    year = int(input("Year of publication?\n"))
    author = input ("What's the name of author?\n")
    read = input("Have you read this book? (yes/no)\n").lower() == "yes"

    new_book = {
        "Title":title,
        "Genre":genre,
        "Year of publication":year,
        "Author":author,
        "Have I read it":read
        }
    
    books.append(new_book)
    print(f"the book {new_book} added to your library.")

def remove_book(books):
    title = input("Enter the title of the book yoy want to remove.\n")

    for i , book in enumerate(books):
        if book["Title"].lower() == title.lower():
            del books[i]
            print(f"{title} removed!")
        return
    print("No book found with a title{title}.")

def search_book(books):
    print("Search by:")
    print("1. Title")
    print("2. Author")

    choice = input("Enter your choice:\n")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input! Please enter '1' for Title or '2' for Author.")
        return
    if choice == 1 :
        title = input("Enter the title:\n")
        found = False

        for book in books:
            if title.lower() in book['Title'].lower():
                print(f"Found: {book['Title']} by {book['Author']} ({book['Year of publication']}) - {book['Genre']} - {'Read' if book['Have I read it'] else 'Unread'}")
            found = True
        if not found:
            print(f"No books found with the title '{title}'.")

    elif choice == 2 :
        author = input("Enter the name of author: \n")
        found = False

        for book in books:
            if author.lower() in book['Author'].lower():
                print(f"Found: {book['Title']} by {book['Author']} ({book['Year of publication']}) - {book['Genre']} - {'Read' if book['Have I read it'] else 'Unread'}")
            found = True
        if not found:
            print(f"No books found by the author '{author}'.")
        
    else:
        print("Invalid choice! Please choose '1' for Title or '2' for Author.")


def display_book(books):
    if len(books) == 0:
        print("Your library is empty.")
    else:
        print("Your library:")
        for idx, book in enumerate(books, 1):
            read_status = "Read" if book["Have I read it"] else "Unread"
            print(f"{idx}. {book['Title']} by {book['Author']} ({book['Year of publication']}) - {book['Genre']} - {read_status}")

def main():
    books = []
    while True:
        show_menu()
        choice = input("Choose a option below:\n")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice! Please enter a number.")
            continue


        if choice == 1:
            add_book(books)
        elif choice == 2:
            remove_book(books)
        elif choice == 3:
            search_book(books)
        elif choice == 4:
            display_book(books)
        elif choice == 5:
            print("Good byeee!!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
