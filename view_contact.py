def view_all(all_contacts):
  if all_contacts != []:
    for cbook in all_contacts:
      print(f"Name: {cbook['name']} | Number: {cbook['number']} | Email: {cbook['email']} | Address: {cbook['address']}\n")
  else:
    print('Empty Contact Book')
    return all_contacts