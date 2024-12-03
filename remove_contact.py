import save_contact

def delete_contact(contacts):
  if contacts != []:
    try:
      number = int(input('Enter number which you want to remove : '))
    except ValueError:
      print('The phone number must be an integer')
      return contacts
    for cbook in contacts:
      if cbook['number'] == number:
        contacts.remove(cbook)
        save_contact.save_file(contacts)
        print('Book removed Successfully')
        return contacts
  print('Empty Contact Book')
  return contacts