# Multi-stage Dockerfile
# Stage 1: Node.js build
FROM node:lts-alpine as node_builder

WORKDIR /app/frontend

COPY frontend/package*.json ./

RUN npm install

COPY frontend .

RUN npm run build

# Stage 2: Python build
FROM python:3.9.12

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Copy the built files from the Node.js build stage
COPY --from=node_builder /app/frontend/dist /app/frontend/dist
