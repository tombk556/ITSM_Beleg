from dotenv import dotenv_values

class Config:
    def __init__(self):
        self.config = dotenv_values(".env")

    def get(self, key, default=None):
        return self.config.get(key, default)

config = Config()