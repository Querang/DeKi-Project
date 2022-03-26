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

def get_note_list(conn,current_folder):
    cur = conn.cursor()
    cur.execute("SELECT object_name FROM note WHERE work_table =? ", (current_folder,))
    rows = cur.fetchall()
    list_objiect_name = []
    for i in rows:
        list_objiect_name.append(i[0])
    cur = conn.cursor()
    cur.execute("SELECT note FROM note WHERE work_table =? ", (current_folder,))
    rows = cur.fetchall()
    list_all_note = []
    for i in rows:
        list_all_note.append(i[0])

    return (list_all_note,list_objiect_name)

def create_note(conn, notet):
    """
    Create a new project into the projects table
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' INSERT INTO note(work_table,object_name,note)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, notet)
    conn.commit()


def note_button_up(conn,current_folder,object_name):
    cur = conn.cursor()
    cur.execute("SELECT note FROM note WHERE work_table =? and object_name = ? ", (current_folder,object_name))
    rows = cur.fetchall()
    row = rows[0]
    print(row)
    return row


def save_note_sq(conn,note):
    cur = conn.cursor()
    sql = ''' UPDATE note
                      SET work_table = ? ,
                          object_name = ? ,
                          note = ? 
                      WHERE work_table = ? and
                            object_name = ?    
                          '''
    cur.execute(sql, note)
    conn.commit()


def get_paths_character(conn, name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM character_path WHERE name=?", (name,))
    rows = cur.fetchall()
    row = None
    for i in rows:
        row = i
    return row


def update_global_name(conn, names):
    cur = conn.cursor()
    sql = ''' UPDATE global_setting
                  SET view_character = ? ,
                      name_character = ? ,
                      name_user = ? ,
                      language = ? ,
                      behavior = ? ,
                      work_table_note = ? ,
                      main_window_size = ?
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
        row = i

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


def reset_button_note(conn, work_table,current_button):
    cur = conn.cursor()
    cur.execute("SELECT note FROM note WHERE work_table =? ", (work_table,))
    rows = cur.fetchall()
    list_all_note = []
    for i in rows:
        list_all_note.append(i[0])
    print(list_all_note)
    print(current_button)
    current_button = int(current_button)
    for i in range(len(list_all_note) - current_button):
        note = (work_table, f"{current_button}", list_all_note[current_button], work_table, f"{current_button + 1}")
        print(note, "qq")
        sql1 = ''' UPDATE note
                                  SET work_table = ? ,
                                      object_name = ? ,
                                      note = ? 
                                  WHERE work_table = ? and
                                      object_name = ? 
                                      '''
        current_button += 1
        cur.execute(sql1, note)


def delete_note(conn, work_table,current_button):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param command: id of the task
    :return:
    """
    cur = conn.cursor()
    sql = 'DELETE FROM note WHERE work_table=? and object_name=?'
    cur.execute(sql, (work_table,current_button))
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


def select_type_of_commands(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    types = []
    for i in rows:
        types.append(i[0])
    return types


def select_files_of_commands(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    file_commands = []
    for i in rows:
        ways = []
        ways.append(i[1])
        ways.append(i[2])
        ways.append(i[3])
        ways.append(i[4])
        ways = tuple(ways)
        file_commands.append(ways)
    return file_commands


def select_sites_of_command(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    sites = []
    for i in rows:
        sites.append(i[5])
    return sites


def main():
    conn = create_connection("Neko.db")
    names = ("Firo", "Filorial", "семпай", "russian", "waify")
    with conn:
        note_button_up(conn,"Note","2")


if __name__ == '__main__':
    main()
