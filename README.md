# ITSM Beleg

Hochschule für Wirtschaft und Technik präsentiert: **ITSM Beleg Wintersemster 23/24**

von **Konrad Adamski, Ayana Ochirova, Nitzsche Charanjit und Tom Bischopink**

# Setup for Development

Follow these steps to run the whole application on your system, which consists of:

- Backend - FastAPI
- Frontend - Vuejs

## Setup: Backend - FastAPI

Please install Python 3.9 or higher. Make sure the packages in requirements.txt are installed properly in the next steps.

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
- put the following ServiceNow Lab instance credentials into the .env file

```bash
INSTANCE_SN=yourinstancename
USERNAME_SN=yourusername
PASSWORD_SN=yourpassword
```

**Note**: the INSTANCE_SN variable should look like this: **nowlearning-nlinst12341234-1234**

### Start the FastAPI Backend Server

Start the FastAPI Backend Server running this command:

```bash
uvicorn app.main:app
```

Open the following URL: **http://127.0.0.1:8000**

You should be greeted by the following message:

```text
"Server is running - Version 0.14.1 ..."
```

Visit **https://127.0.0.1:8000/docs** to get all routes for managing the ServiceNow Incidents.

## Setup: Frontend - Vuejs

Vuejs is the frontend interface to manage all the ServiceNow Incidents.
To run the Vuejs application, make sure the FastAPI Backend and the ServiceNow Lab instance are running in the background.

Run the following commands on another terminal window, inside the project directory. Make sure to install **npm** and other dependencies to run the Vuejs framework on your system.

```bash
cd frontend

npm install

npm run build

npm install -g http-server

http-server dist
```

Afterwards, open the following URL **http://127.0.0.1:8080**

If the FastAPI backend and the ServiceNow Lab instance are properly configured and running, you should see a list of incidents from ServiceNow.

# Tests

## Unit Tests

To run the unit tests run the following cmd:

```bash
pytest ./tests --capture=no
```

Make sure your ServiceNow Lab instance is running.

## Integration and Load Tests

Get k6 running on your system by downloading the latest docker image.

Make sure the FastAPI backend server and the ServiceNow lab credentials are running in the background (the tests are performed locally on 127.0.0.1:8000).

```bash
k6 run ./PostTests/loadtest.js
k6 run ./PostTests/integrationtest.js
```

# Run with Docker

- create a **.env** file (same as before)
- put the following ServiceNow Lab instance credentials into the .env file

```bash
INSTANCE_SN=yourinstancename
USERNAME_SN=yourusername
PASSWORD_SN=yourpassword
```

### Run docker-compose up:

```bash
docker-compose up
```

Make sure your ServiceNow Lab instance is valid and running in the background.

After successfully launching the docker containers visit:

- **http://127.0.0.1:8080** to access the Vuejs frontend and
- **http://127.0.0.1:8080** to access the FastAPI backend
