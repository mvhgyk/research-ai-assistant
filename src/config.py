from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    llm_api_key: str
    llm_base_url: str
    llm_model: str


def load_settings() -> Settings:
    load_dotenv()
    return Settings(
        llm_api_key=os.getenv("LLM_API_KEY", ""),
        llm_base_url=os.getenv("LLM_BASE_URL", "https://api.example.com"),
        llm_model=os.getenv("LLM_MODEL", "your_model_name"),
    )
