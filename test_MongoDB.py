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

# print(db1.find({"Author": "Stephen King"}))

db1.change_stock({"Name": "It"}, 6)

print('test find')
print(db1.find({"Name": "It", "Author": "Stephen King"}))

test_post2 = {"Author": "Herman Melville",
              "Name": "Moby Dick",
              "Stock": 3}

db1.insert(test_post2)

# print(db1.find({"Name": "Moby Dick"}))

print("First list all")
temp_list = db1.list_all()
print(*temp_list, sep='\n')

db1.remove({"Name": "It"})
db1.change_stock({"Name": "Moby Dick"}, - 3)

print("Second list all")
temp_list = db1.list_all()
print(*temp_list, sep='\n')

print('print get stock:')
print(db1.get_stock({"Name": "Moby Dick"}))
