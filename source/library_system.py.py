class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  
        lines = self.file.read().splitlines()
        print("List of Books: ")
        for line in lines:
            book_information = line.split(",")
            print(f"Book Title: {book_information[0]}, Author: {book_information[1]}")
            
    def add_book(self):
        title = input("Book Title: ")
        author = input("Book Author: ")
        release_year = input("Release Year: ")
        number_of_page = input("Number of Pages: ")
        book_information = f"{title},{author},{release_year},{number_of_page}\n"
        self.file.write(book_information)
        print("Book added. ")
        
    def remove_book(self):
           title_remove = input("Name of the book you want to remove: ")
           self.file.seek(0)
           lines = self.file.read().splitlines()
           index_remove = -1
           for i, line in enumerate(lines):
             if title_remove in line:
                index_remove = i
                break
            
             if index_remove != -1:
                del lines[index_remove]
                print(f"Book '{title_remove}' removed. ")
            
           else:
               print(f"Book '{title_remove}' not found. ")
               
               
           self.file.truncate(0)
           for line in lines:
               self.file.write(line+ '\n')
    
               
lib=Library()

while True:
    print("\n***MENU***\n")
    print("1)List Books:")
    print("2)Add Book:")
    print("3)Remove Book:")           
    print("4)Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
      lib.list_books()
       
    elif choice == "2":
       lib.add_book()
         
    elif choice == "3": 
       lib.remove_book()
         
    elif choice == "4":
        break 
     
    else:
        print("Invalid choice. Please try again.")