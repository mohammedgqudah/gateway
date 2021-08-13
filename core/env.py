from enum import Enum
from pydantic import BaseSettings


class APIEnv(str, Enum):
    development = 'development'
    test = 'test'
    staging = 'staging'
    production = 'production'


class Environment(BaseSettings):
    api_env: APIEnv = APIEnv.development
    secret_key: str

    pg_db_name: str = 'clinic_gateway'
    pg_db_user: str = None
    pg_db_pass: str = None
    pg_db_host: str
    pg_db_port: str = '5432'

    sentry_dsn: str = 'https://<>@<>.ingest.sentry.io/<>'

    redis_host: str
    redis_port: str = '6379'

    # jwt expiration (in hours)
    access_token_exp: int = 10

    customers_host: str
    customers_key: str

    catalog_host: str
    catalog_key: str

    @property
    def postgres_dsn(self) -> str:
        return (
            "postgresql+psycopg2://"
            f"{self.pg_db_user}:{self.pg_db_pass}@{self.pg_db_host}:{self.pg_db_port}/{self.pg_db_name}"
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        use_enum_values = True


environment = Environment()
