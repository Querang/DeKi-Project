import sqlite3
from sqlite3 import Error
import json
import yaml

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


def del_books(conn, list_del):
    for i in list_del:
        sql = 'DELETE FROM warehouse WHERE id_book=?'
        cur = conn.cursor()
        cur.execute(sql, (i,))
    conn.commit()


def del_folder(conn, id_folder):
    sql = 'DELETE FROM bookshelf WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id_folder,))
    conn.commit()


def create_folder(conn, folder):
    sql = ''' INSERT INTO bookshelf(folder)
                  VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (folder,))
    conn.commit()
    return cur.lastrowid


def get_id_folder(conn, name_folder):
    cur = conn.cursor()
    cur.execute("SELECT id FROM bookshelf WHERE folder =?", (name_folder,))
    id_container = cur.fetchall()
    id_date = id_container[-1][0]
    # print(id_date)
    return id_date


def create_book(conn, book_date):
    sql = ''' INSERT INTO warehouse(id,book_name,book_path,book_image_path,current_page)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, book_date)
    conn.commit()
    return cur.lastrowid


def get_book(conn, id_book):
    cur = conn.cursor()
    cur.execute("SELECT * FROM warehouse WHERE id_book =?", (id_book,))
    book_date_container = cur.fetchall()
    book_date = book_date_container[0]
    # print(book_date)
    return book_date[1:]


def get_list_book_id(conn, id_folder):
    """получить list id book по id книги"""
    cur = conn.cursor()
    cur.execute("SELECT id_book FROM warehouse WHERE id = ? ", (id_folder,))
    book_list_id_container = cur.fetchall()
    book_list_id = []
    for i in book_list_id_container:
        book_list_id.append(i[0])
    # print(book_list_id)
    return book_list_id


def get_all_folder_and_id(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookshelf ")
    all_folder_container = cur.fetchall()
    date = []
    for i in all_folder_container:
        date.append(i)
    # print(date)
    return date


def get_all_book(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM warehouse  ")
    book_list_container = cur.fetchall()
    return book_list_container


def main():
    conn = create_connection("lib.db")
    with conn:
        # create_folder(conn, "qq")
        # add_book_list_id(conn, 3, "21")
        print(get_book(conn,10))
        # get_id_folder(conn, "undefined")
        # get_all_folder_and_id(conn)
        # get_list_book_id(conn,3)
        # del_books(conn,[1])
        # get_all_book(conn)
        # update_book_list_id(conn,3,[7])

        pass


if __name__ == "__main__":
    main()
