
# output_manager.py - Output Management for Static Code Analysis Engine with Advanced Reporting

import json
import logging

logger = logging.getLogger(__name__)

def save_findings(findings, output_file="analysis_report.json"):
    """Save findings to a JSON file."""
    try:
        with open(output_file, "w") as file:
            json.dump(findings, file, indent=4)
        logger.info(f"Findings saved to {output_file}")
    except Exception as e:
        logger.error(f"Error saving findings: {e}")

def display_findings(findings):
    """Print findings to the console."""
    for finding in findings:
        print(f"Issue: {finding['issue']} | Pattern: {finding.get('pattern', 'N/A')} | Severity: {finding['severity']}")

def export_findings_to_html(findings, output_file="analysis_report.html"):
    """Export findings to an HTML file for cross-platform compatibility."""
    try:
        with open(output_file, "w") as file:
            file.write("<html><head><title>Analysis Report</title></head><body>")
            file.write("<h1>Static Code Analysis Report</h1><ul>")
            for finding in findings:
                file.write(f"<li><strong>Issue:</strong> {finding['issue']}<br>")
                file.write(f"<strong>Severity:</strong> {finding['severity']}<br>")
                file.write(f"<strong>Details:</strong> {finding.get('details', 'N/A')}</li><br>")
            file.write("</ul></body></html>")
        logger.info(f"Findings exported to HTML file at {output_file}")
    except Exception as e:
        logger.error(f"Error exporting findings to HTML: {e}")

def export_findings_to_text(findings, output_file="analysis_report.txt"):
    """Export findings to a plain text file."""
    try:
        with open(output_file, "w") as file:
            file.write("Static Code Analysis Report\n")
            for finding in findings:
                file.write(f"Issue: {finding['issue']}\n")
                file.write(f"Severity: {finding['severity']}\n")
                file.write(f"Details: {finding.get('details', 'N/A')}\n")
                file.write("-" * 40 + "\n")
        logger.info(f"Findings exported to text file at {output_file}")
    except Exception as e:
        logger.error(f"Error exporting findings to text file: {e}")
