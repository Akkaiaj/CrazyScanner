from utils.http_requests import send_request
from core.payloads import PayloadManager
from core.waf_evasion import WAFEvasion
from core.auto_discovery import discover_parameters
from core.vulnerability_analyzer import VulnerabilityAnalyzer
from core.cve_scan import CVEScanner  # New import for CVE scanning
import re
import time

class Scanner:
    def __init__(self, urls, scan_options):
        self.urls = urls
        self.payload_manager = PayloadManager()
        self.waf_evasion = WAFEvasion()
        self.vuln_analyzer = VulnerabilityAnalyzer()
        self.cve_scanner = CVEScanner()  # Initialize the CVE scanner
        self.scan_options = scan_options
    
    def scan_target(self, url):
        print(f" \U0001F50E  Scanning {url}...") 
        
        if self.scan_options.get("sqli", True):
            self.scan_sql_injection(url)
        if self.scan_options.get("xss", True):
            self.scan_xss(url)
        if self.scan_options.get("command_injection", True):
            self.scan_command_injection(url) 
        
        self.scan_all_parameters(url)

    def scan_sql_injection(self, url):
        print(" \U0001F50D  Starting SQL Injection Scan...")
        for payload in self.payload_manager.get_sql_payloads():
            evaded_payload = self.waf_evasion.evade(payload)
            test_url = f"{url}?id={evaded_payload}"
            response, status_code, headers = send_request(test_url)

            time.sleep(0.5) 

            if response is not None:
                if self.vuln_analyzer.analyze_sql_injection(response):
                    print(f" \U0001F9A0  SQL Injection vulnerability detected at: {test_url}")
                    print(" \U0001F9A0  Vulnerability found!")
                else:
                    print(f" \U0000274C  No SQL Injection vulnerability found at: {test_url}")
                if self.waf_evasion.detect_waf(headers):
                    print(f" \U000026A0  WAF detected but SQL may still be possible: {test_url}")
            else:
                print(f" \U0000274C  Could not retrieve URL: {test_url}")

    def scan_xss(self, url):
        print(" \U0001F50D  Starting XSS Scan...")
        for payload in self.payload_manager.get_xss_payloads():
            evaded_payload = self.waf_evasion.evade(payload)
            test_url = f"{url}?q={evaded_payload}"
            response, status_code, headers = send_request(test_url)

            time.sleep(0.5) 

            if response is not None:
                if self.vuln_analyzer.analyze_xss(response, evaded_payload):
                    print(f" \U0001F9A0  XSS vulnerability detected at: {test_url}")
                    print(" \U0001F9A0  Vulnerability found!")
                else:
                    print(f" \U0000274C  No XSS vulnerability found at: {test_url}")
                if self.waf_evasion.detect_waf(headers):
                    print(f" \U000026A0  WAF detected but XSS may still be possible: {test_url}")
            else:
                print(f" \U0000274C  Could not retrieve URL: {test_url}")

    def scan_all_parameters(self, url):
        parameters = discover_parameters(url)
        print(f" \U0001F4DD  Found parameters: {parameters}")  
        
        for method, action, param_name in parameters:
            if method == 'get':
                for payload in self.payload_manager.get_sql_payloads():
                    evaded_payload = self.waf_evasion.evade(payload)
                    test_url = f"{url}?{param_name}={evaded_payload}"
                    response, status_code, headers = send_request(test_url)

                    time.sleep(0.5) 

                    if response is not None:
                        if self.vuln_analyzer.analyze_sql_injection(response):
                            print(f" \U0001F9A0  SQL Injection vulnerability detected at: {test_url}")

    def scan_command_injection(self, url):
        print(" \U0001F50D  Starting Command Injection Scan...")
        command_injection_payloads = [
            "| ls -al",   
            "; uname -a",  
            "& ipconfig /all",  
        ]
        
        for payload in command_injection_payloads:
            test_url = f"{url}?cmd={payload}"  
            response, status_code, headers = send_request(test_url)

            time.sleep(0.5) 

            if response and self.vuln_analyzer.analyze_command_injection(response):
                print(f" \U0001F9A0  Command Injection vulnerability detected at: {test_url}")

    def scan_cve(self, software_name, version):
        """Scan for known CVEs related to a specific software."""
        self.cve_scanner.check_cve(software_name, version)

