from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"
LOGS_DIR = BASE_DIR / "logs"

SMTP_SERVER = "localhost"
SMTP_PORT = 25
DEFAULT_SENDER = "oaf@company.local"
