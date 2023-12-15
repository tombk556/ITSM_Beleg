# Welcome to ITSM Beleg 

Konrad Adamski, Ayana Ochirova, s87654, Tom Bischopink

# Run with Docker

### Install Docker Desktop 

https://www.docker.com/products/docker-desktop/

### Set .env file with env variables

- create a **.env** file 
- put the following variables into the file to access the ServiceNow API:

```bash
INSTANCESN=yourinstancename
USERNAMESN=yourusername
PASSWORDSN=yourpassword
```

### Run Docker Compose application:

```bash
docker-compose up
```

After: visit **http://127.0.0.1:8080** to access frontend (UI) and **http://127.0.0.1:8080** to access backend!

### Access Images:

**FastAPI Backend:**
```bash
docker exec -it fastapi_backend /bin/bash
```

**FastAPI Backend:**
```bash
docker exec -it vuejs_frontend /bin/bash
```

# Setup for Development

## **Mac**
### Create Virtual Environment
```bash 
python3.9 -m venv .venv
```
### Acitvate Virtual Environment
```bash
Source .venv/bin/activate
```

### Install requirements.txt
```bash
pip install -r requirements.txt
```

### Add .env variables

- create a **.env** file 
- put the following variables into the file to access the ServiceNow API:

```bash
INSTANCE_SN=yourinstancename
USERNAME_SN=yourusername
PASSWORD_SN=yourpassword
```

### Start fastapi server
```bash
uvicorn app.main:app --reload
```


## **Windows**
### Create Virtual Environment
```bash 
python -m venv venv
```
### Acitvate Virtual Environment
```bash
venv/Scripts/activate
```

### Install requirements.txt 
```bash
pip install -r requirements.txt
```

### Start fastapi server
```bash
uvicorn app.main:app --reload
```

## **Tests**
To run the tests run the following cmd:
```bash
pytest tests
```