from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pathlib import Path
import platform

if platform.system() == "Windows":
    config_dotenv_path = Path(__file__).resolve().parents[4] / 'xLH-mims-data' / 'config' / 'xlh_mims_python.env'
else:
    config_dotenv_path = Path(__file__).resolve().parents[3] / 'config' / 'xlh_mims_python.env'

print(config_dotenv_path)

if not config_dotenv_path.exists():
    config_dotenv_path = Path(__file__).resolve().parents[0] / 'env.env'

load_dotenv(dotenv_path=config_dotenv_path)

# print(config_dotenv_path)

class Config(BaseSettings):
    openai_api_key: str = ''
    openrouter_api_key: str = ''

config = Config()

if __name__ == '__main__':
    for item in config.__dict__.items():
        print(f'{item[0]}: {item[1]}')
