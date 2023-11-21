# Setup

## **Mac**
### Create Virtual Environment
```bash 
python3.11 -m venv .venv
```
### Acitvate Virtual Environment
```bash
Source .venv/bin/activate
```

### Install requirements.txt
```bash
pip install -r requirements.txt
```

### Start fastapi server
```bash
uvicorn app.main:app --reload
```


## **Windows**
### Create Virtual Environment
```bash 
python3.11 -m venv .venv
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