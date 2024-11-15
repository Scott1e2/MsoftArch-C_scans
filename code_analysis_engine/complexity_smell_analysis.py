
# complexity_smell_analysis.py - Code Complexity and Smell Detection for Static Code Analysis

import re
import logging
from config_loader import load_config
from utils import load_source_code
from logging_config import setup_logging
from output_manager import save_findings, display_findings

# Initialize logging
setup_logging("complexity_smell_analysis.log")
logger = logging.getLogger(__name__)

# Load configuration
config = load_config("config.json")

# Function to analyze code complexity and detect code smells
def analyze_complexity_and_smells(code):
    findings = []

    # Cyclomatic Complexity (simple heuristic based on conditional statements)
    conditional_patterns = ["if", "for", "while", "switch", "case"]
    complexity_score = sum(len(re.findall(rf"\b{pattern}\b", code)) for pattern in conditional_patterns)

    if complexity_score > config["analysis_settings"]["complexity_limit"]:
        finding = {
            "issue": "High cyclomatic complexity",
            "complexity_score": complexity_score,
            "severity": config["analysis_settings"]["severity_thresholds"]["high"]
        }
        findings.append(finding)
        logger.warning(f"Complexity issue detected: {finding}")

    # Large Functions Detection
    large_function_matches = re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)]*\)\s*{[^}]*}", code)
    for match in large_function_matches:
        function_size = len(match.splitlines())
        if function_size > config["code_smell_patterns"]["large_functions"]:
            finding = {
                "issue": "Large function",
                "size": function_size,
                "severity": config["analysis_settings"]["severity_thresholds"]["medium"]
            }
            findings.append(finding)
            logger.info(f"Large function detected: {finding}")

    # Deep Inheritance Detection (simple check for class inheritance depth)
    inheritance_matches = re.findall(r"class\s+[a-zA-Z_][a-zA-Z0-9_]*\s*:\s*public", code)
    inheritance_depth = len(inheritance_matches)
    if inheritance_depth > config["code_smell_patterns"]["deep_inheritance"]:
        finding = {
            "issue": "Deep inheritance hierarchy",
            "depth": inheritance_depth,
            "severity": config["analysis_settings"]["severity_thresholds"]["medium"]
        }
        findings.append(finding)
        logger.info(f"Deep inheritance detected: {finding}")

    return findings

# Main function to run complexity and smell analysis
def run_complexity_smell_analysis(file_path):
    logger.info(f"Starting complexity and smell analysis on {file_path}...")
    code = load_source_code(file_path)
    findings = analyze_complexity_and_smells(code)
    save_findings(findings, "complexity_smell_analysis_report.json")
    display_findings(findings)

if __name__ == "__main__":
    sample_file_path = "sample_code.cpp"  # Placeholder for demonstration; replace with target file
    run_complexity_smell_analysis(sample_file_path)
