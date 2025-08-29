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

# backend/app/models/dashboard_models.py - Dashboard models

from typing import Any, Dict, List
from pydantic import BaseModel


class BuildIssue(BaseModel):
 environment: str
 issue: str
 severity: str


class LargeImage(BaseModel):
 environment: str
 estimated_size_mb: int


class RecentUpdate(BaseModel):
 environment: str
 modified: str
 days_ago: int


class CurrentBuild(BaseModel):
 build_id: str
 environments: List[str]
 started: str
 duration_minutes: int


class SuccessRate(BaseModel):
 percentage: int
 successful_builds: int
 total_builds: int
 period_days: int


class DashboardStats(BaseModel):
 ready_to_build: int
 build_issues: Dict[str, Any] # count + details
 large_images: Dict[str, Any] # count + details 
 recently_updated: Dict[str, Any] # count + details
 currently_building: Dict[str, Any] # count + details
 success_rate: SuccessRate
 last_updated: str
