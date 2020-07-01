import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_table()
user_input = input(menu)

def prompt_add_movie():
    title = input("Enter movie title: ")
    release_date = input("Insert movie release date (mm-dd-YYYY): ")
    parsed_datetime = datetime.datetime.strptime(release_date, "%m-%d-%Y")
    timestamp = parsed_datetime.timestamp()

    database.add_movie(title, timestamp)

def print_movies(heading, movies):
    print(f" ----- {heading} movies ----- ")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%b-%d-%Y")
        print(f"-- {movie[0]} (released on {human_date})")
    print("\n")
        

def watch_movie():
    movie = input("What movie did you watch? ")
    database.watch_movie(movie)


while user_input != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movies('Upcoming', movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movies('All', movies)
    elif user_input == "4":
        watch_movie()
    elif user_input == "5":
        movies = database.get_watched_movies()
        print_movies('Watched', movies)
    else:
        print("Invalid input, please try again!")

    user_input = input(menu)