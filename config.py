import os
import json
from cryptography.fernet import Fernet

# Security: API Key Protection
# In a real production environment, we use environment variables or encrypted vaults.
# This implementation uses a local encrypted storage simulation.

class ConfigManager:
    def __init__(self):
        self.config_path = "config.json"
        self.key_path = "secret.key"
        self._init_security()

    def _init_security(self):
        if not os.path.exists(self.key_path):
            key = Fernet.generate_key()
            with open(self.key_path, "wb") as key_file:
                key_file.write(key)
        
        with open(self.key_path, "rb") as key_file:
            self.key = key_file.read()
        self.fernet = Fernet(self.key)

    def save_api_key(self, service, api_key):
        encrypted_key = self.fernet.encrypt(api_key.encode()).decode()
        config = self._load_raw_config()
        config[service] = encrypted_key
        with open(self.config_path, "w") as f:
            json.dump(config, f)

    def get_api_key(self, service):
        config = self._load_raw_config()
        encrypted_key = config.get(service)
        if encrypted_key:
            return self.fernet.decrypt(encrypted_key.encode()).decode()
        return None

    def _load_raw_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                return json.load(f)
        return {}

# Default Instance
config_manager = ConfigManager()

# Global Constants
DB_NAME = "cti_production.db"
REPORT_DIR = "reports"
LOG_DIR = "logs"

for d in [REPORT_DIR, LOG_DIR]:
    if not os.path.exists(d):
        os.makedirs(d)
