def file_load():
  contact_info = []

  with open('contact-book.csv', 'r') as file:
    for row in file:
      lines = row.strip().split(', ')

      name = lines[0]
      number = lines[1]
      email = lines[2]
      address = lines[3]

      cbook = {
        'name': name,
        'number': int(number),
        'email': email,
        'address': address
      }
      contact_info.append(cbook)
  
  return contact_info