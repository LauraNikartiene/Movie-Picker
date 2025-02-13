from data import *
from welcome import *
from linkedlist import LinkedList


print welcome()

#Code to insert movie types into data structure.

def insert_movie_types():
    movie_type_list = LinkedList()
    for movie_type in types:
        movie_type_list.insert_beginning(movie_type)
    return movie_type_list

#Code to insert movie data into a data structure.

def insert_movie_data():
    restaurant_data_list = LinkedList()
    for movie_type in types:
        movie_sublist = LinkedList()
        for movie in movie_data:
            if movie[0] == movie_type:
                movie_sublist.insert_beginning(movie)
        movie_data_list.insert_beginning(movie_sublist)
    return movie_data_list

my_type_list = insert_movie_types()
my_movie_list = insert_movie_data()

selected_movie_type = ""

#Code for user interaction.

