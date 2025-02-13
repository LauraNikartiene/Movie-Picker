from data import *
from welcome import *
from linkedlist import LinkedList

print welcome()

def insert_movie_genres():
    movie_genre_list = LinkedList()
    for movie_genre in genres:
        movie_genre_list.insert_beginning(movie_genre)
    return movie_genre_list

def insert_movie_data():
    restaurant_data_list = LinkedList()
    for movie_genre in genres:
        movie_sublist = LinkedList()
        for movie in movie_data:
            if movie[0] == movie_genre:
                movie_sublist.insert_beginning(movie)
        movie_data_list.insert_beginning(movie_sublist)
    return movie_data_list

my_type_list = insert_movie_genres()
my_movie_list = insert_movie_data()

selected_movie_genre = ""

while len(selected_movie_genre) == 0:
    user_input = str(input("\nWhat movie genre would you like to watch?\nType the beginning of that movie genre and press enter to see if it's here.\n")).lower()

    matching_genres = []
    genre_list_head = my_genre_list.get_head_node()
    while genre_list_head is not None:
        if str(genre_list_head.get_value()).startswith(user_input):
            matching_genres.append(genre_list_head.get_value())

    for genre in matching_genres:
        print(genre)

    if len(matching_genres) == 1:
        select_genre = str(input("\nThe only matching genre for the specified input is " + matching_genres[0] + ". \nDo you want to look at " + matching_genres[0] + " movies? Enter y for yes and n for no\n")).lower()

        if selected_genre == 'y':
            selected_movie_genre = matching_types[0]
            print("Selected movie genre: " + selected_movie_genre)
            movie_list_head = my_movie_list.get_head_node()
            while movie_list_head.get_next_node() is not None:
                sublist_head = movie_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_movie_genre:
                    while sublist_head.get_next_node() is not None:
                        print("----------------------------------------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Year: " + sublist_head.get_value()[2])
                        print("Summary: " + sublist_head.get_value()[3])
                        print("Rating: " + sublist_head.get_value()[4])
                        print("----------------------------------------")
                        sublist_head = sublist_head.get_next_node()
                movie_list_head = movie_list_head.get_next_node()

            repeat_loop = str(input("\nDo you want to find other movies? Enter y for yes and n for no.\n")).lower()
            if repeat_loop == 'y':
                select_movie_type = ""

        