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


def get_paths_character(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM character_path WHERE name=?",(name,))
    rows = cur.fetchall()
    row = None
    for i in rows:
        row = i
    return row
def update_global_name(conn,names):
    cur = conn.cursor()
    sql = ''' UPDATE global_setting
                  SET view_character = ? ,
                      name_character = ? ,
                      name_user = ? ,
                      language = ? ,
                      behavior = ?
                      '''
    cur.execute(sql, names)
    conn.commit()

def get_names_character(conn):
    cur = conn.cursor()
    cur.execute("SELECT name FROM character_path ")
    rows = cur.fetchall()
    row = []
    print(rows)
    for i in rows:
        row.append(i[0])
    return row

def get_global_name(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM global_setting")
    rows = cur.fetchall()
    row = None
    print(rows)
    for i in rows:
        row=i

    return row


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
        command.append(i[-1])
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
    conn = create_connection("Neko.db")
    names = ("Firo","Filorial","семпай","russian","waify")
    with conn:
        update_global_name(conn,names)


if __name__ == '__main__':
    main()
