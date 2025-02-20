import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(levelname)s]: %(message)s:')



list_of_files = [
   ".github/workflows/.gitkeep",
   "src/__init__.py",
   "src/components/__init__.py", 
   "src/components/data_ingestion.py",
   "src/components/data_transformation.py",
   "src/components/model_trainer.py",
   "src/components/model_evaluation.py",
   "src/pipeline/__init__.py",
   "src/pipeline/training_pipeline.py",
   "src/pipeline/prediction_pipeline.py",
   "src/utils/__init__.py",
   "src/utils/utils.py",
   "src/logger/logging.py",
   "src/exception/exception.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "init_setup.sh",
   "requirements.txt",
   "requirements_dev.txt", 
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating dirrectories: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass 
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f" {filename} is already exists")
#its updated