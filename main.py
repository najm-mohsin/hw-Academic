# Step 1: Create a dictionary of textbooks and their costs
textbooks = {
    "Math": 250,
    "Physics": 300,
    "Chemistry": 280,
    "Biology": 260
}

# Step 2: Update the cost of the Physics book
textbooks["Physics"] = 200

# Step 3: Add 2 more books to the dictionary
textbooks["English"] = 220
textbooks["History"] = 240

# Step 4: Get the cost of a book entered by the user
book_name = input("Enter the name of the book: ")
if book_name in textbooks:
    print(f"The cost of {book_name} is {textbooks[book_name]}")
else:
    print(f"{book_name} is not available in the dictionary.")

# Step 5: Print all books and their costs
print("\nAll books and their costs:")
for book, cost in textbooks.items():
    print(f"{book}: {cost}")
