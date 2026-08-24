# Write a function called favorite_book() that accepts one parameter, title. The function should 
# print a message, such as One of my favorite books is Alice in Wonderland. Call the function, 
# making sure to include a book title as an argument in the function call.

def favorite_book(book):
    print(f"\nMy favourite book is {book.title()}\n")
    
favorite_book("Alice in wonderland")
