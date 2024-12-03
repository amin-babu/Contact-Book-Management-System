import add_contact
import view_contact
import remove_contact
import search_book
import load_file

contact_book = load_file.file_load()

while True:
  print('Welcome to Contact Book Management System')
  print('0. Exit')
  print('1. Add Contacts')
  print('2. View Contacts')
  print('3. Remove Contacts')
  print('4. Search Contacts')

  try:
    select = input('Select an option : ')
  except Exception as e:
    print(e)

  if select == '0':
    print('Thanks for using Contact Book Management System')
    break

  elif select == '1':
    contact_book == add_contact.include_contact(contact_book)
  
  elif select == '2':
    view_contact.view_all(contact_book)
  
  elif select == '3':
    contact_book = remove_contact.delete_contact(contact_book)

  elif select == '4':
    search_book.find_book(contact_book)
  
  else:
    print('Select valid Option')