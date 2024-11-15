
# static_analysis.py - Pattern-Based Vulnerability Detection for Static Code Analysis Engine

import re
import logging
from config_loader import load_config
from utils import load_source_code
from logging_config import setup_logging
from output_manager import save_findings, display_findings

# Initialize logging
setup_logging("static_analysis.log")
logger = logging.getLogger(__name__)

# Load configuration
config = load_config("config.json")

# Function to detect patterns based on vulnerability configurations
def detect_vulnerabilities(code):
    vulnerability_findings = []
    for vulnerability, patterns in config["vulnerability_patterns"].items():
        for pattern in patterns:
            matches = re.findall(rf"\b{pattern}\b", code)
            if matches:
                severity = config["analysis_settings"]["severity_thresholds"]["high"]
                finding = {
                    "vulnerability": vulnerability,
                    "pattern": pattern,
                    "matches": matches,
                    "severity": severity
                }
                vulnerability_findings.append(finding)
                logger.warning(f"Vulnerability detected: {finding}")
    return vulnerability_findings

# Main function to run the static analysis
def run_static_analysis(file_path):
    logger.info(f"Starting static analysis on {file_path}...")
    code = load_source_code(file_path)
    findings = detect_vulnerabilities(code)
    save_findings(findings, "static_analysis_report.json")
    display_findings(findings)

if __name__ == "__main__":
    sample_file_path = "sample_code.c"  # Placeholder for demonstration; replace with target file
    run_static_analysis(sample_file_path)
