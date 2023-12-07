# Welcome to ITSM Beleg 

Konrad Adamski, Ayana Ochirova, s87654, Tom Bischopink

# Run with Docker

### Install Docker Desktop 

https://www.docker.com/products/docker-desktop/

### Set .env file with env variables

- create a **.env** file 
- put the following variables into the file to access the ServiceNow API:

```bash
INSTANCE_SN=yourinstancename
USERNAME_SN=yourusername
PASSWORD_SN=yourpassword
```

### Run Docker Compose and start the container of FastAPI

```bash
docker-compose up
```


### Run Docker Image and Build to Run Vue.js Frontend
cd frontend!!!
#### Build the image:
```sh
docker build -t itsm_beleg/frontend .
```

#### Run the image:
```sh
docker run -it -p 8080:8080 --rm --name frontend itsm_beleg/frontend
```
### Access Docker Files:

**FastAPI Backend:**
```bash
docker exec -it fastapi_backend /bin/bash
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
python3 -m venv .venv
```
### Acitvate Virtual Environment
```bash
.\.venv\Scripts\activate
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
pytest ./tests
```