
# logging_config.py - Centralized Logging Setup for Static Code Analysis Engine

import logging

def setup_logging(log_file="static_code_analysis.log"):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging setup complete.")
