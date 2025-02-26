import json

class Config:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self.default_config()

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

    def default_config(self):
        return {
            "scan_options": {
                "sqli": True,
                "xss": True,
                "command_injection": True,
                "directory_bruteforce": False,
                "file_inclusion": False
            }
        }

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

    def get_scan_options(self):
        return self.config.get("scan_options", self.default_config()["scan_options"])
