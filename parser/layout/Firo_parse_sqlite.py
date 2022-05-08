import sqlite3
import yaml
from sqlite3 import Error

"""yaml"""


def read_config(file_path):
    try:
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
    except:
        print("mistake")  # here will be append dialog window with mistake


def write_config(file_path, config_dict):
    try:
        with open(file_path, "w") as f:
            yaml.dump(config_dict, f, default_flow_style=False)
    except:
        print("mistake")


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def add_received_data(conn, parser_data):
    sql = ''' INSERT INTO parser_label_data(tag,class,id_html,mark,action,action_value,notify,notify_time,pause)
                  VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, parser_data)
    conn.commit()
    return cur.lastrowid


def delete_label(conn, id):
    sql = 'DELETE FROM parser_label_data WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def return_content(conn, id_label):
    cur = conn.cursor()
    cur.execute("SELECT * FROM parse_content WHERE id_content =?", (id_label,))
    parse_date_container = cur.fetchall()
    return parse_date_container


def add_content(conn, list_content):
    id = list_content[0][0]
    sql = 'DELETE FROM parse_content WHERE id_content=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    for i in list_content:
        sql = ''' INSERT INTO parse_content(id_content,text_content,time_parse)
                          VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, tuple(i))

        conn.commit()


def del_content(conn, id):
    sql = 'DELETE FROM parse_content WHERE id_content=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def del_content_by_time(conn, id,time):
    sql = 'DELETE FROM parse_content WHERE id_content=? AND time_parse =?'
    cur = conn.cursor()
    cur.execute(sql, (id,time))
    conn.commit()

def update_label(conn,id_label,notify,notify_time,pause):
    sql = ''' UPDATE parser_label_data
                  SET notify = ? ,
                      notify_time = ?,
                      pause = ?
                  WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (notify,notify_time,pause,id_label))
    conn.commit()

if __name__ == "__main__":
    conn = create_connection("parse_.db")
    with conn:
        update_label(conn,16,None,"1 hour","True")
