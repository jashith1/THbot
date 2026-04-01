from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DISCORD_BOT_TOKEN: str
    MENTOR_CHANNEL_ID: int #discord.py expects channel ID to be ints

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
