
# utils.py - Utility Functions for Static Code Analysis Engine

def load_source_code(file_path):
    """Load and read the contents of a C/C++ source file."""
    with open(file_path, "r") as file:
        code = file.read()
    return code
