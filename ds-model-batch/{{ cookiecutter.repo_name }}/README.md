{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── Makefile               <- Makefile with commands like `make data` or `make train`
    ├── README.md              <- The top-level README for developers using this project.
    ├── data       
    │   ├── processed          <- The final, canonical data sets for modeling.
    │   └── raw                <- The original, immutable data dump.
    │      
    ├── models                 <- Trained and serialized models, model predictions, or model summaries
    │      
    ├── notebooks              <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                             the creator's initials, and a short `-` delimited description, e.g.
    │                             `1.0-jqp-initial-data-exploration`.
    │      
    ├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
    │                             generated with `pip freeze > requirements.txt`
    ├── requirements_dev.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                             generated with `pip freeze > requirements.txt`
    |
    ├── setup.py               <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                    <- Source code for use in this project.
    │   ├── __init__.py        <- Makes src a Python module
    │   │
    │   ├── data               <- Scripts to download or generate data
    │   │   └── make_dataset.py
    |   |   └── generate_data.sql 
    │   │
    │   ├── features           <- Scripts reponsáveis pelo feature engineering
    │   │   └── feature_engineering.py
    │   │
    │   ├── models             <- Scripts de train/predict
    │   │   │                     
    │   │   ├── predict.py
    │   │   └── train.py
    |   |
    │   ├── utils.py
    │
    └── tox.ini                <- tox file with settings for running tox; see tox.readthedocs.io

--------
