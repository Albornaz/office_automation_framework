from dataclasses import dataclass

@dataclass
class EmailConfig:
    smtp_server: str
    port: int
    username: str
    password: str


@dataclass
class AppConfig:
    company_name: str
    timezone: str = "Europe/Moscow"
