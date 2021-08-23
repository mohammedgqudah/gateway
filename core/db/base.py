from sqlalchemy.ext.declarative import declarative_base
from fastapi_baseplate.clients.sqlalchemy import CustomBase

Base = declarative_base(cls=CustomBase)
