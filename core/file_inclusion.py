import requests

class FileInclusionScanner:
    def __init__(self, url):
        self.url = url
        self.payloads = [
            "/etc/passwd",  # Unix file
            "C:\\boot.ini",  # Windows file
        ]

    def scan(self):
        print(" \U0001F50E  Scanning for file inclusion vulnerabilities...")
        for payload in self.payloads:
            test_url = f"{self.url}?file={payload}"
            try:
                response = requests.get(test_url)
                if response.status_code == 200 and self.is_file_included(response.text, payload):
                    print(f" \U0001F9A0  File inclusion vulnerability found at: {test_url}")
                else:
                    print(f" \U0000274C  No file inclusion vulnerability found for payload: {payload}")
            except requests.RequestException as e:
                print(f" \U0000274C  Error during request: {e}")

    def is_file_included(self, response_text, payload):
        # Check if the content of the payload is in the response
        if payload in response_text:
            return True
        return False

