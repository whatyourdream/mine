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
### Project Description

1. Constant directory, used to constant string as Relevant or Irrelevant string, etc.
2. Controller directory, used to handling request from http request both web or API Request
3. Db directory, used to save datasets from upload data if not exists you should create before run this project
4. Module directory, used to functionality or logic process in this research then called from controller
5. Static directory, used to serve css or javascript files
6. Templates directpry, used for html file when called from controller
7. Docs directory, used to save documentation of this research
8. Venv directory, used for virtual environment on this app with python3

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
