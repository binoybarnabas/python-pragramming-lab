import pymongo  
client = pymongo.MongoClient("mongodb+srv://root:root@cluster0.7mrqgec.mongodb.net/?retryWrites=true&w=majority")  
  
collection = client.libraryDB.books  
booksData = [  
  
      {  
         "id":"01",  
         "language": "Java",  
         "edition": "third",  
         "author": "Herbert Schildt"  
      },  
  
      {  
         "id":"07",  
         "language": "C++",  
         "edition": "second",  
         "author": "E.Balagurusamy"  
      }  
   ]  
  
collection.insert_many(booksData)
