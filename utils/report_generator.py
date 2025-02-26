from datetime import datetime

class ReportGenerator:
    @staticmethod
    def generate_html_report(results):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        html_content = "<html><head><title>Scan Report</title></head><body>"
        html_content += f"<h1>Scan Report ({timestamp})</h1>"
        
        for result in results:
            html_content += f"<h2>{result['type']}</h2>"
            html_content += f"<p>{result['details']}</p>"
        
        html_content += "</body></html>"
        
        with open(f"report_{timestamp}.html", "w") as report_file:
            report_file.write(html_content)
        
        print(f"[+] Report saved as report_{timestamp}.html")

