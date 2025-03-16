# 🔍 CrazyScanner [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Python Version](https://img.shields.io/badge/python-3.8%2B-blue) [![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<img src="https://raw.githubusercontent.com/Akkaiaj/CrazyScanner/main/a08a504c-077f-48d3-babb-5782437734b3.jpg" alt="CrazyScanner Logo" width="300">

> **A fast and advanced vulnerability scanner for SQL Injection and XSS**  
> *Uncover hidden vulnerabilities like a pro!*

[![Open Issues](https://img.shields.io/github/issues-raw/Akkaiaj/CrazyScanner)](https://github.com/Akkaiaj/CrazyScanner/issues) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Akkaiaj/CrazyScanner/pulls)

![CrazyScanner Demo](https://via.placeholder.com/800x400.png?text=CrazyScanner+Demo+GIF+Here) *Add demo gif when available*

![Hack Counter](https://count.getloli.com/get/@yourname?theme=moebooru)



## 📖 Table of Contents
- [✨ Features](#-features)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [🔧 Usage](#-usage)
- [📊 Report Example](#-report-example)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [⚠️ Disclaimer](#️-disclaimer)

## ✨ Features
| Feature | Description |
|---------|-------------|
| 🛡️ **SQLi Detection** | Advanced payloads with WAF evasion techniques |
| 🎯 **XSS Detection** | Comprehensive XSS payload library |
| ⚡ **High Performance** | Multi-threaded scanning engine |
| 📈 **Smart Parameter Discovery** | Automatic input detection in forms/URLs |
| 📂 **HTML Reporting** | Professional vulnerability reports |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
# Clone repository
git clone https://github.com/Akkaiaj/CrazyScanner.git
cd CrazyScanner

# Install dependencies
pip install -r requirements.txt

# Run scanner
python cli.py --url https://target.com

## 🔧 Usage
```bash
# Basic scan
python cli.py --url https://example.com

# Custom payload scan
python cli.py --url https://example.com --payloads sql,xss

# Save HTML report
python  cli.py --url https://example.com --output scan_report.html

# Show help menu
python cli.py --help
```

## 📊 Report Example
![Report Preview](https://via.placeholder.com/600x300.png?text=HTML+Report+Preview+Here)  
*Include actual report screenshot when available*

## 🤝 Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See our [Contribution Guidelines](CONTRIBUTING.md) for more details.

## 📄 License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## ⚠️ Disclaimer
> **Warning**  
> This tool is intended for **legal security testing** and **educational purposes** only. Never use it on systems you don't own or have explicit permission to test. The developers assume no liability for misuse of this software.
```
