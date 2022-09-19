from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig" , 
                        ["dataset_download_url" , 
                        "tgz_download_url" , 
                        "raw_data_dir" , 
                        "ingested_trained_dir" , 
                        "ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig" , ["schema_file_path" , "report_file_path" , "report_page_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig" , 
                            ["add_bedroom_per_room" ,
                            "transformed_trained_dir" ,
                            "transformed_test_dir" , 
                            "preprocessed_object_file_path"])

ModelTrainerConfig = namedtuple("ModelTrainerConfig" , ["trained_model_file_path" , "base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig" , ["model_evaluation_file_path" , "time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig" , ["export_path_dir"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig" , ["artifact_dir"])