from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Web_Fast_Study"
    debug: bool = True
    database_url: str = "sqlite:///./origin.db"
    cors_origins: str = [
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"

    class Config:
        env_file = ".env"


settings = Settings()