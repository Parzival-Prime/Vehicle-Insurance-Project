import os 
import sys
import pymongo #type: ignore
import certifi #type: ignore

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URI

# Load the certificate authority file to avoid timeout errors when connecting to MongoDB
ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient is responsible for establishing a connection with MongoDB Database.
    
    Attributes:
    ------------
    client: MongoClient
        A shared MongoClient instance for the class.
    database:
        The specific databse instance that MongoDBClient connects to. 
    
    Methods:
    ---------
    __init__(database_name: str) -> None
        Initializes the database connection with the given database name.
    """
    
    client = None  # Shared MongoClient instance across all MongoDBClient instances
    
    def __init__(self, database_name: str=DATABASE_NAME) -> None:
        """Initializes a connection with mongodb database. If no existing connection is found, it establishes a new one.
        
        Parameters:
        -----------
        database_name: str, optional
            Name of the MongoDB database to connect to. Default is set by constant DATABASE_NAME.
            
        Raises:
        -------
        MyException
            If there is an issue or connecting to MongoDB or is the ENV variable for MongoDB is not set. 
        """
        
        try:
            # Check if a MongoDBClient connection has already been established; if not then create a new one
            if MongoDBClient.client is None:
                mongodb_uri = os.getenv(MONGODB_URI)
                if mongodb_uri is None:
                    raise MyException(f"Environment variable '{MONGODB_URI}' is not set ")
                
                # Establish a new MongoDB client connection
                MongoDBClient.client = pymongo.MongoClient(MONGODB_URI, tlsCAFile=ca)
                
            # use the shared MongoClient for this instance
            self.client = MongoDBClient.client
            self.database = self.client[database_name] # connect to the specified databse
            self.database_name = database_name
            logging.info("MongoDB connection successful.")
            
        except Exception as e:
            # Rasie a custom exception with traceback details if connection fails
            raise MyException(e, sys)