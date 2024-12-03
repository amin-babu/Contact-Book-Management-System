import save_contact

def delete_contact(contacts):
  if contacts != []:
    try:
      number = int(input('Enter number which you want to remove : '))
    except Exception as e:
      print(e)
      return contacts
    found = False
    for cbook in contacts:
      if cbook['number'] == number:
        found = True
        contacts.remove(cbook)
        save_contact.save_file(contacts)
        print('Book removed Successfully')
        return contacts
    if not found:
      print('Book Not Found')
      return contacts
  else:
    print('Empty Contact Book')
    return contacts