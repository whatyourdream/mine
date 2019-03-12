# # Simple REST Full API of Luthvi Riskawati's Research

Research documentation

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure you have installed Python 3 on your device

### Project structure
```
* flask-rest-api/
  |--- app/
  |    |--- constant/
  |    |    |--- __init__.py
  |    |    |--- StringConstant.py
  |    |--- controller/
  |    |    |--- __init__.py
  |    |    |--- AppController.py
  |    |--- db/
  |    |    |--- dataset-pre.xlsx
  |    |    |--- datasets.xlsx
  |    |--- module/
  |    |    |--- __init__.py
  |    |    |--- AppModule.py
  |    |--- static/
  |    |    |--- images/
  |    |    |--- js/
  |    |--- templates/
  |    |    |--- index.html
  |    |--- __init__.py
  |--- docs/
  |--- venv/
  |--- run.py
```

### Step to create flask rest api

A step by step series of examples that tell you how to get a development env running

1. Install virtual environment
```
pip install virtualenv
```
2. Create virtual environment and activate inside your flask-rest-api directory according the above structure
```
virtualenv venv
> On windows -> venv\Scripts\activate
> On linux -> . env/bin/activate
```
3. Install some third party librares on your virtual environment with pip
```
pip install -r requirements.txt
```
4. Run web service
```
python run.py
```
