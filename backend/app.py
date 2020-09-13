#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Authentication Setup
import motor.motor_asyncio
from fastapi import FastAPI
from fastapi_users import models
from fastapi_users.db import MongoDBUserDatabase


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


DATABASE_URL = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
# DB configs
db = client["IOB"]
collection = db["users"]


# DB Adaptor
user_db = MongoDBUserDatabase(UserDB, collection)

# -----------------------------------------------------------------------------

# Cookie setup
from fastapi_users.authentication import CookieAuthentication, JWTAuthentication

SECRET = "SECRET" # NeedZs change

# auth backend needs simplification
auth_backends = []

#authentication = CookieAuthentication(secret=SECRET, lifetime_seconds=3600, name='fastapiusersauth')
authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(authentication)

# -----------------------------------------------------------------------------

from fastapi_users import FastAPIUsers

# FastAPI Users helper class with all the configurations from above
# It will give us all the routes
fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)


# Initiating FastAPI Server

app = FastAPI()

# Managing CORS
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# /login /logout routes
app.include_router(
    fastapi_users.get_auth_router(auth_backends[0]),
    prefix="/auth",
    tags=["auth"],
)


# /register route
from fastapi import Request

def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")

app.include_router(
    fastapi_users.get_register_router(),
    # fastapi_users.get_register_router(on_after_register),
    prefix="/auth",
    tags=["auth"],
)
    
