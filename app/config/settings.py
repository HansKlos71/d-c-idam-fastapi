from typing import Optional

# pydantic v2 moved BaseSettings to the separate package `pydantic-settings`.
# Detect what's available and provide a clear error if the runtime requires
# `pydantic-settings` but it's not installed.
try:
    # Preferred import for pydantic v2+: BaseSettings lives in pydantic-settings
    from pydantic_settings import BaseSettings
    from pydantic import AnyUrl, Field
except ModuleNotFoundError:
    # pydantic-settings not installed. Check whether we have pydantic v1 or v2.
    import pydantic

    pyd_version = getattr(pydantic, "__version__", "0")
    if pyd_version.startswith("1."):
        # pydantic v1 provides BaseSettings directly
        from pydantic import BaseSettings, AnyUrl, Field  # type: ignore
    else:
        # pydantic v2 without pydantic-settings: raise an actionable error
        raise RuntimeError(
            "pydantic v2 detected but `pydantic-settings` is not installed.\n"
            "Install it with: pip install pydantic-settings\n"
            "Or pin pydantic<2 if you prefer the legacy behaviour."
        )


class Settings(BaseSettings):
    """Application configuration loaded from environment (.env supported).

    - MAILERSEND_API_KEY is optional here so importing the settings module won't fail during tests;
      the adapter will raise an explicit error if the key is missing at runtime.
    """

    MAILERSEND_API_KEY: Optional[str] = Field(None, env="MAILERSEND_API_KEY")
    MAILERSEND_BASE_URL: AnyUrl = Field("https://api.mailersend.com/v1", env="MAILERSEND_BASE_URL")
    MAILERSEND_TEMPLATE_ID: Optional[str] = Field(None, env="MAILERSEND_TEMPLATE_ID")
    MAILERSEND_EMAIL_FROM: Optional[str] = Field(None, env="MAILERSEND_EMAIL_FROM")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# single source of configuration for the app
settings = Settings()
