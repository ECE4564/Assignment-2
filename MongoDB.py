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

    def insert(self, post):
        self.post_id = self.posts.insert_one(post).inserted_id
        # store post IDs in a dictionary?

    def find(self, query):
        return self.posts.find_one(query)

    def list_all(self):
        # returns all posts in the db
        for post in self.posts.find():
            return post

    def increase_stock(self, title, increase_num):
        self.collection.update()