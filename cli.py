import argparse
from core.scanner import Scanner
from core.multi_thread import MultiThreadedScanner
from core.file_inclusion import FileInclusionScanner
from ascii_arts import get_random_banner
from utils.config import Config
import sys # Used to check and install packages

# Function to check and install missing packages
def install_missing_packages(packages):
    import importlib
    for package in packages:
        try:
            importlib.import_module(package)
        except ImportError:
            print(f"Installing missing package: {package}")
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed: {package}")

def main():
    print(get_random_banner()) # Get and print random banner

    parser = argparse.ArgumentParser(description="Crazy Vulnerability Scanner")
    parser.add_argument("-u", "--urls", nargs='+', required=True, help="Target URLs to scan")
    parser.add_argument("--enable_file_inclusion", action="store_true", help="Enable file inclusion scanning")
    parser.add_argument("--sqli", action="store_true", help="Enable SQLi scanning")
    parser.add_argument("--xss", action="store_true", help="Enable XSS scanning")
    parser.add_argument("--command_injection", action="store_true", help="Enable command injection scanning")

    args = parser.parse_args()
    config = Config() # Add code to load configuration
    scan_options = config.get_scan_options()

    packages_to_check = ['requests', 'beautifulsoup4', 'lxml']
    install_missing_packages(packages_to_check)

    # Enable scan options that the user has defined.
    if args.sqli:
        scan_options["sqli"] = True
    if args.xss:
        scan_options["xss"] = True
    if args.command_injection:
        scan_options["command_injection"] = True

    scanner = Scanner(args.urls, scan_options)

    multi_threaded_scanner = MultiThreadedScanner(scanner)
    multi_threaded_scanner.run_scan(args.urls)

    if args.enable_file_inclusion:
        for url in args.urls:
            file_inclusion_scanner = FileInclusionScanner(url)
            file_inclusion_scanner.scan()

if __name__ == "__main__":
    main()

