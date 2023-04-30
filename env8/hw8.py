import sqlite3


conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

print(f'Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, '
      f'для выхода из программы введите 0:')

def select_all(cursor):
    sql = '''SELECT * FROM cities'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
print(select_all(conn))



def get_employees_by_city(city_id):
    query = '''
        SELECT e.first_name, e.last_name, c.title, ct.title
        FROM employees e
        INNER JOIN cities ct ON e.city_id = ct.id
        INNER JOIN countries c ON ct.country_id = c.id
        WHERE e.city_id = ?
    '''
    cursor.execute(query, (city_id,))
    employees = cursor.fetchall()
    return employees

while True:
 city_id = int(input("Введите id города (или 0 для выхода): "))
 if city_id == 0:
    print("Программа завершена.")
    break
 else:
    city_id = int(city_id)
    employees = get_employees_by_city(city_id)
    print("Сотрудники, проживающие в выбранном городе:")
    for employee in employees:
        print("Имя:", employee[0])
        print("Фамилия:", employee[1])
        print("Страна:", employee[2])
        print("Город:", employee[3])
        print()

conn.close()

