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

    def insert(self, new_book):
        self.post_id = self.posts.insert_one(new_book).inserted_id
        # store post IDs in a dictionary?

    def find(self, query):
        return self.posts.find_one(query)

    def list_all(self):
        # returns all posts in the db
        cursor = self.posts.find({})
        all_books = []
        for document in cursor:
            all_books.append(document)
        return all_books

    def change_stock(self, title, new_stock):
        # self.collection.update_one(title, {"$set": {"Stock": new_stock}})
        self.posts.update_one(title, {"$set": {"Stock": new_stock}})

    def remove(self, post):
        result = self.posts.delete_one(post)
        if result.deleted_count == 1:
            return True
        else:
            return False

    def clear_db(self):
        self.db.drop_collection(self.posts)

    def get_stock(self, title):
        found_book = self.posts.find_one(title)
        return found_book['Stock']