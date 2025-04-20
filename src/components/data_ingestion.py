import os
import sys

from pandas import DataFrame #type: ignore
from sklearn.model_selection import train_test_split #type: ignore

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.exception import MyException
from src.logger import logging
from src.data_access.project1_data import Project1Data


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig=DataIngestionConfig()):
        """
        :param data_ingestion_config: configuration for data ingestion
        """
        
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise MyException(sys, e)
    
    
    def export_data_into_feature_store(self) -> DataFrame:
        """
        Description: This method exports data from mongodb to csv file
        
        Output: Data is returned as artifact of data ingestion components
        On Faliure: Log and raise an Exception  
        """
        
        try:
            logging.info(f"Exporting Data from MongoDB...")
            my_data = Project1Data()
            dataframe = my_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            logging.info(f"Shape of DataFrame: {dataframe.shape}")
            
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_name = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_name, exist_ok=True)
            logging.info(f"Saving the exported data into feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path,index=False, header=True)
            return dataframe
        
        except Exception as e:
            raise MyException(e, sys)
        
    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        """
        Method     : split_data_as_train_test
        Description: This method splits the dataframe into train test based on split ratio
        
        Output     : Folder is created in s3 bucket
        On Faliure : Write and log an Exception  
        """
        
        try:
            logging.info('Performing train test split')
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            
            logging.info('Exporting train and test file path...')
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dir_path = os.path.dirname(self.data_ingestion_config.testing_file_path)
            os.makedirs(dir_path, exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
            logging.info('Exported train test file path')
        
        except Exception as e:
            raise MyException(e, sys)
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Method Name :   initiate_data_ingestion
        Description :   This method initiates the data ingestion components of training pipeline 
        
        Output      :   train set and test set are returned as the artifacts of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        """
        
        try:
            logging.info('Initiating Data Ingestion...')
            dataframe = self.export_data_into_feature_store()
            self.split_data_as_train_test(dataframe)
            
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
            test_file_path=self.data_ingestion_config.testing_file_path)
            
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e, sys) from e            
            