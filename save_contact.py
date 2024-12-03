def save_file(file_list):
  with open('contact-book.csv', 'w') as file:
    for cbook in file_list:
      line = f"{cbook['name']}, {cbook['number']}, {cbook['email']}, {cbook['address']}\n"
      file.write(line)

