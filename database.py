from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('/home/seraphina/Documents/TRAINING/training_2019/PACKT/the_ultimate_flask_course/4_Food_Tracker_App/food_log.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db