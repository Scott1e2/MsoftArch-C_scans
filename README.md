# MsoftArch-C_scans
a comprehensive tool for scanning Microsoft architecture and identifying C/C++ code vulnerabilities



# Microsoft focused "Static" Code Analysis Engine

## Overview
This tool is designed for deep analysis of C/C++ code, identifying security vulnerabilities, code complexity, and common "code smells." It features modular analysis, including pattern-based detection, data flow tracking, C++ template handling, and complexity evaluation.

### Key Features
1. **Pattern-Based Vulnerability Detection**: Scans for known vulnerability patterns (e.g., buffer overflows, memory mismanagement).
2. **Data Flow Analysis**: Tracks variables across functions, identifying unsanitized inputs and improper memory usage.
3. **C++ Template and Macro Handling**: Analyzes templates and macros for complex constructs in C++ code.
4. **Complexity and Smell Detection**: Detects high cyclomatic complexity, large functions, and deep inheritance.
5. **Modular Reporting**: Exports findings in JSON, HTML, or text formats for easy analysis and sharing.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repository/static-code-analysis-engine.git
    cd static-code-analysis-engine
    ```

2. **Dependencies**: This tool is developed in Python and uses built-in libraries, so no additional dependencies are required.

## Configuration

Edit the `config.json` file to customize vulnerability patterns, severity thresholds, and complexity limits. Here’s an example of the configuration structure:
```json
{
    "vulnerability_patterns": {
        "buffer_overflow": ["strcpy", "sprintf", "gets", "strcat"],
        "memory_management": ["malloc", "free", "new", "delete"],
        "unsanitized_input": ["scanf", "gets", "fgets"],
        "dangerous_casting": ["reinterpret_cast", "C-style casts"]
    },
    "analysis_settings": {
        "severity_thresholds": {
            "critical": 10,
            "high": 7,
            "medium": 5,
            "low": 2
        },
        "complexity_limit": 15,
        "report_format": "json"
    },
    "code_smell_patterns": {
        "nested_conditionals": 3,
        "large_functions": 100,
        "deep_inheritance": 5
    }
}
```

## Usage

1. **Run Individual Modules**:
    - **Pattern-Based Analysis**:
      ```bash
      python static_analysis.py sample_code.c
      ```

    - **Data Flow Analysis**:
      ```bash
      python data_flow_analysis.py sample_code.c
      ```

    - **C++ Template and Macro Analysis**:
      ```bash
      python cpp_template_macro_analysis.py sample_code.cpp
      ```

    - **Complexity and Smell Analysis**:
      ```bash
      python complexity_smell_analysis.py sample_code.cpp
      ```

2. **Output**:
    Each module exports findings to a JSON file by default, with options for HTML or text output using `output_manager.py`. To change formats, edit the report format in `config.json`.

## Modules

- **config_loader.py**: Centralized configuration loading for all modules.
- **data_flow_analysis.py**: Tracks data flow to identify unsanitized inputs and memory mismanagement.
- **cpp_template_macro_analysis.py**: Analyzes complex C++ constructs like templates and macros.
- **complexity_smell_analysis.py**: Checks for high complexity and detects potential code smells.
- **static_analysis.py**: Detects vulnerable patterns based on known C/C++ security risks.
- **output_manager.py**: Manages output formats, exporting findings in JSON, HTML, or text.
- **logging_config.py**: Centralizes logging setup for consistent logging across modules.
- **utils.py**: Utility functions, e.g., file loading.

## License
This project is licensed under the MIT License.

## Support
For issues or suggestions, please open an issue on the GitHub repository.
