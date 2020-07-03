import datetime
import sqlite3

connection = sqlite3.connect("data.db")

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies(
    title TEXT,
    release_timestamp REAL
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched(
    username TEXT,
    title TEXT
);"""

ADD_MOVIE = "INSERT INTO movies VALUES (?, ?, 0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE username = ?;"
INSERT_WATCHED_MOVIE = "INSERT INTO watched VALUES (?, ?);"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(ADD_MOVIE, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
    if upcoming:
        today = datetime.datetime.today().timestamp()
        cursor.execute(SELECT_UPCOMING_MOVIES, (today,))
    else:
        cursor.execute(SELECT_ALL_MOVIES)
    return cursor.fetchall()


def watch_movie(username, title):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (username, title))


def get_watched_movies(username):
    with connection:
        # recall connection.execute returns a cursor
        return connection.execute(SELECT_WATCHED_MOVIES, (username,)).fetchall()
