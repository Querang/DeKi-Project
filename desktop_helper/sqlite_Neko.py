import sqlite3
from sqlite3 import Error

import yaml


def delete_voice_commands(conn, command_name):
    """
    Delete a voice command by command name
    :param conn:  Connection to the SQLite database
    :param command_name: command name for the voice
    :return:
    """
    sql = 'DELETE FROM voice_commands WHERE command_name=?'
    cur = conn.cursor()
    cur.execute(sql, (command_name,))
    conn.commit()


def delete_voice_source(conn, bd_name):
    """
    Delete a task by voice command
    :param conn:  Connection to the SQLite database
    :param bd_name: command name for the voice
    :return:
    """
    sql = 'DELETE FROM voice_commands WHERE bd_name=?'
    cur = conn.cursor()
    cur.execute(sql, (bd_name,))
    conn.commit()


def update_active_voice(conn, bd_name, status):
    """обновляет статус голосовых команд"""
    cur = conn.cursor()
    sql = 'UPDATE voice_commands SET active = ? WHERE bd_name = ?'
    if status == 1:
        active = 0
        data = (active, bd_name)
        cur.execute(sql, data)
    else:
        active = 1
        data = (active, bd_name)
        cur.execute(sql, data)
    conn.commit()


def voice_commands_status(conn):
    """возвращает список статусов команд"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM voice_commands")
    rows = cur.fetchall()
    command = []
    for i in rows:
        command.append(i[2])
    return command


def voice_commands_names(conn):
    """возвращает названия команд"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM voice_commands")

    rows = cur.fetchall()
    command = []
    for i in rows:
        command.append(i[0])
    return command


def voice_commands_source(conn):
    """возвращает список команд, на которые ссылаются названия"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM voice_commands")

    rows = cur.fetchall()
    command = []
    for i in rows:
        command.append(i[:2])
    return command


def create_voice_com(conn, voice_commands):
    """
    Create a new project into the projects table
    :param conn:
    :param voice_commands:
    :return: project id
    """
    sql = ''' INSERT INTO voice_commands(command_name,bd_name,active)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, voice_commands)
    conn.commit()
    return cur.lastrowid


"""yaml"""


def read_config(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def write_config(file_path, config_dict):
    with open(file_path, "w") as f:
        yaml.dump(config_dict, f, default_flow_style=False)


"""sqlite"""


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


if __name__ == '__main__':
    pass
