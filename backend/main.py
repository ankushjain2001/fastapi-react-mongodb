#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import motor.motor_asyncio
from fastapi import FastAPI, Request, Depends
from fastapi_users import FastAPIUsers, models
from fastapi_users.db import MongoDBUserDatabase
from fastapi_users.authentication import CookieAuthentication, JWTAuthentication


# --- MongoDB Setup -----------------------------------------------------------

# MongoDB Configurations
DATABASE_URL = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
# MongoDB database instance ("DB" by default, can be changed)
database = client["DB"]

# MongoDB users collection instance ("users" by default, can be changed)
collection = database["users"]


# --- Users Collection Schema Setup -------------------------------------------

# Pydantic models for MongoDB "User" collection schema
# Learn more at https://frankie567.github.io/fastapi-users/configuration/model/

class User(models.BaseUser):
    """
        Fields "id", "is_active" and "is_superuser" are created by this model

        Modify the below lines to add more fields for the user

        WARNING: You must also modify the same lines in the
        UserCreate model below
    """
    
    firstName: str
    lastName: str


class UserCreate(models.BaseUserCreate):
    """
        Fields "email" and "password" are created by this model

        Modify the below lines to add more fields for the user

        WARNING: You must also modify the same lines in the
        User model above
    """

    firstName: str
    lastName: str


class UserUpdate(User, models.BaseUserUpdate):
    """
        This class Extends/Inherits the User class
    """
    pass


class UserDB(User, models.BaseUserDB):
    """
        This class Extends/Inherits the User class

        Field "hashed_password" is created by this model
    """
    pass


# --- Authentication Method Setup ---------------------------------------------

"""
    Session duration/expiration can be changed through the lifetime_seconds
    attribute

    Learn more at https://frankie567.github.io/fastapi-users/configuration/authentication/

"""

# Secret Key (must be changed from "SECRET")
SECRET = "SECRET"

# Authentication Method JWT
auth_backends = []
authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)
auth_backends.append(authentication)


# --- FastAPIUsers Object Declaration -----------------------------------------

# MongoDB "users" collection adaptor for API calls
user_db = MongoDBUserDatabase(UserDB, collection)

# FastAPI Users helper class with all the configurations from above
# It provides us all the routes
fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB
)


# --- FastAPI Server Initialization -------------------------------------------

# Learn more https://frankie567.github.io/fastapi-users/configuration/routers/

# Initiating FastAPI Server
app = FastAPI()

# Managing CORS for the React Frontend connections
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# --- User Authentication Routes ----------------------------------------------

# Learn more at https://frankie567.github.io/fastapi-users/configuration/routers/

# Add route for Login                           POST "/auth/login"
app.include_router(
    fastapi_users.get_auth_router(auth_backends[0]),
    prefix="/auth",
    tags=["auth"]
)

# Add route for Registeration                   POST "/auth/register"

# Below function can be used to init any backend process like sending out a
# successful registeration email
def on_after_register(user: UserDB, request: Request):
    print("User {user.id} has registered.")

app.include_router(
    # fastapi_users.get_register_router(),
    fastapi_users.get_register_router(on_after_register),
    prefix="/auth",
    tags=["auth"]
)

# Add route for User utilities "/auth/users/*"

""" 
    Get current logged in user profile          GET "/auth/users/me"
    Update current logged in user profile       PATCH "/auth/users/me"
    Get "_id" user profile                      GET "/auth/users/"
    Update "_id" user profile                   PATCH "/auth/users/{id}"
    Delete "_id" user profile                   DELETE "/auth/users/{id}" 
"""

app.include_router(
    fastapi_users.get_users_router(),
    prefix="/auth/users",
    tags=["auth"]
)

# Add route for Reset Password utility

"""
    Forgot Password                             POST /auth/users/forgot-password
    Reset Password                              POST /auth/users/reset-password                         
"""

app.include_router(
    fastapi_users.get_reset_password_router("SECRET"),
    prefix="/auth/users",
    tags=["auth"]
)


# --- Custom Unprotected Routes Template --------------------------------------

"""
    The below templates can be used for creating any Rest APIs that are
    independent of user's authenticaion state (logged in or logged out).
    
    Hence, these API calls don't necessarily require a user to be logged in.

    Please read Mongo Motor docs to perform async DB operations.
    Learn more https://motor.readthedocs.io/en/stable/
"""

@app.get("/custom-unprotected-route", tags=["unprotected-routes"])
async def get_custom_unprotected_route():
    # Add database CRUD operation logic here
    return "Success!"

@app.post("/custom-unprotected-route", tags=["unprotected-routes"])
async def post_custom_unprotected_route(
    body: dict
    ):
    # Add database CRUD operation logic here
    print(body)
    return "Success!"


# --- Custom Protected Routes Template ----------------------------------------

"""
    The below templates can be used for creating any Rest APIs that mandatorily
    require the user to be in logged in state. Such as getting user specific
    information.

    Please read Mongo Motor docs to perform async DB operations.
    Learn more https://motor.readthedocs.io/en/stable/
"""

@app.get("/custom-protected-route", tags=["protected-routes"])
async def get_custom_protected_route(
    user: User = Depends(fastapi_users.get_current_user)
):
    # Add database CRUD operation logic here
    return "Success!"

@app.post("/custom-protected-route", tags=["protected-routes"])
async def post_custom_protected_route(
    body: dict, 
    user: User = Depends(fastapi_users.get_current_user)
):
    # Add database CRUD operation logic here
    print(body)
    return "Success!"
