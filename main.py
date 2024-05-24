
import sys
sys.path.append('C:/Users/ubaid/Desktop/NLP Projects/NLP-Project/src')
from textClassification.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from src.textClassification.logging import logging

STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise e