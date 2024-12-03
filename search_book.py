def find_book(contact_book):
  if contact_book != []:
    try:
      number = int(input('Enter book number which you want to search: '))
    except ValueError:
      print('The phone number must be an integer')
      return contact_book
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