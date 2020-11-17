

# FSD Consulting

One Paragraph of project description goes here


## Requirements
* Clone this repository: 
```
git clone https://github.com/zank0201/fsdcon.git
```
* Install postgressql locally and access the server from the terminal:
```
psql -U postgres
```

* Create a user 'postgres' with the password 'postgres'. This will be the database that will be used to create a dynamic dashboard:
* Create a database called fsdcon from the terminal:

```
CREATE DATABASE fsdcon
```

## Installing
### API

[Find the End-Points documentation at `End-points.md`](https://github.com/zank0201/fsdcon/blob/master/End-points.md)
* Enter the root file and install the python dependencies from ```requirements.txt```:
```
pip install -r requirement.txt
```

* Run the environement variables before running the API

```
export APP_SETTINGS="config.DevelopmentConfig"
```
* Run the API
```
python app.py
```
### Frontend
* Enter the frontend folder and install the dependencies:

```
cd frontend
npm install
```

* Connect to the frontend by running:

```
npm run dev
```

