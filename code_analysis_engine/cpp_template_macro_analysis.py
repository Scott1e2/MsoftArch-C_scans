
# cpp_template_macro_analysis.py - C++ Template and Macro Handling for Static Code Analysis

import re
import logging
from config_loader import load_config
from utils import load_source_code
from logging_config import setup_logging
from output_manager import save_findings, display_findings

# Initialize logging
setup_logging("cpp_template_macro_analysis.log")
logger = logging.getLogger(__name__)

# Load configuration
config = load_config("config.json")

# Function to analyze C++ templates and macros
def analyze_cpp_templates_and_macros(code):
    findings = []

    # Detect templates
    template_matches = re.findall(r"template\s*<[^>]+>\s*class\s+\w+|template\s*<[^>]+>\s*struct\s+\w+", code)
    for match in template_matches:
        finding = {
            "issue": "Template usage",
            "pattern": "template class/struct",
            "severity": config["analysis_settings"]["severity_thresholds"]["medium"],
            "details": match.strip()
        }
        findings.append(finding)
        logger.info(f"Template detected: {finding}")

    # Detect macros
    macro_matches = re.findall(r"#define\s+\w+\s+.*", code)
    for match in macro_matches:
        finding = {
            "issue": "Macro usage",
            "pattern": "#define",
            "severity": config["analysis_settings"]["severity_thresholds"]["medium"],
            "details": match.strip()
        }
        findings.append(finding)
        logger.info(f"Macro detected: {finding}")

    return findings

# Main function to run C++ template and macro analysis
def run_cpp_template_macro_analysis(file_path):
    logger.info(f"Starting C++ template and macro analysis on {file_path}...")
    code = load_source_code(file_path)
    findings = analyze_cpp_templates_and_macros(code)
    save_findings(findings, "cpp_template_macro_analysis_report.json")
    display_findings(findings)

if __name__ == "__main__":
    sample_file_path = "sample_code.cpp"  # Placeholder for demonstration; replace with target file
    run_cpp_template_macro_analysis(sample_file_path)
