import save_contact

def include_contact(contact_list):

  name = input('Enter your Name : ')
  try:
    number = int(input('Enter your Number : '))
  except ValueError:
    print('The phone number must be an integer')
    return contact_list

  for contact in contact_list:
    if number == contact['number']:
      print('This phone number is already assigned')
      return contact_list
  
  email = input('Enter your Email : ')
  address = input('Enter your address : ')

  cbook = {
    'name' : name,
    'number' : number,
    'email' : email,
    'address' : address
  }

  contact_list.append(cbook)
  save_contact.save_file(contact_list)
  print('Contact Added Successfully')
  return contact_list