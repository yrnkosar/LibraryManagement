class Library:
    def __init__(self, database_path='books.txt'):
        self.database_path = database_path
        self.file = open(self.database_path, 'a+')

    def __del__(self):
        self.file.close()
    #code change for control difference
    def add_book(self, title, author, releasedate, page):
        if title.strip() == "" or author.strip() == "" or releasedate.strip() == "" or page.strip() == "":
            print("Values cannot be null!")
        else:
            if releasedate.isnumeric() and page.isnumeric():
                with open(self.database_path, 'r') as file:
                    existing_titles = [line.split(',')[0].strip() for line in file.readlines()]

                if title.strip() in existing_titles:
                    print(f"{title} is already in the library. Returning to the main menu.")
                    return

                with open(self.database_path, 'a') as file:
                    file.write(f"{title},{author},{releasedate},{page},available\n")
                print(f"{title} by {author} {releasedate} {page} has been added to the library.")
            else:
                print("Release Date/Page are allowed only numeric characters.")

    def list_books(self):
        with open(self.database_path, 'r') as file:
            for line in file:
                title, author, releasedate, page, status = line.strip().split(',')
                print(f"Title: {title}, Author: {author}, Release Date: {releasedate}, Pages: {page}, Available: {status}")

    def check_in_book(self, title):
        lines_to_write = []

        with open(self.database_path, 'r') as file:
            lines = file.readlines()

        found = False
        for line in lines:
            current_title, author, releasedate, page, status = line.strip().split(',')
            if current_title.strip() == title.strip():
                found = True
                if status.strip() == 'unavailable':
                    line = line.replace("unavailable", "available")
                    print(f"{title} has been checked in.")
                else:
                    print(f"{title} is already available.")
            lines_to_write.append(line)

        if not found:
            print(f"{title} is not found in the library.")

        with open(self.database_path, 'w') as file:
            file.writelines(lines_to_write)

    def check_out_book(self, title):
        lines_to_write = []

        with open(self.database_path, 'r') as file:
            lines = file.readlines()

        found = False
        for line in lines:
            current_title, author, releasedate, page, status = line.strip().split(',')
            if current_title.strip() == title.strip():
                found = True
                if status.strip() == 'available':
                    line = line.replace("available", "unavailable")
                    print(f"{title} has been checked out.")
                else:
                    print(f"{title} is already checked out.")
            lines_to_write.append(line)

        if not found:
            print(f"{title} is not found in the library.")

        with open(self.database_path, 'w') as file:
            file.writelines(lines_to_write)

    def remove_book(self, title):
        try:
            with open(self.database_path, 'r') as file:
                lines = file.readlines()

            with open(self.database_path, 'w') as file:
                a = False
                for line in lines:
                    if title != line.split(",")[0]:
                        file.write(line)
                    else:
                        a = True
                        print(f"{title} has been removed from the library.")
                if not a:
                    print(f"{title} is not found in the library")
        except FileNotFoundError:
            print("File not found.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. List Books")
        print("2. Add Book")
        print("3. Check Out Book")
        print("4. Check In Book")
        print("5. Remove Book")
        print("Q. Quit")

        choice = input("Enter your choice : ")

        if choice == '1':
            library.list_books()
        elif choice == '2':
            title = input("Enter the title of the book: ")

            # Check if the title already exists
            with open(library.database_path, 'r') as file:
                existing_titles = [line.split(',')[0].strip() for line in file.readlines()]

            if title.strip() in existing_titles:
                print(f"{title} is already in the library. Returning to the main menu.")
                continue  # Return to the main menu without adding the book

            # If the title is unique, proceed to add the book
            library.add_book(title, input("Enter the author of the book: "),
                             input("Enter the release date of the book: "),
                             input("Enter the number of pages: "))

        elif choice == '3':
            title = input("Enter the title of the book to check out: ")
            library.check_out_book(title)

        elif choice == '4':
            title = input("Enter the title of the book to check in: ")
            library.check_in_book(title)

        elif choice == '5':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == 'Q' or choice == 'q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid character.")


if __name__ == "__main__":
    main()
