
import sqlite3
from sqlite3 import Error

def create():

    try: #ТАБЛИЦА СТУДЕНТЫ 
        c.execute("""CREATE TABLE студенты(
                            код_студента INTEGER PRIMARY KEY,
                            ФИО TEXT NOT NULL,
                            пол TEXT NOT NULL,
                            №комнаты INTEGER NOT NULL,
                            куратор TEXT NOT NULL,
                            дата_рождения TEXT NOT NULL,
                            домашний_адрес TEXT NOT NULL,
                            телефон INTEGER NOT NULL,
                            группа TEXT NOT NULL,
                            заселён TEXT NOT NULL)""")
    except:
        print("Ошибка создания таблицы 'студенты'")
        pass  
    

    try: #ТАБЛИЦА ЗАСЕЛЕНИЕ-ВЫСЕЛЕНИЕ
        c.execute("""CREATE TABLE  заселение_выселение(
                            код INTEGER PRIMARY KEY,
                            код_студента INTEGER,
                            дата_заселение TEXT,
                            дата_выселение TEXT,
                            №комнаты INTEGER,
                            FOREIGN KEY (код_студента) REFERENCES студенты (код_студента)            
                            );""")
                            
    except:
        print("Ошибка создания таблицы 'заселение_выселение'")
        pass


    try: #ТАБЛИЦА КОМНТАТЫ
        c.execute("""CREATE TABLE комнаты(
                            код INTEGER PRIMARY KEY,
                            №комнаты INTEGER NOT NULL,
                            мужская_женская TEXT NOT NULL,
                            количество_мест TEXT NOT NULL,
                            этаж INTEGER NOT NULL,
                            ремонт TEXT NOT NULL
                            );""")
    except:
        print("Ошибка создания таблицы 'комнаты'")
        pass


    try: #ТАБЛИЦА КУРАТОР
        c.execute("""CREATE TABLE куратор(
                            ФИО TEXT PRIMARY KEY,
                            телефон TEXT NOT NULL,
                            группа TEXT NOT NULL)""")
    except:
        print("Ошибка создания таблицы 'куратор'")
        pass


    try: #ТАБЛИЦА ГРУППЫ
        c.execute("""CREATE TABLE группы(
                            группа TEXT PRIMARY KEY)""")
    except:
        print("Ошибка создания таблицы 'группы'")
        pass    



def insert(): #TODO ЗАПИСЬ ДАННЫХ
    #  заселение_выселение
    data = [1, 234, "03.03.2021", "03.03.2021", 204, ] 
    c.execute("INSERT INTO заселение_выселение  VALUES(?,?,?,?,?);", ( data))

    # студенты
    data2 = [234, "Волков Семён Олегович", "м.", 204, "Антонова Яна Глебовна",
                "03.03.2021", "г. Жуково, ул. Павелецкая пл, дом 15", 87774, "ИС-18", "Да" ]

    c.execute("INSERT INTO студенты VALUES(?,?,?,?,?,?,?,?,?,?);", ( data2))

    #  комнаты
    data3 = [1, 234, "м.", "2/5", 2, "нет" ] 
    c.execute("INSERT INTO комнаты VALUES(?,?,?,?,?,?);", ( data3))

    #  куратор
    data4 = ["Антонова Яна Глебовна", "8967021323", "ИС-17-1" ] 
    c.execute("INSERT INTO куратор VALUES(?,?,?);", ( data4))

    #  группы
    data5 = ["ИС-18"] 
    c.execute("INSERT INTO группы VALUES(?);", ( data5))

  
    

def select(verbose=True): #*ВЫВОД В КОНСОЛЬ
    sql = "SELECT * FROM заселение_выселение"
    sql2 = "SELECT * FROM студенты"
    recs = c.execute(sql)
    recs2 = c.execute(sql2)
    if verbose:
        for row in recs:
            print (row)
    if verbose:
        for row2 in recs2:
            print (row2)


def create_connection(db_path): #!ПРОВЕРКА НА ОШИБКУ
    connection = None
    try:
        connection = sqlite3.connect(db_path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


db_path = r'D:\Work_R\Python\coursework\test.db'   
conn = sqlite3.connect(db_path)     #* осуществит подключение к файлу
c = conn.cursor()
create()
insert()
conn.commit() #сохранение изменений
select()
c.close()