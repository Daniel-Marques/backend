from fastapi import FastAPI
from src.routers import router_users, router_auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers Authenticate and Authorization
app.include_router(router_auth.router, prefix="/auth")

# Routers USERS
app.include_router(router_users.router)
