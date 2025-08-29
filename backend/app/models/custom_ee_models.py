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

# backend/app/models/custom_ee_models.py - Custom EE Wizard models

from typing import Dict, List, Optional
from pydantic import BaseModel


class CustomEERequest(BaseModel):
 name: str
 description: Optional[str] = ""
 base_image: Optional[str] = ""
 python_packages: List[str] = []
 system_packages: List[str] = []
 ansible_collections: List[str] = []
 additional_build_steps: Optional[str] = None
 build_immediately: Optional[bool] = False
 # YAML import mode
 import_mode: Optional[str] = "wizard" # "wizard" or "yaml"
 yaml_content: Optional[str] = ""


class CustomEEResponse(BaseModel):
 success: bool
 message: str
 environment_path: Optional[str] = None
 build_id: Optional[str] = None


class EETemplate(BaseModel):
 name: str
 packages: List[str]
 description: str


class EETemplates(BaseModel):
 python_packages: Dict[str, List[str]]
 system_packages: Dict[str, List[str]]
 ansible_collections: Dict[str, List[str]]
