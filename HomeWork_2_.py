import json
import sqlite3
import os
from pprint import pprint


class Filmsql:

    def __init__(self):
        self.conn = None
        self.curs = None

    def sql_connect(self):
        databazasql = os.path.join(os.getcwd(), "database", 'film_data.db')
        try:
            conn = sqlite3.connect(databazasql)

        except:
            raise
        self.conn = conn
        self.curs = conn.cursor()

    def sql_select(self):
        self.sql_connect()
        select = """SELECT title FROM film_data WHERE title like "B%" """
        result = self.curs.execute(select)
        self.conn.commit()
        return result.fetchall()

    def sql_select_max(self):
        self.sql_connect()
        select = """SELECT * FROM film_data  WHERE length=(SELECT MAX(length) FROM film_data)  """
        result =self.curs.execute(select)
        self.conn.commit()
        return result.fetchall()

    def sql_in_json(self):
        self.sql_connect()
        select = """SELECT * FROM film_data  """
        result_1 = self.curs.execute(select)
        with open("sql_json.json", "w") as sql_json:
            json.dump(result_1.fetchall(), sql_json, indent=4)
        self.conn.commit()

    def filtered_film(self):
        self.sql_connect()
        select_2 = """SELECT * FROM film_data Where release_year>2010 and length between 100 and 180"""
        result = self.curs.execute(select_2)
        self.conn.commit()
        with open("database/filtered_film.db", "w"):
            database = os.path.join(os.getcwd(), 'database', "filtered_film.db")
            conn = sqlite3.connect(database)
            curs = conn.cursor()
            user_table_create = """ CREATE TABLE IF NOT EXISTS filtered_film (
                                                    film_id integer,
                                                    title text ,
                                                    description text ,
                                                    release_year integer,
                                                    length integer,
                                                    rate text,
                                                    special_features text
                                                ); """
            curs.execute(user_table_create)
            insert_sql = """ INSERT INTO filtered_film(film_id, title, description, 
                            release_year, rate, length, special_features)
                            VALUES(:film_id,:title,:description,:release_year,:rate,:length,:special_features);
                            """
            for i in result.fetchall():
                curs.execute(insert_sql, i)
                conn.commit()


a = Filmsql()

pprint(a.filtered_film())
# pprint(a.sql_select_max())
# pprint(a.sql_select())
# pprint(a.sql_in_json())