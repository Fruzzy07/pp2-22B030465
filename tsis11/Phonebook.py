import psycopg2, csv
from config import data

config = psycopg2.connect(**data)
current = config.cursor()

insert = """
    INSERT INTO users VALUES(%s, %s) returning *;
"""

update = """
    UPDATE users SET phonenumber = %s WHERE name = %s;
"""

select = """
    SELECT * FROM users;
"""

delete = """
    DELETE FROM users WHERE name = %s;
"""



while True:
    command = input("insert, update, select, delete, exit\n")

    if command == 'insert':
        n = int(input("Если хотите загрузить с csv файла введите 1, иначе 2\n"))
        if n == 1:
            with open("c.csv", "r") as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    current.execute(insert, row)
            config.commit()
        if n == 2:
            name = (input("Введите имя:"))
            phonenumber = input("Введите номер:")
            current.execute(insert, (name, phonenumber))
            config.commit()

    if command == 'update':
        name = input("Введите имя:")
        phonenumber = input("Введите номер:")
        current.execute(update, (phonenumber, name))
        config.commit()
    if command == 'select':
        current.execute(select)
        print(*current.fetchall(), sep='\n')
        config.commit()
    if command == 'delete':
        name = input("Введите имя:")
        current.execute(delete, [name])
        config.commit()
    if command == 'exit':
        break

current.close()
config.commit()
config.close()