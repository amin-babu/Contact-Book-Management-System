def file_load():
  contact_info = []

  with open('contact-book.csv', 'r') as file:
    for line in file:
      name, number, email, address = line.strip().split(', ')
      cbook = {
        'name': name,
        'number': int(number),
        'email': email,
        'address': address
      }
      contact_info.append(cbook)
  
  return contact_info