from sqlmodel import Field, SQLModel
from typing import List, Optional
from datetime import datetime

class AuthSchema(SQLModel, table=False):
    __table_args__ = {'schema': 'auth'}

class User(AuthSchema, table=True):
    
    id: Optional[str] = Field(default=None, primary_key=True, nullable=False)
    username: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    is_active: Optional[bool] = Field(default=None)
    is_superuser: Optional[bool] = Field(default=None)
    hashed_password: Optional[str] = Field(default=None)
    groups: Optional[List[str]] = Field(default=None)
    user_permissions: Optional[List[str]] = Field(default=None)
    last_login: Optional[datetime] = Field(default=None)
    date_joined: Optional[datetime] = Field(default=None)