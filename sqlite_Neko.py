import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def crate_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_task(conn, task):
    """
    Create a new project into the projects table
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' INSERT INTO tasks(type,file0,file1,file2,file3,site,command)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def select_last_task(conn):
    """
    Query tasks by priority
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("""SELECT * 
                    FROM    tasks 
                    WHERE   ID = (SELECT MAX(ID)  FROM tasks)""")
    row = cur.fetchall()
    #[()]
    id = row[0][0]

    return id

def select_all_command(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    command = []
    for i in rows:
        command.append(i[3])
    return command

def delete_task(conn, command):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param command: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE command=?'
    cur = conn.cursor()
    cur.execute(sql, (command,))
    conn.commit()

def select_task_by_command(conn, command):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE command=?", (command,))

    row = cur.fetchall()
    return row

def main():
    conn = create_connection("other_file/Neko.db")
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        type text,
                                        path_0 text ,
                                        path_1 text ,
                                        path_2 text ,
                                        command text   
                                    );"""
    task = (1,"f",'www','www')
    if conn is not None:
        create_task(conn, sql_create_tasks_table)



if __name__ == '__main__':
    main()
