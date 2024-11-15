
# data_flow_analysis.py - Data Flow Analysis Module for Vulnerability Detection in Static Code Analysis Engine

import re
import logging
from config_loader import load_config
from utils import load_source_code
from logging_config import setup_logging
from output_manager import save_findings, display_findings

# Initialize logging
setup_logging("data_flow_analysis.log")
logger = logging.getLogger(__name__)

# Load configuration
config = load_config("config.json")

# Data Flow Analysis to track variable usage across functions
def analyze_data_flow(code):
    data_flow_findings = []
    # Detect unsanitized inputs
    input_patterns = config["vulnerability_patterns"]["unsanitized_input"]
    for pattern in input_patterns:
        input_matches = re.findall(rf"\b{pattern}\b\s*\(([^)]+)\)", code)
        for match in input_matches:
            finding = {
                "issue": "Unsanitized input usage",
                "pattern": pattern,
                "input_variable": match.strip(),
                "severity": config["analysis_settings"]["severity_thresholds"]["medium"]
            }
            data_flow_findings.append(finding)
            logger.warning(f"Data Flow Analysis Finding: {finding}")

    # Detect improper memory management
    alloc_patterns = ["malloc", "new"]
    free_patterns = ["free", "delete"]
    alloc_usage = {pattern: re.findall(rf"\b{pattern}\b\s*\(([^)]+)\)", code) for pattern in alloc_patterns}
    free_usage = {pattern: re.findall(rf"\b{pattern}\b\s*\(([^)]+)\)", code) for pattern in free_patterns}

    for alloc in alloc_patterns:
        if alloc_usage[alloc] and not any(free_usage[free] for free in free_patterns):
            finding = {
                "issue": "Potential memory leak",
                "pattern": alloc,
                "severity": config["analysis_settings"]["severity_thresholds"]["high"]
            }
            data_flow_findings.append(finding)
            logger.warning(f"Data Flow Analysis Finding: {finding}")

    return data_flow_findings

# Main function to run data flow analysis
def run_data_flow_analysis(file_path):
    logger.info(f"Starting data flow analysis on {file_path}...")
    code = load_source_code(file_path)
    findings = analyze_data_flow(code)
    save_findings(findings, "data_flow_analysis_report.json")
    display_findings(findings)

if __name__ == "__main__":
    sample_file_path = "sample_code.c"  # Placeholder for demonstration; replace with target file
    run_data_flow_analysis(sample_file_path)
