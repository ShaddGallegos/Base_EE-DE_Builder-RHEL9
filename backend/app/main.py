#!/usr/bin/env python3
"""
User-configurable variables - modify as needed
"""
import os
import getpass

# User configuration
USER = os.getenv('USER', getpass.getuser())
USER_EMAIL = os.getenv('USER_EMAIL', f"{USER}@{os.getenv('COMPANY_DOMAIN', 'example.com')}")
COMPANY_NAME = os.getenv('COMPANY_NAME', 'Your Company')
COMPANY_DOMAIN = os.getenv('COMPANY_DOMAIN', 'example.com')

# backend/app/main.py - Clean FastAPI Application Entry Point

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.routers import auth, builds, environments, dashboard, custom_ee

@asynccontextmanager
async def lifespan(app: FastAPI):
 """Application lifespan - startup and shutdown events"""
 # Startup
 print(f"Quick Start Starting {settings.APP_NAME} v{settings.VERSION}")
 print(f"Installation Environment: {settings.ENVIRONMENT}")
 print(f" Container Runtime: {settings.CONTAINER_RUNTIME}")
 
 yield
 
 # Shutdown
 print(" Shutting down EE-DE Builder...")

# Create FastAPI application
app = FastAPI(
 title=settings.APP_NAME,
 description=settings.APP_DESCRIPTION,
 version=settings.VERSION,
 lifespan=lifespan
)

# Configure CORS
app.add_middleware(
 CORSMiddleware,
 allow_origins=settings.ALLOWED_ORIGINS,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
app.include_router(builds.router, prefix="/api/builds", tags=["builds"])
app.include_router(environments.router, prefix="/api/environments", tags=["environments"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["dashboard"])
app.include_router(custom_ee.router, prefix="/api/custom-ee", tags=["custom-ee"])

@app.get("/")
async def root():
 """Root endpoint - health check"""
 return {
 "message": f"Welcome to {settings.APP_NAME}",
 "version": settings.VERSION,
 "status": "healthy"
 }

@app.get("/health")
async def health_check():
 """Health check endpoint"""
 return {"status": "healthy", "service": settings.APP_NAME}

if __name__ == "__main__":
 import uvicorn
 uvicorn.run(
 "app.main:app",
 host="0.0.0.0",
 port=settings.PORT,
 reload=settings.DEBUG
 )
