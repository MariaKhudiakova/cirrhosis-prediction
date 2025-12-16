from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"

RAW_DATA_PATH = DATA_DIR / "raw_data.csv"
PROCESSED_DATA_PATH = DATA_DIR / "processed_data.csv"
