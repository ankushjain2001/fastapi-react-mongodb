# FastAPI-React-MongoDB
A minimal boilerplate / template project to get you started with a Python FastAPI backend, React frontend, MongoDB, and JWT user authentication (via FastAPIUsers).

This template project provides the following:
- React frontend with the commonly used styling framework React-Bootstrap and icons library React-Icons
- Authentication system for FastAPI using JWT tokens as offered by FastAPIUsers project
- Examples for creating protected routes and regular routes using FastAPIUsers at backend and React-Router at frontend
- Examples for creating MongoDB collection schemas (using Pydantic) and adding more attributes to "users" collection
<hr>

## Screenshots
#### Landing Page
[![Landing Page](https://user-images.githubusercontent.com/10784445/93058018-6a472080-f634-11ea-8991-b11725621a06.png)]

#### Home Page
![Home Page](https://user-images.githubusercontent.com/10784445/93058005-65826c80-f634-11ea-8d50-c325dba0f273.png)

#### Swagger UI API Documentation
![Swagger UI API Documentation](https://user-images.githubusercontent.com/10784445/93057970-569bba00-f634-11ea-9520-4a46d5c38427.png)

## Dependencies
- **[FastAPI](https://github.com/tiangolo/fastapi)** (backend server)
- **[FastAPIUsers](https://github.com/frankie567/fastapi-users)** (authentication system)
- **[React](https://reactjs.org/)** (frontend library)
- **[React-Bootstrap](https://github.com/react-bootstrap/react-bootstrap)** (frontend styling library)
- **[React-Icons](https://github.com/react-icons/react-icons)** (frontend styling library)
- **[MongoDB](https://github.com/mongodb/mongo)** (database server)
- **[Motor](https://github.com/mongodb/motor)** (async MongoDB connector for Python)

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

<hr>

## Acknowledgement
- React authorization component inspired by [Buuntu's](https://github.com/Buuntu) [fastapi-react](https://github.com/Buuntu/fastapi-react)
- FastAPI authorization system by [franke567's](https://github.com/frankie567) [fastapi-users](https://github.com/frankie567/fastapi-users)
