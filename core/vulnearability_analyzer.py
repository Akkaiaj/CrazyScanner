import re

class VulnerabilityAnalyzer:
    def __init__(self):
        pass

    def analyze_sql_injection(self, response):
        """
        Analyzes the HTTP response to determine if a SQL injection vulnerability exists.
        Returns True if a vulnerability is detected, False otherwise.
        """
        # Common SQL error messages
        sql_error_patterns = [
            r"SQL syntax.*MySQL",
            r"Warning.*mysqli_.*",
            r"SQLSTATE\[\d+\]: Syntax error",
            r"ORA-\d+ ORA-",  # Oracle errors
            r"Unclosed quotation mark before the character string",  # SQL Server errors
            r"supplied argument is not a valid MySQL",
            r"mysqli_fetch_array() expects parameter 1 to be mysqli_result, bool given"
        ]

        for pattern in sql_error_patterns:
            if re.search(pattern, response, re.IGNORECASE):
                return True  # SQL injection detected
        return False  # No SQL injection detected

    def analyze_xss(self, response, payload):
        """
        Analyzes the HTTP response to determine if an XSS vulnerability exists.
        Returns True if a vulnerability is detected, False otherwise.
        """
        # Check if the payload appears in the response
        if payload in response:
            return True  # XSS detected
        return False  # No XSS detected

    def analyze_command_injection(self, response):
        """
        Analyzes the HTTP response to determine if a command injection vulnerability exists.
        Returns True if a vulnerability is detected, False otherwise.
        """
        # Check for common command execution output patterns (you may need to customize these)
        command_execution_patterns = [
            r"uid=\d+\(\w+\) gid=\d+\(\w+\)",  # Unix-like systems (e.g., Linux, macOS)
            r"Volume in drive [A-Z] has no label",  # Windows systems
            r"total \d+",  # Unix-like systems (e.g., Linux, macOS)
            r"bytes free",  # Windows systems
        ]
        for pattern in command_execution_patterns:
            if re.search(pattern, response, re.IGNORECASE):
                return True  # Command injection detected
        return False  # No command injection detected
