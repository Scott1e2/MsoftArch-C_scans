# MsoftArch-C_scans
a comprehensive tool for scanning Microsoft architecture and identifying C/C++ code vulnerabilities




# Static Code and OS-Level Vulnerability Analysis Tool

## Overview
This tool analyzes C/C++ code statically and performs dynamic, OS-level vulnerability detection. It is designed to detect code-level vulnerabilities, track runtime interactions, assess security mitigations, and identify functional issues in Windows-native applications.

### Key Features
1. **Static Analysis**: Identifies patterns, tracks data flow, detects complex constructs, and measures code complexity.
2. **Dynamic Analysis** (OS-Level):
   - **System Call and API Monitoring**: Hooks into Windows API to detect suspicious system calls.
   - **Fuzz Testing**: Generates randomized inputs to test network protocols and services.
   - **Security Mitigation Bypass Testing**: Tests bypassing DEP, ASLR, and other mitigations.
   - **Functional Testing Framework**: Validates secure user interactions and permissions.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repository/static-code-analysis-engine.git
    cd static-code-analysis-engine
    ```

2. **Dependencies**: Built-in libraries; no additional dependencies required.

## Configuration

The `config.json` file allows customization of vulnerability patterns, severity levels, and runtime settings.

## Usage

### Static Analysis Modules
- **Pattern-Based Vulnerability Detection**:
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

### Dynamic Analysis Modules (OS-Level)

1. **System Call and API Monitoring**:
   ```bash
   python dynamic_analysis_engine/dynamic_analysis.py
   ```
   - Monitors API calls and logs suspicious interactions.

2. **Fuzz Testing**:
   ```bash
   python dynamic_analysis_engine/fuzz_testing.py
   ```
   - Performs fuzz testing on HTTP protocols and Windows File Service.

3. **Security Mitigation Bypass Testing**:
   ```bash
   python dynamic_analysis_engine/security_mitigation_bypass.py
   ```
   - Simulates tests for DEP and ASLR bypass vulnerabilities.

4. **Functional Testing Framework**:
   ```bash
   python dynamic_analysis_engine/functional_testing_framework.py
   ```
   - Runs user login and file access tests to ensure secure interactions.

## File Structure

```
static_code_analysis_engine/
├── config.json                        # Configuration file for analysis settings
├── config_loader.py                   # Centralized configuration loading
├── data_flow_analysis.py              # Static data flow analysis
├── cpp_template_macro_analysis.py     # Static analysis of C++ templates and macros
├── complexity_smell_analysis.py       # Complexity and code smell detection
├── static_analysis.py                 # Pattern-based vulnerability detection
├── output_manager.py                  # Handles JSON, HTML, and text output
├── logging_config.py                  # Centralized logging configuration
├── utils.py                           # Utility functions
└── dynamic_analysis_engine/           # New folder for dynamic OS-level analysis
    ├── dynamic_analysis.py            # Monitors system calls and API interactions
    ├── fuzz_testing.py                # Protocol and service fuzz testing
    ├── security_mitigation_bypass.py  # Tests for DEP and ASLR bypass
    └── functional_testing_framework.py # User and file access permission testing
```

