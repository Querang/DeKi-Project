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
    sql = ''' INSERT INTO parser_label_data(url,tag,class,id_html,mark,action,action_value,notify,notify_time)
                  VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, parser_data)
    conn.commit()
    return cur.lastrowid


def get_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM parser_label_data ")
    date_container = cur.fetchall()
    # print(book_date)
    return date_container


def delete_label(conn, id):
    sql = 'DELETE FROM parser_label_data WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


if __name__ == "__main__":
    conn = create_connection("parse_.db")
    with conn:
        print(get_data(conn))
