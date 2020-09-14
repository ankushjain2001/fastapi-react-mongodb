# FastAPI-React-MongoDB
A minimal boilerplate / template project to get you started with a Python FastAPI backend, React frontend, MongoDB, and JWT user authentication (via FastAPIUsers).

This template project provides the following:
- React frontend with the commonly used styling framework React-Bootstrap and icons library React-Icons
- Authentication system for FastAPI using JWT tokens as offered by FastAPIUsers project
- Examples for creating protected routes and regular routes using FastAPIUsers at backend and React-Router at frontend
- Examples for creating MongoDB collection schemas (using Pydantic) and adding more attributes to "users" collection
<hr>

## Features
- **[FastAPI](https://github.com/tiangolo/fastapi)** (backend server)
- **[FastAPIUsers](https://github.com/frankie567/fastapi-users)** (authentication system)
- **[React](https://reactjs.org/)** (frontend library)
- **[React-Bootstrap](https://github.com/react-bootstrap/react-bootstrap)** (frontend styling library)
- **[React-Icons](https://github.com/react-icons/react-icons)** (frontend styling library)
- **[MongoDB](https://github.com/mongodb/mongo)** (database server)
- **[Motor](https://github.com/mongodb/motor)** (async MongoDB connector for Python)

<hr>

## Screenshots
#### Landing Page
![Landing Page](https://user-images.githubusercontent.com/10784445/93062550-b301d800-f63a-11ea-99f6-d60911927245.png)

#### Home Page
![Home Page](https://user-images.githubusercontent.com/10784445/93062563-ba28e600-f63a-11ea-9119-5b711efa7cd8.png)

#### Swagger UI API Documentation
![Swagger UI API Documentation](https://user-images.githubusercontent.com/10784445/93062570-bd23d680-f63a-11ea-8d6a-2a2d121817a4.png)

<hr>

## Setup Instructions
#### A. MongoDB Database
1. Install [MongoDB-4.4.0](https://docs.mongodb.com/manual/installation/)

#### B. Python/FastAPI Backend
1. Install [Anaconda](https://docs.anaconda.com/anaconda/install/)
2. Create an anaconda virtual environment (called "ProjectENV" or whatever you like) using the requirements.txt
```bash
conda create -n ProjectENV python=3.8
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
1. Navigate to the root directory (where the three directories backend, database and frontend are present) or start your existing MongoDB server
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

<hr>

## Acknowledgement
- Idea inspired by [tiangolo's](https://github.com/tiangolo) [full-stack-fastapi-postgresql](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- React authorization component inspired by [Buuntu's](https://github.com/Buuntu) [fastapi-react](https://github.com/Buuntu/fastapi-react)
- FastAPI authorization system by [franke567's](https://github.com/frankie567) [fastapi-users](https://github.com/frankie567/fastapi-users)
