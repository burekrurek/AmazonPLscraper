from db_connect import Database
db = Database()

db.create_table('products', [
    'id INTEGER PRIMARY KEY',
    'ProductName TEXT',
    'Price FLOAT',
    'SubmissionDate TIMESTAMP',
    'ProductLink TEXT',
    'ProductImage TEXT'
])

db.create_table('links', [
    'id INTEGER PRIMARY KEY',
    'ProductLink VARCHAR(255) UNIQUE'
])