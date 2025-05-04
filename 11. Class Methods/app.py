class Book:
    total_books = 0  # Class variable to track total books
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Call class method when new book is created
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increment the class variable
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books  # Class method to get the total count

# Creating book instances
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Accessing the class variable through class method
print(f"Total books in library: {Book.get_total_books()}")