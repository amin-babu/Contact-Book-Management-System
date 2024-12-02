def find_book(contact_book):
  if contact_book != []:
    number = int(input('Enter book number which you want to search: '))
    found = False
    
    for cbook in contact_book:
      if cbook['number'] == number:
        found = True
        print(f"Here is the contact book:\nName: {cbook['name']} | Number: {cbook['number']} | Email: {cbook['email']} | Adress: {cbook['address']}")
        break
    if not found:
      print('Book Not Found')
  
  else:
    print('Empty Contact Book')





# def find_book(contact_book):
#     if contact_book != []:  # Check if the contact book is not empty
#         number = int(input('Enter book number which you want to search: '))
#         found = False  # Flag to track if the number is found

#         for cbook in contact_book:
#             if cbook['number'] == number:
#                 found = True
#                 print(f"Here is the contact book:\n"
#                       f"Name: {cbook['name']} | Number: {cbook['number']} | "
#                       f"Email: {cbook['email']} | Address: {cbook['address']}")
#                 break  # Exit the loop as we've found the contact book

#         if not found:
#             print('No Book Found')  # Message when the number is not found
#     else:
#         print('Empty Contact Book')  # Message when the contact book is empty












"""
def find_book(contact_book):
  if contact_book !=  []:
    number = int(input('Enter book number which you want to search : '))
    for cbook in contact_book:
      if cbook['number'] == number:
        print(f"Here is the contact book:\nName: {cbook['name']} | Number: {cbook['number']} | Email: {cbook['email']} | Adress: {cbook['address']}")

  else:
    print('Empty Contact Book')
"""