import requests
import socket

class Recon:
    def __init__(self):
        pass

    def subdomain_enumeration(self, domain):
        print(f"[+] Enumerating subdomains for {domain}")
        subdomains = ["www", "mail", "ftp", "dev", "api"]
        found_subdomains = []
        for sub in subdomains:
            subdomain = f"{sub}.{domain}"
            try:
                socket.gethostbyname(subdomain)
                print(f"[+] Found subdomain: {subdomain}")
                found_subdomains.append(subdomain)
            except socket.gaierror:
                pass
        return found_subdomains

    def port_scan(self, ip):
        print(f"[+] Scanning ports on {ip}")
        open_ports = []
        ports = [21, 22, 80, 443]
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print(f"[+] Port {port} is open")
                    open_ports.append(port)
                sock.close()
            except Exception as e:
                print(f"[-] Error scanning port {port}: {e}")
        return open_ports

    def directory_bruteforce(self, url):
        print(f"[+] Bruteforcing directories on {url}")
        directories = ["admin", "login", "uploads", "images"]
        found_directories = []
        for directory in directories:
            test_url = f"{url}/{directory}"
            response = requests.get(test_url)
            if response.status_code == 200:
                print(f"[+] Found directory: {test_url}")
                found_directories.append(test_url)
        return found_directories
