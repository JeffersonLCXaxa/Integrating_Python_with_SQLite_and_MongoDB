# Implementing a NoSQL Database with MongoDB using PyMongo

from pymongo import MongoClient

# Connect to MongoDB Atlas
client = MongoClient('<connection_string>')

# Create the database
db = client['bank']

# Create the 'bank' collection to store client documents
collection = db['bank']

# Insert documents with the mentioned structure
document1 = {
    'id': 1,
    'name': 'John',
    'cpf': '123456789',
    'address': 'Street A',
    'accounts': [
        {
            'id': 'c1',
            'type': 'Checking',
            'agency': '001',
            'number': 123,
            'balance': 1000
        },
        {
            'id': 'c2',
            'type': 'Savings',
            'agency': '002',
            'number': 456,
            'balance': 5000
        }
    ]
}

document2 = {
    'id': 2,
    'name': 'Mary',
    'cpf': '987654321',
    'address': 'Street B',
    'accounts': [
        {
            'id': 'c3',
            'type': 'Checking',
            'agency': '003',
            'number': 789,
            'balance': 2000
        }
    ]
