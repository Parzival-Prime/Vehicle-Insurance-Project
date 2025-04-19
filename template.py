import os
from pathlib import Path

main_directory = 'src'

list_of_files = [
    f"{main_directory}/__init__.py",
    f"{main_directory}/components/__init__.py",
    f"{main_directory}/components/data_ingestion.py",  
    f"{main_directory}/components/data_validation.py",
    f"{main_directory}/components/data_transformation.py",
    f"{main_directory}/components/model_trainer.py",
    f"{main_directory}/components/model_evaluation.py",
    f"{main_directory}/components/model_pusher.py",
    f"{main_directory}/configuration/__init__.py",
    f"{main_directory}/configuration/mongo_db_connection.py",
    f"{main_directory}/configuration/aws_connection.py",
    f"{main_directory}/cloud_storage/__init__.py",
    f"{main_directory}/cloud_storage/aws_storage.py",
    f"{main_directory}/data_access/__init__.py",
    f"{main_directory}/data_access/proj1_data.py",
    f"{main_directory}/constants/__init__.py",
    f"{main_directory}/entity/__init__.py",
    f"{main_directory}/entity/config_entity.py",
    f"{main_directory}/entity/artifact_entity.py",
    f"{main_directory}/entity/estimator.py",
    f"{main_directory}/entity/s3_estimator.py",
    f"{main_directory}/exception/__init__.py",
    f"{main_directory}/logger/__init__.py",
    f"{main_directory}/pipline/__init__.py",
    f"{main_directory}/pipline/training_pipeline.py",
    f"{main_directory}/pipline/prediction_pipeline.py",
    f"{main_directory}/utils/__init__.py",
    f"{main_directory}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as file:
            pass
    else:
        print(f'File is already present at "{filepath}"')