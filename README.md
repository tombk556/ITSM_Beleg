# Welcome to ITSM Beleg 

Konrad Adamski, Ayana Ochirova, s87654, Tom Bischopink

# Setup

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