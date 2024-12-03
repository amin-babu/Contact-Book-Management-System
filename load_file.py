import os

def file_load():
  contact_info = []

  if not os.path.exists('contact-book.csv'):
    return contact_info

  try:
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
  
  except Exception as e:
    print(f"Error loading file: {e}")
  
  return contact_info