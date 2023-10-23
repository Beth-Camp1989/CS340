from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31904
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self,data):
        if data is not None:
            result = self.collection.insert_one(data)
            return True 
        else:
            return False
            
    def read(self, search_dict):
        result = self.collection.find(search_dict)
        return list(result) if result else []
    
    def update(self, search_dict, update_data):
        if search_dict and update_data:
            result = self.collection.update_many(search_dict, {"$set": update_data})
            return result.modified_count
        else:
            return 0
        
    def delete(self, search_dict):
        if search_dict:
            result = self.collection.delete_many(search_dict)
            return result.deleted_count
        else: 
            return 0
   