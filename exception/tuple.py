try:
    with open('notfound.py') as file:
        print(file.read())
except (FileNotFoundError,):
    print('file tidak ditemukan')
