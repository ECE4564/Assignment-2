# MongoDB.py - Encapsulates MongoDB related functions for ECE 4564 Assignment 2

import pymongo


class MongoDB:

    post_id = ''

    def __init__(self):
        # open default port and host (local client)
        self.client = pymongo.MongoClient()
        # generate book database
        self.db = self.client.book_database  # lazy initialisation
        self.collection = self.db.collection
        self.posts = self.db.posts

    # inserts a new book into the database
    # requires full information in JSON format, including a stock value of 0
    def insert(self, new_book):
        self.post_id = self.posts.insert_one(new_book).inserted_id
        # store post IDs in a dictionary?

    # query the database to find a book, search by title, author, or both
    def find(self, query):
        return self.posts.find_one(query)

    # list all books in the database, returns a list object containing JSON elements
    def list_all(self):
        # returns all posts in the db
        cursor = self.posts.find({})
        all_books = []
        for document in cursor:
            all_books.append(document)
        return all_books

    # modify the stock of a given book
    # can search with title, author, or both
    # for a BUY request, stock_change should be positive
    # for a SELL request, stock_change should be negative
    def change_stock(self, book, stock_change):
        # self.collection.update_one(title, {"$set": {"Stock": new_stock}})
        found_book = self.posts.find_one(book)
        old_stock = found_book["Stock"]
        self.posts.update_one(book, {"$set": {"Stock": old_stock + stock_change}})

    # remove a book from the database
    # returns a boolean if wanted
    def remove(self, book):
        result = self.posts.delete_one(book)
        if result.deleted_count == 1:
            return True
        else:
            return False

    # clears the database, this can be used to remove duplicate objects in the database when testing
    def clear_db(self):
        self.db.drop_collection(self.posts)

    # returns the current stock of a book
    def get_stock(self, title):
        found_book = self.posts.find_one(title)
        return found_book['Stock']