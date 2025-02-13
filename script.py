from data import *
from welcome import *
from linkedlist import LinkedList


print welcome()

#Code to insert movie types into data structure here.

def insert_movie_types():
    movie_type_list = LinkedList()
    for movie_type in types:
        movie_type_list.insert_beginning(movie_type)
    return movie_type_list

