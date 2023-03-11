import os


class EnvManager:
    SECRET_KEY: str = ""
    DEBUG: bool = False

    @staticmethod
    def _get_env_var(var_name: str) -> str:
        return os.environ.get(f"DJANGO_{var_name}", "")

    def __init__(self):
        self.SECRET_KEY = self._get_env_var("SECRET_KEY")
        self.DEBUG = self._get_env_var("DEBUG") == "True"


env_var = EnvManager()
