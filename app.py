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
database.create_tables()
user_input = input(menu)

while user_input != "6":
    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("Invalid input, please try again!")

    user_input = input(menu)