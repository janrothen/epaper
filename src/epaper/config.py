import tomllib
from pathlib import Path

_CONFIG_PATH = Path(__file__).parents[2] / "config.toml"
_config: dict | None = None


def config() -> dict:
    global _config
    if _config is None:
        with open(_CONFIG_PATH, "rb") as f:
            _config = tomllib.load(f)
    return _config
