# NephroFlow 🩺

ML pipeline for early prediction of kidney disease using structured lab test data.

## Features
- Logistic Regression + Ensemble Models
- MLflow tracking
- DVC versioning
- Docker-ready setup
- Modular folder structure

## Setup

```bash
git clone https://github.com/MB3339/NephroFlow.git
cd NephroFlow
pip install -r requirements.txt
```
## Workflows
- update config.yaml file
- update secrets.yaml file [optinal]
- update params.yaml file
- update the entity
- update the configuration manager in src config
- update the components
- update the pipeline
- update main.py
- update dvc.yaml
- app.py

## DagsHub Integration

This project integrates with [DagsHub](https://dagshub.com) for experiment tracking and data versioning.

### Setup

1. Install DagsHub client and MLflow if not already:

```bash
pip install dagshub mlflow
```


2. Set your DagsHub credentials as environment variables:
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/MB3339/NephroFlow.mlflow
export DAGSHUB_USERNAME='your-username'
export DAGSHUB_TOKEN='your-personal-access-token'
```

DagsHub Repo
Track experiments and access data on DagsHub:
👉 https://dagshub.com/MB3339/NephroFlow


Replace `your_dagshub_token` with your actual token before usage (but never commit tokens to GitHub).



