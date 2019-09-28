from sanic_envconfig import EnvConfig


class Settings(EnvConfig):
    DEBUG: bool = True
    HOST: str = '0.0.0.0'
    PORT: int = 8000
    DATABASE_URL: str = 'postgresql://postgres:postgres@localhost/postgres'
