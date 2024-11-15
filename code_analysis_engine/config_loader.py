
# config_loader.py - Centralized Configuration Loader for Static Code Analysis Engine

import json

def load_config(config_path="config.json"):
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
    return config
