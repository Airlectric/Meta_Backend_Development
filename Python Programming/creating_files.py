try:
    with open('new_file.txt', mode = 'w') as file:
        file.writelines(['\nThis is a newly created file', '\nJust included a new line of text'])
except FileNotFoundError as e:
    print(e ,': File not found')
