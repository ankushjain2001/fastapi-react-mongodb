# FastAPI-React-MongoDB
A minimal boilerplate / template project to get you started with a FastAPI backend, React frontend, MongoDB, and JWT or session cookie user authentication (via FastAPIUsers).

<hr>

## Features
- **[FastAPI](https://github.com/tiangolo/fastapi)** 
- **[FastAPIUsers](https://github.com/frankie567/fastapi-users)** 
- **[React](https://reactjs.org/)**
- **[React-Bootstrap](https://github.com/react-bootstrap/react-bootstrap)**
- **[React-Icons](https://github.com/react-icons/react-icons)**
- **[MongoDB](https://github.com/mongodb/mongo)**
- **[Motor](https://github.com/mongodb/motor)**

<hr>

## Setup Instructions
#### A. MongoDB Database
1. Install [MongoDB-4.4.0](https://docs.mongodb.com/manual/installation/)

#### B. Python/FastAPI Backend
1. Install [Anaconda](https://docs.anaconda.com/anaconda/install/)
2. Create an anaconda virtual environment (called "ProjectENV" or whatever you like) using the requirements.txt
```bash
conda create -n ProjectENV python=3.7
```
3. Activate the virtual environemnt
```bash
conda activate ProjectENV
```
4. Navigate to the root directory (where the three directories backend, database and frontend are present)
5. Install Python packages to the virtual environment
```bash
pip install -r backend/requirements.txt 
```      
6. Deactivate the virtual environment
```bash
conda deactivate
```

#### C. React Frontend
1. Install [Node Package Manager (npm)](https://www.npmjs.com/get-npm)
2. Navigate into /frontend directory (where package.json is present)
3. Install the React dependencies with npm
```bash
npm install
```

<hr>

## Run Instructions
#### A. MongoDB Database
1. Navigate to the root directory (where the three directories backend, database and frontend are present)
2. Start MongoDB server
```bash
mongod --dbpath=database
 ```
3. The MongoDB server will be hosted at its default port 27017
#### B. Python/FastAPI Backend
1. Navigate into /backend directory (where main.py is present)
2. Activate the virtual environemnt
```bash
conda activate ProjectENV
```
3. Start FastAPI server
```bash
uvicorn main:app --reload
``` 
4. The FastAPI server will be hosted at its default port 8000
5. To access SwaggerUI for API testing and documentation, goto [http://localhost:8000/docs](http://localhost:8000/docs)
#### C. React Frontend
1. Navigate to /frontend directory (where package.json is present)
2. Start React Web Application
```bash
npm start
```
3. The React web application will be hosted at its default port 3000, goto [http://localhost:3000/](http://localhost:3000/)
