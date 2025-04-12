from pymongo import MongoClient

connection_string = "mongodb+srv://ananyabadagi:<@password>@cluster0.rxngbx9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)

# Example: Access a database and collection
db = client['my_database']
collection = db['my_collection']

# Perform operations

try:
    client.admin.command('ping')
    print("Pinged your development. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
