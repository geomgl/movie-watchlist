import datetime
import sqlite3

connection = sqlite3.connect("data.db")

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies(
    title TEXT,
    release_timestamp REAL,
    watched INTEGER
);"""

ADD_MOVIE = "INSERT INTO movies VALUES (?, ?, 0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"
WATCH_MOVIE = "UPDATE movies SET watched = 1 WHERE title = ?;"


def create_table():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)

def add_movie(title, release_timestamp):
    with connection:
        connection.execute(ADD_MOVIE, (title, release_timestamp))

def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
    if upcoming:
        today = datetime.datetime.today().timestamp
        cursor.execute(SELECT_UPCOMING_MOVIES, (today,))
    else:
        cursor.execute(SELECT_UPCOMING_MOVIES)
    return cursor.fetchall()


def watch_movie(title):
    with connection:
        connection.execute(WATCH_MOVIE, (title,))
        

def get_watched_movies():
    with connection:
        # recall connection.execute returns a cursor
        return connection.execute(SELECT_WATCHED_MOVIES).fetchall


    
