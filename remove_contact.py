import save_contact

def delete_contact(contacts):
  number = int(input('Enter number which you want to remove: '))
  for cbook in contacts:
    if cbook['number'] == number:
      contacts.remove(cbook)
      save_contact.save_file(contacts)
      print('Book removed Successfully')
      return contacts
  print('Empty Contact Book')
  return contacts