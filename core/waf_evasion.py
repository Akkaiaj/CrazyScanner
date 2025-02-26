import random, base64

class WAFEvasion:
    def evade(self, payload):
        evaded_payload = self.encode_double(payload)
        evaded_payload = self.mixed_encoding(evaded_payload)
        evaded_payload = self.insert_junk(evaded_payload)
        
        # Further transformations (more evasive)
        if random.random() > 0.7:
            evaded_payload = self.wildcard_space(evaded_payload) # Add random wildcards

        if random.random() > 0.7:  # Apply alternate encoding
            evaded_payload = self.base64_encode(evaded_payload)

        return evaded_payload

    def encode_double(self, payload):
        return payload.replace("%", "%25")

    def mixed_encoding(self, payload):
        return payload.replace("'", "%27").replace(" ", "/**/")

    def insert_junk(self, payload):
        junk_chars = ['+-', '/*', '--', '/*', '*/']
        for junk in junk_chars:
            if random.random() > 0.5:
                payload += junk
        return payload

    def wildcard_space(self, payload):  # Random wildcards in place of space
        return payload.replace(" ", "%20")

    def base64_encode(self, payload):
        return base64.b64encode(payload.encode()).decode()

    def detect_waf(self, headers):
        if headers is not None and 'status' in headers and headers['status'] == '406':
            return True
        return False

