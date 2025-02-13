from data import *
from welcome import *
from linkedlist import LinkedList

print_welcome()

def insert_movie_genres():
    movie_genre_list = LinkedList()
    for movie_genre in genres:
        movie_genre_list.insert_beginning(movie_genre)
    return movie_genre_list

def insert_movie_data():
    movie_data_list = LinkedList()
    for movie_genre in genres:
        movie_sublist = LinkedList()
        for movie in movie_data:
            if movie[0] == movie_genre:
                movie_sublist.insert_beginning(movie)
        movie_data_list.insert_beginning(movie_sublist)
    return movie_data_list

my_genre_list = insert_movie_genres()
my_movie_list = insert_movie_data()

selected_movie_genre = ""

while len(selected_movie_genre) == 0:
    user_input = str(input("\nWhat movie genre would you like to watch?\nType the beginning of that movie genre and press enter to see if it's here.\n")).lower()

    matching_genres = []
    genre_list_head = my_genre_list.get_head_node()
    while genre_list_head is not None:
        if str(genre_list_head.get_value()).startswith(user_input):
            matching_genres.append(genre_list_head.get_value())
        genre_list_head = genre_list_head.get_next_node()

    for genre in matching_genres:
        print(genre)

    if len(matching_genres) == 1:
        selected_genre = str(input("\nThe only matching genre for the specified input is " + matching_genres[0] + ". \nDo you want to look at " + matching_genres[0] + " movies? Enter y for yes and n for no\n")).lower()

        if selected_genre == 'y':
            selected_movie_genre = matching_genres[0]
            print("\nSelected movie genre: " + selected_movie_genre)
            
            movie_list_head = my_movie_list.get_head_node()
            found_movies = False  # Track if any movies were found

            while movie_list_head is not None:
                movie_sublist = movie_list_head.get_value()
                sublist_head = movie_sublist.get_head_node() if movie_sublist else None

                # Check if sublist is not None and contains movies for the selected genre
                while sublist_head is not None:
                    movie = sublist_head.get_value()
                    if movie and movie[0] == selected_movie_genre:  # Make sure the movie is not None
                        found_movies = True  # Mark that we found movies
                        print("----------------------------------------")
                        print("Name: " + movie[1])
                        print("Year: " + movie[2])
                        print("Summary: " + movie[3])
                        print("Rating: " + movie[4])
                        print("----------------------------------------\n")
                    sublist_head = sublist_head.get_next_node()

                movie_list_head = movie_list_head.get_next_node()  # Move to the next genre

            if not found_movies:
                print("\nNo movies found for this genre.")

            repeat_loop = str(input("\nDo you want to find other movies? Enter y for yes and n for no.\n")).lower()
            if repeat_loop == 'y':
                selected_movie_genre = ""
            else:
                print("Thank you for using Movie Picker!")
                break