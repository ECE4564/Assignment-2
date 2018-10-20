# Unit tests for MongoDB class

import MongoDB
import unittest


db1 = MongoDB.MongoDB()

# clear the database to remove duplicates
db1.clear_db()

test_post1 = {"Author": "Stephen King",
              "Name": "It",
              "Stock": 4}

db1.insert(test_post1)

#print(db1.find({"Author": "Stephen King"}))

db1.change_stock({"Name": "It"}, 6)

#print(db1.find({"Name": "It"}))

test_post2 = {"Author": "Herman Melville",
              "Name": "Moby Dick",
              "Stock": 3}

db1.insert(test_post2)

#print(db1.find({"Name": "Moby Dick"}))

print("First list all")
temp_list = db1.list_all()
for p in temp_list:
    print(p)

db1.remove({"Name": "It"})

print("Second list all")
temp_list = db1.list_all()
for p in temp_list:
    print(p)

print(db1.get_stock({"Name": "Moby Dick"}))