from fastapi_baseplate.clients.sqlalchemy import CustomBase
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(cls=CustomBase)
