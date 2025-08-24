### reading the data
### split data to train and test
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


# Get absolute project root
PROJECT_ROOT = os.getcwd()   # ensures paths are based on current project

@dataclass
class DataingestionConfig:
    artifacts_dir: str = os.path.join(PROJECT_ROOT, "artifacts")
    train_data_path: str = os.path.join(PROJECT_ROOT, "artifacts", "train.csv")
    test_data_path: str = os.path.join(PROJECT_ROOT, "artifacts", "test.csv")
    raw_data_path: str = os.path.join(PROJECT_ROOT, "artifacts", "data.csv")


class Dataingestion:
    def __init__(self):
        self.ingestion_config = DataingestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method/component")
        
        try:
            # Debugging info
            print("✅ Project root:", PROJECT_ROOT)
            print("✅ Artifacts will be saved in:", self.ingestion_config.artifacts_dir)

            df = pd.read_csv(r'notebook\StudentsPerformance.csv')
            logging.info("Read the dataset as dataframe")
            print("✅ Dataset loaded successfully. Shape:", df.shape)

            # Ensure artifacts directory exists
            os.makedirs(self.ingestion_config.artifacts_dir, exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train & test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed")
            print("✅ Train/Test files created successfully!")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    try:
        obj = Dataingestion()
        obj.initiate_data_ingestion()
    except Exception as e:
        print("❌ Error:", e)
