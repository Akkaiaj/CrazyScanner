import base64

class PayloadManager:
    def __init__(self):
        self.sql_payloads = self.load_payloads("payloads/sql_payloads.txt")
        self.xss_payloads = self.load_payloads("payloads/xss_payloads.txt")

    def load_payloads(self, file_path):
        try:
            with open(file_path, "r") as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
            return []

    def get_sql_payloads(self):
        return self.sql_payloads

    def get_xss_payloads(self):
        return self.xss_payloads

    def encode_payload(self, payload):
        return base64.b64encode(payload.encode()).decode()

    def mixed_encoding(self, payload):
        return payload.replace("'", "%27").replace(" ", "%20")
