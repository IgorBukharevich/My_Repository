import psycopg2


class FuncitonDataBase:
    """class FunctionDataBase"""

    @staticmethod
    def func_delete_database():
        """function join and deleted databases"""
        # Connect databases
        connect_db = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="",
            host="127.0.0.1",
            port="5432"
        )
        print("Database opened successfully")
        # we are making a request to delete data
        cur = connect_db.cursor()
        cur.execute("""DELETE FROM db_info.course WHERE course_id > 0;
                       DELETE FROM db_info.groups WHERE group_id > 0;
                       DELETE FROM db_info.teachers WHERE id > 0;
                       DELETE FROM db_info.students WHERE id > 0;               
                    """
                    )

        connect_db.commit()
        print("RECORD DELETED!!!")
        connect_db.close()

    @staticmethod
    def func_add_databases():
        """function join and add databases"""
        # Connect databases
        connect_db = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="",
            host="127.0.0.1",
            port="5432"
        )
        print("Database opened successfully\n")
        # making a request to add data
        cur = connect_db.cursor()
        cur.execute("""INSERT INTO db_info.teachers (first_name,last_name,email,telephone,specialized) VALUES
                       ('Simen', 'Afanasinov', 'afanasim@gmail.com', '+375291234565', 'Python-Developer'),
                       ('Maksim', 'Geronov', 'maksialt@gmail.com', '+375293222131', 'Java-Developer'),
                       ('Valodya', 'Fedorov', 'valodya.fe@gmail.com', '+375291234135', 'Back-end Developer'),
                       ('Viktoria', 'Cherkasova', 'vik.cher@gmail.com', '+375293453124', 'Frond-end Developer'),
                       ('Sysanna', 'Perepelka', 'sys.anna@gmail.com', '+375293453434', 'GemeDev');
                    
                       INSERT INTO db_info.students (first_name,last_name,email,telephone) VALUES
                       ('Oleg', 'Barabanov', 'baraban@gmail.com', '+375291234565'),
                       ('Afgustin', 'limonov', 'limon@gmail.com', '+375293222131'),
                       ('Petya', 'Fedorov', 'fedorov.p@gmail.com', '+375291234135'),
                       ('Alesya', 'Smirnova', 'alesya.smirnova@gmail.com', '+375293453124'),
                       ('Nina', 'Pavlovec', 'nina.pavl@gmail.com', '+375293453434');
                    
                       INSERT INTO db_info.groups
                       (name_group) VALUES
                       ('A-10'),
                       ('B-15'),
                       ('C-20'),
                       ('D-25'),
                       ('D-25');
                    
                    
                       INSERT INTO db_info.course
                       (name_course) VALUES
                       ('Python-Developer'),
                       ('Java-Developer'),
                       ('.NET-Developer'),
                       ('Learn DS&ML'),
                       ('C++ -Developer');              
                    """
                    )

        connect_db.commit()
        print("RECORDS ADD!")
        connect_db.close()

    @staticmethod
    def function_join_database():
        """function join table"""
        # Connect databases
        connect_db = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="",
            host="127.0.0.1",
            port="5432"
        )
        print("Database opened successfully\n")
        # request to merge tables
        cur = connect_db.cursor()
        cur.execute("""SELECT db_info.course.name_course,
                              db_info.groups.name_group
                       FROM db_info.groups
                       JOIN db_info.course on db_info.course.group_id = db_info.groups.group_id;
                    """
                    )
        # request data output
        rows = cur.fetchall()
        for row in rows:
            print("Course =", row[0])
            print("Group =", row[1], "\n")

        connect_db.commit()
        print("JOIN complete!!!")
        connect_db.close()

    @staticmethod
    def function_hwo_py_dev():
        """function find hwo python-developer """
        # connect databases
        connect_db = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="",
            host="127.0.0.1",
            port="5432"
        )
        print("Database opened successfully\n")
        # search request for a Python developer
        cur = connect_db.cursor()
        cur.execute("""SELECT db_info.students.first_name,
                       db_info.students.last_name,
                       db_info.course.course_id,
                       db_info.course.name_course
                       FROM db_info.students, db_info.course
                       WHERE db_info.course.name_course = 'Python-Developer';
                    """
                    )
        # request data output
        rows = cur.fetchall()
        for row in rows:
            print("First Name =", row[0])
            print("Last Name =", row[1])
            print("Course ID =", row[2])
            print("Course =", row[3], "\n")

        connect_db.commit()
        print("JOIN complete!!!")
        connect_db.close()


def main_run():
    """input output function"""
    str_menu = """+===============MENU===============+
|                                  |   
| 1: Add info DataBase             |
| 2: Clean FULL Table              |
| 3: JOIN                          |
| 4: who is our Python developer   |
| 5: Exit                          |
|                                  | 
+==================================+"""
    # created an instance of the class
    user = FuncitonDataBase()

    while True:
        print(str_menu)
        try:
            operation = int(input("Select operation: "))
            # checking whether the necessary commands are in the line
            if operation in (1, 2, 3, 4, 5):
                # checking if the user wants to log out
                if operation == 5:
                    print('Goodbye!')
                    break

                elif operation == 1:
                    user.func_add_databases()

                elif operation == 2:
                    user.func_delete_database()

                elif operation == 3:
                    user.function_join_database()

                elif operation == 4:
                    user.function_hwo_py_dev()
        except (ValueError, KeyboardInterrupt) as e:
            print(e)


main_run()
