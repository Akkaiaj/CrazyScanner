import requests

class CVEScanner:
    def __init__(self):
        self.cve_database_url = "https://cve.circl.lu/api/"

    def check_cve(self, software_name, version):
        print(f" \U0001F50D  Checking for CVEs related to {software_name} version {version}...")
        response = requests.get(f"{self.cve_database_url}/search/{software_name}/{version}")
        
        if response.status_code == 200:
            cves = response.json()
            if cves:
                print(f" \U0001F9A0  Found CVEs for {software_name}:")
                for cve in cves:
                    print(f" \U000027A1  {cve['id']}: {cve['summary']}")
            else:
                print(f" \U0000274C  No CVEs found for {software_name} version {version}.")
        else:
            print(" \U0000274C  Error fetching CVE data.")
